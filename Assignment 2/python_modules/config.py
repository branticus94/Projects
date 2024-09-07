# As the code was becoming quite large I pulled out lists used to randomly give the
# user messages throughout the game. This makes it easier to navigate and I can
# change the messages when needed

correct_celebrations = [
                            "You nailed it! Spot on!",
                            "Ding, ding, ding! You've got it!",
                            "Bullseye! You’re on fire!",
                            "As Sherlock would say, 'Elementary, my dear Watson!'",
                            "Correct! You must have a crystal ball!",
                            "And the crowd goes wild! You're absolutely right!",
                            "You aced it—no ‘question’ about it!",
                            "Correct answer uploaded and approved!",
                            "Abracadabra! You've conjured up the correct answer!"
                            ]

incorrect_letdowns = [
                            "Not quite, but nice try!",
                            "Oops! Close, but no cigar!",
                            "Almost there, but not this time!",
                            "Oh, so close! But no points this round.",
                            "Uh-oh! Looks like your answer needs a reboot!",
                            "Sorry, that answer missed the mark—better luck next time!",
                            "Bibbidi-bobbidi-wrong! But don’t give up!",
                            "Not quite! But I see what you were going for!",
                            "Swing and a miss! But you're still in the game!",
                            "Incorrect, but don’t worry—there’s always the next question!"
                            ]

psych_up_comments = [
                            "You look like you’ve got the whole textbook memorized!",
                            "Is that your quiz face? Because it’s on point.",
                            "You’re rocking that ‘I’m totally prepared’ look.",
                            "I see someone’s been hitting the books hard!",
                            "Are you ready to ace this like a quiz master?",
                            "You look like you’ve been practicing for this all week!",
                            "Ready for the quiz showdown? You’re dressed for success!",
                            "I can tell you’ve been studying—your quiz game is strong.",
                            "You’ve got that ‘I’m going to crush this quiz’ vibe.",
                            "You look like you’re about to drop some serious knowledge!"
                            ]

appearance_comments = [
                            "Are you testing out the ‘rolled-out-of-bed’ look today? It’s definitely unique!",
                            "Is today ‘dress like no one’s watching’ day? Because you’re nailing it!",
                            "You’re really embracing that ‘casual chic’ style—casual being the keyword!",
                            "I see you’re going for the ‘I just woke up’ aesthetic—bold choice!",
                            "It looks like you’re channeling your inner ‘rebel against grooming’ vibe!",
                            "Your look is definitely one-of-a-kind—maybe it’s time for a little touch-up?",
                            "You’re rocking the ‘I-didn’t-have-time’ look—impressive in its own way!",
                            "Looks like your style is ‘authentically un-styled’—very avant-garde!",
                            "You’ve definitely got that ‘I’m-too-cool-for-grooming’ vibe going on!",
                            ]

agree_responses = [
                            "                         Time to play.                      ",
                            "                    Let's see how you do.                   ",
                            "              Hope you're ready for a challenge.            ",
                            "                Let's jump into the action.                 ",
                            "                     Let's start the fun.                   ",
                            "                  You're in! Let’s begin.                   ",
                            "               Perfect! The game begins now.                ",
                            "                 Buckle up, it's game time.                 ",
                            "              Awesome! Let's see what happens.              "
                            ]

pre_selected_categories = [
                            "General Knowledge",
                            "Entertainment: Books",
                            "Entertainment: Film",
                            "Entertainment: Music",
                            "Science & Nature",
                            "Sports",
                            "Geography",
                            "History",
                            "Art",
                            "View all"
                            ]

easy_mode_comments = [
                            "Easy mode, huh? Let’s get those brain cells warmed up!",
                            "Taking it easy, I see. Let’s roll!",
                            "You're in for a smooth ride! Let’s crush this!",
                            "Easy mode activated—let’s see how fast you can breeze through!",
                            "Nothing wrong with starting simple. Let’s ace it!",
                            "Choosing easy mode—great strategy! Let’s rack up those points!",
                            "You’re about to be unstoppable in easy mode!",
                            "Easy mode? More like winning mode. Let’s go!",
                            "Cruising through easy mode? Let's make it fun!",
                            "Easy mode selected! Prepare for victory!"
                            ]

medium_mode_comments = [
                            "Medium mode, huh? A fine balance of brains and brawn!",
                            "Not too easy, not too hard—let’s find your sweet spot!",
                            "Medium mode selected! Just enough challenge to keep things interesting!",
                            "You’re stepping it up with medium mode. Let’s see what you’ve got!",
                            "Not afraid of a little challenge, are we? Let’s ace medium mode!",
                            "Medium mode: the perfect level for sharpening those skills!",
                            "In the middle of the road? Let's make sure you dominate!",
                            "Medium mode? You’re ready for the thrill of a good challenge!",
                            "Brave enough for medium mode? Let’s bring on the fun!",
                            "Medium it is! Time to show off those well-balanced smarts!"
                            ]

hard_mode_comments = [
                            "Hard mode? Bold move! Let’s see if you’ve got what it takes!",
                            "Oh, you’re not messing around—hard mode it is!",
                            "Ready to test those brain cells to the limit? Hard mode engaged!",
                            "Hard mode? You must like living on the edge!",
                            "No fear in your game—hard mode it is. Let’s do this!",
                            "You asked for a challenge, and hard mode is here to deliver!",
                            "Strap in! Hard mode means no mercy!",
                            "Going for the ultimate test with hard mode? Let’s crush it!",
                            "Hard mode? You’re either a genius or a thrill-seeker. Let’s find out!",
                            "Only the brave choose hard mode. Time to earn those bragging rights!"
                            ]
all_difficulties_comments = [
                            "All difficulties? You're in for a wild ride!",
                            "Brave soul! You’ve just unlocked the full spectrum of challenges!",
                            "Feeling adventurous? Let’s tackle everything the game throws at you!",
                            "All difficulties selected—get ready for the ultimate quiz gauntlet!",
                            "Mixing it up, I see! Let’s dance between easy, medium, and hard!",
                            "You're going all-in! No difficulty left behind!",
                            "All levels? You must be in it for the full experience!",
                            "One moment it's easy, the next it's tough—let’s keep you on your toes!",
                            "All difficulties? You like surprises, don't you? Let’s go!",
                            "Everything at once? Get ready for a challenge rollercoaster!"
                            ]

leaderboard_comments = [
                            "Welcome to the leaderboard! Who's claiming the top spot today?",
                            "The competition is fierce! Are you among the top contenders, or is it time to make your move?",
                            "Let's take a look at the champions! Will your name be etched in glory?",
                            "Checking the leaderboard... Will you reign supreme, or is there room to climb?",
                            "The leaderboard is up! Are you dominating the ranks or plotting your comeback?",
                            "Ready to see where you stand? The leaderboard is calling!",
                            "Who's the hero of the hour? Time to reveal the leaderboard and find out!",
                            "The results are in! Are you leading the charge or trailing behind the legends?",
                            "Leaderboard loading... Can you feel the excitement? Let's see who's on top!",
                            "The leaderboard awaits! Will you be crowned victor, or is it time to up your game?"
                            ]
