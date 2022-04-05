import requests
from bs4 import BeautifulSoup


URL = f"https://stackoverflow.com/jobs/companies?tl=python"

def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find("div",{"class":"s-pagination"}).find_all('a')
  last_page = pages[-2].get_text(strip=True)
  return int(last_page)
  

def extract_job(html):
  title = html.find("div",{"class":"flex--item fl1 text mb0"}).find("h2").find("a")
  company, location = html.find("div",{"class":"d-flex gs12 gsx ff-row-wrap fs-body1"}).find_all("div")
  print(company,location)
  
  return {'title':title}







def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    result = requests.get(f"{URL}&pg={page+1}")
    soup = BeautifulSoup(result.text,"html.parser")
    results = soup.find_all("div",{"class":"dismiss-trigger js-dismiss-company ps-absolute r12 fc-black-500 c-pointer"})
    for result in results:
      print(result["data-id"])
    
  
  

def get_jobs():
  last_page =  get_last_page()
  jobs = extract_jobs(last_page)
  return jobs

