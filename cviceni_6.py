import sys 
import requests 

if __name__ == "__main__": 
    
    if len(sys.argv) <= 2:
        print(f"Usage: {sys.argv[0]} <pefix>")
        sys.exit()

    pefix = sys.argv[1]

    url = f"https://deta.carnewschina.com/suggest/q={pefix}"

    respone = requests.get(url
    if not respone.ok:
        sys.exit()

    data = respone.json(respone.text)

    for model in data["models"]:
        print(model)
    