import sys
from scraping import scrape_slido
from funcoes import valida_url
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Adicionar uma URL do slido como parametro.")
        print("""
        Exemplo:python slido-scraping.py https://app.sli.do/event/abc123 [output_option]
        output_option: table, json, csv
              """)
    elif len(sys.argv) < 3:
        url = sys.argv[1]
        if not valida_url(url): sys.exit()
        df = scrape_slido(url)
        print(df)
    else:
        url = sys.argv[1]
        if not valida_url(url): sys.exit()
        output_option = sys.argv[2] #if len(sys.argv) >= 3 else 'csv'
        df = scrape_slido(url, output_option)
        if output_option == 'table':
            df.to_string('output.txt')
        elif output_option == 'json':
            df.to_json('output.json', orient='records')
        elif output_option == 'csv':
            df.to_csv('output.csv', index=False)