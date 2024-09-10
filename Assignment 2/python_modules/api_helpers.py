# Built in imports
import json
import time

# External imports
import requests as req

# API RESPONSE CODE REFERENCE
# Response Codes
# The API appends a "Response Code" to each API Call to help tell developers what the API is doing.
# Code 0: Success Returned results successfully.
# Code 1: No Results Could not return results. The API doesn't have enough questions for your query. (Ex. Asking for 50 Questions in a Category that only has 20.)
# Code 2: Invalid Parameter Contains an invalid parameter. Arguments passed in aren't valid. (Ex. Amount = Five)
# Code 3: Token Not Found Session Token does not exist.
# Code 4: Token Empty Session Token has returned all possible questions for the specified query. Resetting the Token is necessary.
# Code 5: Rate Limit Too many requests have occurred. Each IP can only access the API once every 5 seconds.

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

        if request.status_code == 200:
            # load the error code using json loads method
            code = json.loads(request.text)['response_code']

            match code:
                # if the code is 0  return the results data
                case 0:
                    return json.loads(request.text)['results']
                # if the code is 4 it means the token is empty (all questions exhausted) and needs to be reset, therefore reset the token
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
        else:
            raise Exception("Status code: " + str(request.status_code))

def generate_api_request_method_2(amount=None, category=None, difficulty=None, question_type=None, token=None):
    endpoint = "https://opentdb.com/api.php"

    payload = {
        "amount": amount,
        "category": category,
        "difficulty": difficulty,
        "type": question_type,
        "token": token
    }

    response = req.get(url=endpoint, params=payload)
    response_code = int(response.text[17:18])

    retry_count = 0

    if response.status_code == 200:
        while True:
            # Code 0: Success Returned results successfully. Therefore, return the data.
            if response_code == 0:
                request_data = response.json()
                return request_data['results']

            print("\nSorry there has been an error with the HTTP request.\n")
            time.sleep(5)
            if response_code == 1:
                print("Code 1: No Results Could not return results. The API doesn't have enough questions for your query. "
                      "(Ex. Asking for 50 Questions in a Category that only has 20.). Please report this error to us so "
                      "that we can fix the parameters")
            elif response_code == 2:
                print("Code 2: Invalid Parameter Contains an invalid parameter. Arguments passed in aren't valid. "
                      "(Ex. Amount = Five) please report this error so that we can fix the parameters")
            elif response_code ==3:
                print("Code 3: Token Not Found. Session Token does not exist. Getting a new session token and trying again\n")
                payload["token"] = get_session_token()['token']
                response = req.get(url=endpoint, params=payload)
                response_code = int(response.text[17:18])
                time.sleep(5)
            elif response_code == 4:
                print("Code 4: Token Empty. Session Token has returned all possible questions for the specified query. Resetting the Token and trying again.\n")
                token_dictionary = reset_session_token(payload['token'])
                payload["token"] = token_dictionary['token']
                response = req.get(url=endpoint, params=payload)
                response_code = int(response.text[17:18])
                time.sleep(5)
            elif response_code == 5:
                print("Code 5: Rate Limit Too many requests have occurred. Each IP can only access the API once every 5 seconds. Waiting and trying again")
                time.sleep(5)
            else:
                print("Unknown response code")
                return

            retry_count += 1

            if retry_count > 5:
                raise Exception("Retry count exceeded the maximum limit of 5.")
    else:
        raise Exception("Status code: " + str(response.status_code))


# testing area for method 2 API request:
# token =get_session_token()
# token = token['token']
# token = "cb5e427a4a464b9828adffd80b856b9a0dc01b12205dcfedac2eff8676336bb7"
# # api_parameters:
# amount=31
# category=10
# difficulty = 'easy'
# token=token
# api_data = generate_api_request_method_2(amount=amount, category=category, token=token, difficulty=difficulty)
# print(api_data)
# time.sleep(5)
# api_data = generate_api_request_method_2(amount=amount, category=category, token=token, difficulty=difficulty)
# print(api_data)