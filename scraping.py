import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# scraping slido questions page
def scrape_slido(url):
    """"
    Function to scrape questions from a Slido page.
    Parameters: url (str) - The URL of the Slido page to scrape.
    When a valid URL, it returns a DataFrame with the questions, authors and votes(likes).
    """
    
    print('Starting scraping... This may take a few seconds.')
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  #Opening the web page in selenium without opening the browser
    
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(10) # Crappy code! Necessary to give some time to async load. Need to make it better!

    page = driver.execute_script('return document.body.innerHTML')
    soup = BeautifulSoup(''.join(page), 'html.parser')

    questions = []
    votes = []
    authors = []

    # Validdating if there are questions in the page
    # class_='card question-item' is the closest I found to map the cards that contains the questions
    if not soup.find('div', class_='card question-item'):
        print('It seems there are no questions in the loaded page. Check the URL and try again.')
        exit(1)
    
    print(f'Total number of questions found: {len(soup.find_all("div", class_="card question-item"))}')
    for question in soup.find_all('div', class_='card question-item'):
        author_div = question.find('div', {'data-testid': 'question-author'})
        author_name = author_div.text if author_div else None

        vote_div = question.find('div', class_='score question-item__score score--only-upvotes')
        vote_count = vote_div.find('span').get_text() if vote_div else None

        question_div = question.find('div', {'data-testid': 'question-text'})
        question_text = question_div.find('span').get_text() if question_div else None

        questions.append(question_text)
        votes.append(vote_count)
        authors.append(author_name)

    # Create a DataFrame with the data
    data = {
        'WHO': authors,
        'LIKES': votes,
        'QUESTION': questions
    }
    df = pd.DataFrame(data)
    return df
