def Speak(str):
        from win32com.client import Dispatch
        speak = Dispatch("SAPI.SpVoice")
        speak.Speak(str)

if __name__ == '__main__':
    import requests
    import json
    Speak("Today's News is")
    url = "http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=fbedd65c70e94aee99bbf6e7c471612f"
    news = requests.get(url).text
    news1 = json.loads(news)
    head = news1["articles"]
    for articles in head:
        Speak(articles["title"])
        print(articles["title"])
        Speak("Ok now i am reading next news of the day, Please listen to it carefully")
    Speak("That is it for today. See you tomorrow!!")
