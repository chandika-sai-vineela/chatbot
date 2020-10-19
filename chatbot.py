from datetime import datetime
import requests


def intro():
    print("Hello user! I am volte. May I know your name?")

def time():
    current_time=datetime.now()
    if(current_time.hour >0 and current_time.hour < 12):
        greet_of_the_day="Good Morning"
    if(current_time.hour >= 12 and current_time.hour < 16):
        greet_of_the_day="Good Afternoon"
    if(current_time.hour >= 16 and current_time.hour < 21):
        greet_of_the_day="Good Evening"
    if(current_time.hour >= 21):
        greet_of_the_day="Good Night"
    print(greet_of_the_day)

def greet(name):
    print(name,"Nice to meet you")
    print("I can help you to know COVID cases in any country")

def volte():
    intro()
    name=input("Enter your name:")
    time()
    greet(name)

def stop():
    n=input("do u want to see result of another country yes/no :")
    if(n=="yes"):
        Demo()
    elif(n=="no"):
        print("tq for sepnding ur valuble time")
    else:
        print("enter only yes/no other or invalid")
        stop()

def Demo():
    tag=input("Enter country name:")
    tag.strip()
    tag.replace(" ","%20")
    link='https://coronavirus-19-api.herokuapp.com/countries/'+tag
    page=requests.get(link)
    try:
        print(f"Country Name = {page.json()['country']}")
        print(f"Total Cases  = {page.json()['cases']}") 
        print(f"TodayCases = {page.json()['todayCases']}")
        print(f"deaths = {page.json()['deaths']}")
        print(f"todayDeaths = {page.json()['todayDeaths']}") 
        print(f"recovered = {page.json()['recovered']}")
        print(f"active = {page.json()['active']}")
        print(f"critical = {page.json()['critical']}")
        print(f"casesPerOneMillion = {page.json()['casesPerOneMillion']}")
        print(f"deathsPerOneMillion = {page.json()['deathsPerOneMillion']}")
        print(f"totalTests = {page.json()['totalTests']}")
        print(f"testsPerOneMillion = {page.json()['testsPerOneMillion']}")
    except Exception as e:
        print("Enter a correct country name")
        Demo()
    stop()

volte()
Demo()