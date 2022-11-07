import sys
import requests
import json



def getting_req(val):
    try:
        r=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except:
        pass
    else:
        o=r.json()
        res=o["bpi"]["USD"]["rate_float"]
        res=res*val
        print(f"${res:,.4f}")





def user_input():
    if(len(sys.argv)<2):
        sys.exit("Missing command-line argument")
    elif(not(sys.argv[1].isdigit()) and str(sys.argv[1]).find(".")==-1):
        sys.exit("Command-line argument is not a number")
    else:
        getting_req(float(sys.argv[1]))

user_input()