import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# scraping do slido
def scrape_slido(url):
    print('Iniciando scraping...')
    # Configuração do webdriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # para abrir o navegador em segundo plano
    # Adiciona um User-Agent
    # options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537')

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(10) # GAMBI!!! Melhorar isso

    page = driver.execute_script('return document.body.innerHTML')
    soup = BeautifulSoup(''.join(page), 'html.parser')
    # Conta o número de tags
    # print(f'Número de tags HTML encontradas: {len(soup.find_all())}')

    questions = []
    votes = []
    authors = []

    # Valida dados carregados
    if not soup.find('div', class_='card question-item'):
        print('Parece não haver perguntas na página carregada. Verifique a URL e tente novamente.')
        exit(1)
    
    # class_='card question-item' é o mais próximo que encontrei para mapear os cards que contém as perguntas
    print(f'Número de perguntas encontradas: {len(soup.find_all("div", class_="card question-item"))}')
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
