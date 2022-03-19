import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}&start=9999"
def extract_indeed_pages():
  pages =[]
  result =         requests.get(URL)
  soup =   BeautifulSoup(result.text, 'html.parser')

  pagination=soup.find("div",{"class":"pagination"})
  links = pagination.find_all('a')
  pages=[]
  for link in links:
    pages.append(link.string)

  max_page = int(pages[1])+1
  return max_page


def extract_indeed_jobs(last_page):
  jobs = []
  for page in range(last_page):
    result=requests.get(f"{URL}&start={page*LIMIT}")
    print(result.status_code)
  return jobs