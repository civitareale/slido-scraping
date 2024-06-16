import re
import sys
import argparse
from scraping import scrape_slido

def valida_url(url):
    print("Validando a URL fornecida...")
    # Valida se a URL é válida
    if not re.match(r'^https://app.sli.do/event/[a-zA-Z0-9]+', url):
        print('URL inválida. Por favor, insira uma URL válida do Slido.')
        return False
    print('URL válida com sucesso!')
    return True

def main():
    parser = argparse.ArgumentParser(description="Esse programa processa extrai perguntas de uma página do Slido, através de web scraping.")
    
    # Define os argumentos
    parser.add_argument('--url', type=str, required=True, help="URL do Slido a ser processada. Esse parâmetro é obrigatório.")
    parser.add_argument('--format', '-f', type=str, help="O formato de saída desejado: txt, json ou csv. Quando omitido a saída será na tela.")
    parser.add_argument('--output-file', '-o', type=str, help="Nome do arquivo quando o tipo for txt, json ou csv.")

    # Parseia os argumentos
    args = parser.parse_args()
    
    # Valida se os argumentos possuem valor
    if not args.url:
        print("Erro: O argumento '--url' é obrigatório e não pode estar vazio.")
        parser.print_help()
        exit(1)

    if args.output_file and not args.format:
        print("Erro: O argumento '--output-file' só pode ser usado se '--format' for fornecido.")
        parser.print_help()
        exit(1)
    
    # Acessa os valores dos argumentos
    url = args.url
    format = args.format if args.format else "screen"
    output_file = args.output_file if args.output_file else "output"

    # Exibe os valores dos argumentos
    save_to_file = True if format != "screen" else False
    print(f"URL fornecida: {url}")
    if save_to_file:
        print(f"Arquivo de saída: output/{output_file}.{format}")
    else:
        print(f"A saída será na tela. stdout.")


    # Valida se a URL é válida
    if not valida_url(url): sys.exit()
    # Executa o scraping na URL fornecida e retorna um DataFrame com as perguntas, autores e votos
    df = scrape_slido(url)
    
    # Exibe o DataFrame
    if format == 'txt':
        df.to_string(f'output/{output_file}.{format}')
    elif format == 'json':
        df.to_json(f'output/{output_file}.{format}', orient='records')
    elif format == 'csv':
        df.to_csv(f'output/{output_file}.{format}', index=False)
    else:
        print(df)

    if save_to_file: print(f"Arquivo criado: output/{output_file}.{format}")
    print("Fim do programa.")