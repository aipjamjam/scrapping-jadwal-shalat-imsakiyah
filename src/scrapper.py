from requests import get
from bs4 import BeautifulSoup
import pandas as pd


def _base_url(city: str) -> str:
    url = f"https://www.kompas.com/ramadhan/jadwal-imsakiyah/{city}"
    return url


def _get_page(url: str) -> BeautifulSoup:
    page = get(url)
    soup = BeautifulSoup(page.text, "lxml")
    return soup


def _get_cities():
    url = "https://www.kompas.com/ramadhan/jadwal-imsakiyah/kota-jambi"
    soup = _get_page(url)
    options = soup.find("select", {"name": "state"}).findAll("option")
    cities = []
    for i in options:
        name = i.text
        city = i["value"]

        cities.append({
            "city": city,
            "name": name
        })
    return cities


def _get_imsak_schedule(city: str) -> str:
    uri = _base_url(city)
    df = pd.read_html(uri)

    df = df[0].to_json(orient="records")
    return df