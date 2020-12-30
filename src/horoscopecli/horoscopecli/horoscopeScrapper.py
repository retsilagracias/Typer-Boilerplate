from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import socket


def getHoroscopeScrapper(sign: str, category: str):
    dic = {"love": 0, "work": 1, "finance": 2, "self": 3, "family": 4}
    urlpage = f"https://www.evozen.fr/horoscope/horoscope-du-jour/{sign}"
    try:
        page = urllib.request.urlopen(urlpage, timeout=30)
    except urllib.error.HTTPError as e:
        print("http")
        return ("ERROR: HTTPError occured: ", e.code)
    except urllib.error.URLError as e:
        print("url")
        return ("ERROR: URLError occured: ", f"Site url: https://www.evozen.fr/horoscope/horoscope-du-jour/{sign}")
    except socket.timeout as e:
        print("timout")
        return ("ERROR: Socket timeout occured of 30seconds, try again later: ", f"Site url: https://www.evozen.fr/horoscope/horoscope-du-jour/{sign}")
    else:
        soup = BeautifulSoup(page, 'html.parser')
        myDivs = soup.find_all("div", {"class": "daily-tex t-container"})
        div = dic[category]
        data = myDivs[div].find_all('p')
        return (data[0].get_text(), data[1].get_text())