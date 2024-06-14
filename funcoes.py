import re

def valida_url(url):
    # Valida se a URL é válida
    if not re.match(r'^https://app.sli.do/event/[a-zA-Z0-9]+', url):
        print('URL inválida. Por favor, insira uma URL válida do Slido.')
        return False
    return True


