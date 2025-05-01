import requests as rq
from bs4 import BeautifulSoup as bs


def get_wuzzuf(job="software developer"):
    res = rq.get(f"https://wuzzuf.net/search/jobs/?q=${job}")
    soup = bs(res.content, "html.parser")
    jobs = soup.select("div.css-1gatmva") 
    jobsList = []
    for job in jobs:
        title = job.select_one("h2.css-m604qf a").text.strip()
        company = job.select_one("div.css-d7j1kk a").text.strip()
        location = job.select_one("span.css-5wys0k").text.strip()
        posted_element = job.select_one("div.css-4c4ojb")
        posted = posted_element.text.strip() if posted_element else "Not specified"
        work_state_div = job.select_one("div.css-1lh32fc")

        work_state = []
        if work_state_div:
            state_elements = work_state_div.select("a span")
            work_state = [state.text.strip() for state in state_elements]
        work_state = ", ".join(work_state) if work_state else "Not specified"

        experience = job.select_one("div.css-1lh32fc").find_next("div").text.strip()

        link_element = job.select_one("h2.css-m604qf a")
        link_job = link_element["href"] if link_element else "No link found"

        # print("---------------")

        # print(f"Title: {title}")
        # print(f"Company: {company}")
        # print(f"Location: {location}")
        # print(f"Posted: {posted}")
        # print(f"Work State: {work_state}")
        # print(f"Experience: {experience}")
        # print(f"Link: {link_job}")

        # print("---------------")

        jobsList.append({
            "title": title,
            "company": company,
            "location": location,
            "posted": posted,
            "work_state": work_state,
            "experience": experience,
            # "job_link": link_tag
        })
    return jobsList

# print(get_wuzzuf())


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# import time

# options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# driver = webdriver.Chrome(options=options)

# def get_indeed():
#     driver.get("https://hi-interns.com/internships")
#     time.sleep(3)
#     job_cards = driver.find_elements(By.CLASS_NAME, 'overflow-clip')
#     for job in job_cards:
#         print(job.text)
    
#     driver.quit()

# get_indeed()
