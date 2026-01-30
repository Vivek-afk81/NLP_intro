from datetime import datetime
import webbrowser
import requests
import os

date_msgs = ["what's the date today?", "tell me the date", "date today", "current date"]
time_msgs = ["what's the time?", "tell me the time", "current time", "time now"]
greet_msgs = ["hi", "hello", "hey", "greetings", "what's up"]
websites_msgs = ["google", "youtube", "facebook", "twitter"]
news_msgs = ["give me the latest news", "news update", "latest news", "news headlines"]

API_KEY = os.getenv("NEWS_API")
def fetch_latest_news():
    url = f"https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey={API_KEY}"
    response = requests.get(url)
    print("Status:", response.status_code)

    if response.status_code==200:
        data =response.json()
        articles= data.get("articles", [])
        for i,article in enumerate(articles[:10], 1):
            print(f"{i}.{article['title']}")
    else:
        print("Failed to fetch news.")
def define_word(word):
    url=f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response=requests.get(url)
    if response.status_code==200:
        data=response.json()
        definition=data[0]['meanings'][0]['definitions'][0]['definition']
        print(f"The definition of {word} is: {definition}")
    else:
        print("OOH Its a new word for me!")


chat=True
while chat:
    user_msg = input("enter your message: ").lower()

    if user_msg in greet_msgs:
        print("friday:Hello! How are you?")

    elif user_msg =="how high are you":
        print("friday:It's high, how are you?")

    elif user_msg =="exit":
        print("friday:Goodbye! Have a great day!")
        chat = False

    elif "open" in user_msg and any(site in user_msg for site in websites_msgs):
        site =user_msg.split()[-1]
        webbrowser.open(f"https://www.{site}.com")

    elif "calculate" in user_msg:
        try:
            expression = user_msg.split("calculate")[-1].strip()
            result = eval(expression)
            print(f"friday: The result of your expression {expression} is {result}")
        except:
            print("friday: Sorry, I couldn't calculate that expression.")

    elif user_msg in date_msgs:
        print("friday: Today's date is", datetime.now().strftime("%Y-%m-%d"))

    elif user_msg in time_msgs:
        print("friday: The current time is", datetime.now().strftime("%I:%M:%S %p"))

    elif user_msg in news_msgs:
        print("friday: Here are the latest news headlines:")
        fetch_latest_news()

    elif "define" in user_msg:
        word = user_msg.split("define")[-1].strip()
        define_word(word)

    else:
        print("friday: I'm sorry, I can only respond to greetings at the moment.")
