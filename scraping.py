import requests
from bs4 import BeautifulSoup

website_url = 'https://infopark.in/companies/job-search'
keywords = ['node', 'react']
output_file = open('jobs.txt', 'w')
res = requests.get(website_url)
soup = BeautifulSoup(res.text, 'lxml')
jobs = soup.find_all('div', {"class": "row company-list joblist"})

for job in jobs:
    title_element = job.find('a')
    title = title_element.text
    link = title_element['href']
    company = job.find('div', {'class': 'jobs-comp-name'}).text
    date = job.find('div', {'class' : 'job-date'}).text

    if any(word.lower() in title.lower() for word in keywords):         # convert all words to lower case and then search
        print(title, company, date)
        output_file.write(title + " " + company + " " + date + "\n" + link + "\n\n")
    