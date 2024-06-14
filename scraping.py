import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# scraping do slido
def scrape_slido(url, output_option=''):
    # Configuração do webdriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # para abrir o navegador em segundo plano

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(10) # GAMBI!!! Melhorar isso

    page = driver.execute_script('return document.body.innerHTML')
    soup = BeautifulSoup(''.join(page), 'html.parser')

    questions = []
    votes = []
    authors = []

    # Valida dados carregados
    if not soup.find('div', class_='card question-item'):
        print('Parece não haver perguntas na página carregada. Verifique a URL e tente novamente.')
        return
    

    # class_='card question-item' é o mais próximo que encontrei para mapear os cards que contém as perguntas
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

    # Cria o DataFrame
    data = {
        'QUEM': authors,
        'VOTOS': votes,
        'PERGUNTA': questions
    }

    df = pd.DataFrame(data)
    return df
