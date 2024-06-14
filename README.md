# slido-scraping

Este programa é uma ferramenta de web scraping que extrai perguntas de uma página do Slido. O Slido é uma plataforma de perguntas e respostas usada em conferências, reuniões e outros eventos. Este programa pode ser útil para analisar as perguntas feitas em um evento específico.

Até onde apurei o Slido não fornece APIs, por esse motivo a técnica de scraping, mesmo o site não contendo IDs bem definidos no HTML.

<h1>COMO UTILZAR</h1>

1. Instale as dependências necessárias:<br>
<code>pip install -r requirements.txt</code>

2. Clone o repositório para o seu computador local:<br>
<code>git clone https://github.com/civitareale/slido-scraping</code>

3. Navegue até o diretório do projeto:<br>
<code>cd slido-scraping<c/ode>

4. Execute o programa com o comando Python. Você precisará fornecer a URL da página do Slido como um argumento:<br>
<code>python main.py https://app.sli.do/event/xyz123</code>

Substitua "https://app.sli.do/event/xyz123", sem aspas, pela URL da página do Slido que você deseja consultar.
Essa opção imprimirá na tela uma tabela com Nome de quem fez a pergunta, Quantidade de Likes e Perunta:
|    QUEM    | VOTOS  |         PERGUNTA                 |
| Anonymous  |   4    | O que é Python?                  |

Você pode também inserir um segundo argumento especificando a criação de um arquivo no formato csv, json ou txt.
Nesse caso será gerado da pasta atual um arquivo de nome "output" com a respectiva extensão.
python main.py https://app.sli.do/event/xyz123 csv

Esse programa é apenas para fins educacionais e de aprendizado. Certifique-se de respeitar os termos de serviço do Slido ao usar este programa.