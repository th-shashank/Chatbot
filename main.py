from datetime import datetime
from colorama import Fore, Style, init

init(autoreset = True)

responses = {
    "hi": "Hello! How can I help you?",
    "hello": "Hey! Nice to meet you.",
    "hey": "Hey there!",
    "good morning": "Good morning! Have a great day.",
    "your name": "I am SmartBot v1.0.",
    "who are you": "I am a Python-based CLI chatbot.",
    "how are you": "I'm doing well! Thanks for asking.",
    "thank you": "You're welcome!",
    "bye": "Goodbye! Have a great day."
}

def bot_get_reply(user_message):
    # user_message = user_message.lower().strip()

    now = datetime.now()

    if user_message in responses:
        return responses[user_message]
    elif "time" in user_message or "kitne baje" in user_message:
        return now.strftime("%H:%M:%S")
    elif "date" in user_message or "tarikh" in user_message:
        return now.strftime("%d-%m-%Y")
    elif "day" in user_message:
        return now.strftime("%A")
    elif "year" in user_message:
        return now.strftime("%Y")
    else:
        return "Sorry, I don't understand that yet. Type 'help'."

def main():
    while True:
        now = datetime.now()

        user_message = str(input(Fore.CYAN+Style.BRIGHT+"YOU :\t").lower().strip())

        bot_reply=bot_get_reply(user_message)
        print(Fore.MAGENTA + Style.BRIGHT+ f"BOT: {bot_reply}".rjust(80))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.YELLOW+"\n BOT: Program Stopped")
    except EOFError:
        print(Fore.YELLOW+"BOT : Input closed , GoodBye!!")
    except NameError as error:
        print(Fore.YELLOW+f"BOT : NameError : {error}")
    except Exception as error:
        print(Fore.RED+f"\nBOT : Start error : {error}")