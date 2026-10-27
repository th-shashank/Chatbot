from datetime import datetime
from colorama import Fore, Style, init

init(autoreset = True)

now = datetime.now()
def main():
    responses={
        "hi":"hello ",
        "good morning":"good morning ",
        "your name":"Bot v1",
    } 
    while True:
        user_massege = str(input(Fore.CYAN+Style.BRIGHT+"YOU :\t").lower().strip())

        if user_massege in ("exit","tata","clear"):
            print("Bot: Bye ")
            break

        responses["date"]=now.strftime("%d :%m :%y")
        responses["time"]=now.strftime("%H :%M :%S")
        responses["day"]=now.strftime("%A")
        responses["year"]=now.strftime("%Y")

        bot_reply = responses.get(user_massege, "Sorry ,  i can't able to process try another massage ")
        print(Fore.MAGENTA+Style.BRIGHT+f"bot: {bot_reply}".rjust(100))

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