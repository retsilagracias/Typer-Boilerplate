import requests
import json

def getHoroscopeApi(sign: str, flag: str):
    try:
        r = requests.get(f"http://horoscope-api.herokuapp.com/horoscope/{flag}/{sign}")
        if r.status_code != 200:
            return (False, "ERROR: Sorry, we have found an issue with the API we are currently using.")
        rText = json.loads(r.text)
        return (True, rText["horoscope"])
    except:
        return (False, "ERROR: Sorry, your request didn't went through, bad network error.")