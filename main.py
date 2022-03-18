import requests
from bs4 import BeautifulSoup

URL = "https://kr.indeed.com/jobs?q=python&limit=50&radius=25"
page = requests.get(URL)


soup = BeautifulSoup(page.text, "html.parser")


pagination = soup.find("ul",{"class":"pagination-list"})


pages = pagination.find_all('a')


list = []
for page_result in pages:
  list.append(page_result.find("span"))
print(list[:-1])