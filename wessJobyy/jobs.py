import requests as rq
from bs4 import BeautifulSoup as bs
from fastapi import FastAPI

app = FastAPI()


# Define the root endpoint
@app.get("/")
def read_root():
    return "Server is running"

# Get jobs from Wuzzuf  
@app.get("/jobs_wuzzuf")
def get_wuzzuf():
    res = rq.get("https://wuzzuf.net/a/IT-Software-Development-Jobs-in-Egypt?ref=browse-jobs")
    soup = bs(res.content, "html.parser")
    jobs = soup.select("div.css-1gatmva") 
    jobsList = []
    for job in jobs:
        title = job.select_one("h2.css-m604qf a").text.strip()
        company = job.select_one("div.css-d7j1kk a").text.strip()
        location = job.select_one("span.css-5wys0k").text.strip()
        posted = job.select_one("div.css-4c4ojb").text.strip()
        work_state = job.select_one("div.css-1lh32fc").text.strip()
        experience = job.select_one("div.css-1lh32fc").find_next("div").text.strip()
        # print(f"Title: {title}")
        # print(f"Company: {company}")
        # print(f"Location: {location}")
        # print(f"Posted: {posted}")
        # print(f"Work State: {work_state}")
        # print(f"Experience: {experience}")
        jobsList.append({
            "title": title,
            "company": company,
            "location": location,
            "posted": posted,
            "work_state": work_state,
            "experience": experience
        })
    return jobsList