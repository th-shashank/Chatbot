from datetime import datetime
from colorama import Fore, Style, init

init(autoreset = True)

now = datetime.now()

responses={
    "hi":"hello ",
    "good morning":"good morning ",
    "your name":"Bot v1",
    "date": now.strftime("%d-%m-%y"),
    "time": now.strftime("%H:%M:%S"),
    "year": now.strftime("%Y"),
    "day": now.strftime("%A")
}

while True:
    user_massege = str(input(Fore.CYAN+Style.BRIGHT+"YOU :\t").lower().strip())

    if user_massege in ("exit","tata"):
        print("Bot: Bye ")
        break

    responses["date"]=now.strftime("%d :%m :%y")
    responses["time"]=now.strftime("%H :%M :%S")
    responses["day"]=now.strftime("%A")
    responses["year"]=now.strftime("%Y")

    bot_reply = responses.get(user_massege, "Sorry ,  i can't able to process try another massage ")
    print(Fore.MAGENTA+Style.BRIGHT+f"bot: {bot_reply}")