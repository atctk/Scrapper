import requests
from bs4 import BeautifulSoup


URL = f"https://stackoverflow.com/jobs?q=python"

def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pagination = soup.find("div", {"class": "s-pagination"})
  if pagination:
    pages = pagination.find_all("a")
  print(pagination)

def get_jobs():
  last_page =  get_last_page()
  return []

