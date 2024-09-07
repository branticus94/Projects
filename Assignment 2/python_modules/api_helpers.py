# Built in imports
import json
import time

# External imports
import requests as req
from numpy.f2py.auxfuncs import throw_error

# Have left a multiline comment below detailing the API response codes for my reference.
"""
    Response Codes
    The API appends a "Response Code" to each API Call to help tell developers what the API is doing.
    Code 0: Success Returned results successfully.
    Code 1: No Results Could not return results. The API doesn't have enough questions for your query. (Ex. Asking for 50 Questions in a Category that only has 20.)
    Code 2: Invalid Parameter Contains an invalid parameter. Arguments passed in aren't valid. (Ex. Amount = Five)
    Code 3: Token Not Found Session Token does not exist.
    Code 4: Token Empty Session Token has returned all possible questions for the specified query. Resetting the Token is necessary.
    Code 5: Rate Limit Too many requests have occurred. Each IP can only access the API once every 5 seconds.
"""

def get_session_token():
    # Use the get method of the requests library to get a session token -
    # this is useful as it ensures that you don't get served the same questions more than once
    retrieve_token = req.get("https://opentdb.com/api_token.php?command=request")

    # Use the json loads method to save the session token
    json_session_token = json.loads(retrieve_token.text)

    # return the json of the session token API request
    return json_session_token

def reset_session_token(session_token):
    # reset the session token, this is used in knockout mode
    reset_token = req.get("https://opentdb.com/api_token.php?command=reset&token="+session_token)

    # use the json loads method to save the reset token as a json
    reset_token_json = json.loads(reset_token.text)

    # return the reset token json
    return reset_token_json

def get_categories_list():
    # get the list of categories from the category api using the get method
    categories = req.get('https://opentdb.com/api_category.php')

    # convert the output of the request to a json for manipulation
    categories_json = json.loads(categories.text)

    # return the categories json
    return categories_json

def get_category_question_count(category_id):
    # Use the get method of the requests library to get the number of questions in a given category
    number_questions_in_category = req.get(f"https://opentdb.com/api_count.php?category={category_id}")

    # Use the loads method of the json library to get the number of questions in a category
    number_questions_in_category_json = json.loads(number_questions_in_category.text)

    # return the number of questions in category json
    return number_questions_in_category_json

def generate_api_request_url(amount=None, category=None, difficulty=None, question_type=None, token=None):

    # creates a list to hold all the parameters for the API call
    query_parameters = []

    # If any given parameter is not None then append it to the query parameters list
    if amount is not None:
        query_parameters.append(f"amount={amount}")

    if category is not None:
        query_parameters.append(f"category={category}")

    if difficulty is not None:
        query_parameters.append(f"difficulty={difficulty}")

    if question_type is not None:
        query_parameters.append(f"type={question_type}")

    if token is not None:
       query_parameters.append(f"token={token}")

    # use the join method create a query string, the API string is joined with a '&'
    query_string = '&'.join(query_parameters)

    # generate the url using the query string
    url = f"https://opentdb.com/api.php?{query_string}"

    # return the url
    return url

def get_api_data(api_url, session_token):
    retry_count = 0

    while True:
        # Perform the API request with the given URL containing the session token
        request = req.get(api_url)

        # load the error code using json loads method
        code = json.loads(request.text)['response_code']

        match code:
            # if the code is 0  return the results data
            case 0:
                return json.loads(request.text)['results']
            # if the code is 4 it means the token is empty and needs to be reset, therefore reset the token
            case 4:
                # reset the session token
                session_token = reset_session_token(session_token)
                time.sleep(5)
            # if the code is 3 token no longer exists therefore remove token from api url string and get new one, add to api url
            case 3:
                api_url = api_url[:-64]
                session_token = get_session_token()['token']
                api_url = api_url + session_token
                time.sleep(5)
        retry_count += 1

        if retry_count > 5:
            raise Exception("Retry count exceeded the maximum limit of 5.")

