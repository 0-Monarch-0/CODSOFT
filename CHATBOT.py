import time
import re
# function having the keys=moods values=responses takes in the user input and iterates with the keywords and gives the appropriate response.
def mood_checker(user_input):
    moods_responses = {

        "happy": "I'm glad to hear that you're happy!\n If you need me i am here for you?",
        "good": "That's great to hear!.\nIf you need me i am here for you?",
        "nice": "Wonderful! I'm happy for you.\nIs there anything else i can help you with?",
        "sad": "I'm sorry to hear that.\n Is there anything specific you'd like to talk about?",
        "stress": "I understand. Dealing with stress can be challenging.\n one way to dela with stress is to take a break and do something you enjoy.",
        "excited": "That's fantastic! What's making you feel excited?",
        "anxious": "I hear you. Anxiety can be tough.\n Have you tried any relaxation techniques? \n I find breathing exercises helpful.",
        "angry": "I see. Dealing with anger is important.\n Would you like tips on calming down?\n I find breathing exercises helpful.",
        "lonely": "Feeling lonely can be tough.\n Is there someone you'd like to reach out to?\n I find talking to a friend helpful.",
        "motivated": "Great to hear you're motivated!\n use your motivation to do something you enjoy.",
        "bored": "Boredom happens. Try to get a new skill like in a game.\n I find learning something new helpful.",
        "grateful": "It's wonderful to feel grateful! What are you thankful for today?",
        "overwhelmed": "Feeling overwhelmed is common. Let's break it down. What's on your plate right now?\n do it one by one.",
        "music": "try spotify or some other music platoforms according to your taste in songs.",
        "friends": " try to reach out to your friends and talk to them.\n sharing with friends can help you feel better.",
        "thank you": "You're welcome! I'm always here to listen.",
    
    }
    
    default_response = "sry I have a limited database. I am still learning. you can reach google for more information."

    for moods, response in moods_responses.items():
        if moods in user_input:
            return "Mia:"+response

    return default_response

#main function
        
print("🌈 Hi I am BAYMAX - Your Personal Mood Tracker! 🌟")
time.sleep(1)
print(" I'm here to help you understand and navigate your emotions.")
time.sleep(2) 
print("please try to respond one at a time.")
time.sleep(2)
print("BAYMAX:"+"what is your name?")
user_name = input("you:")
print("BAYMAX:"+"Hello "+user_name+"! How are you feeling today?")
time.sleep(1)

#taking User input
while(True):    
    prime_input = input("you:")
    # removing unwanted characters
    split_message = re.split(r'\s+|[,;?!.-]\s*', prime_input.lower())
    user_input = split_message
    #add lemmetizer here
    if (mood_checker(user_input)=="BAYMAX:You're welcome! I'm always here to listen."):
        break
    else:
        print(mood_checker(user_input))
        time.sleep(1)
time.sleep(1)
print("Thank you for using BAYMAX - Your Personal Mood Tracker! 🌟")
