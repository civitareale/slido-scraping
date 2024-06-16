# slido-scraping

Este programa é uma ferramenta de web scraping que extrai perguntas de uma página do Slido. O Slido é uma plataforma de perguntas e respostas usada em conferências, reuniões e outros eventos. Este programa pode ser útil para analisar as perguntas feitas em um evento específico.

Até onde apurei o Slido não fornece APIs, por esse motivo a técnica de scraping, mesmo o site não contendo IDs bem definidos no HTML.

<h1>COMO UTILZAR</h1>

1. Instale as dependências necessárias:<br>
<code>pip install -r requirements.txt</code>

2. Clone o repositório para o seu computador local:<br>
<code>git clone https://github.com/civitareale/slido-scraping</code>

3. Navegue até o diretório do projeto:<br>
<code>cd slido-scraping</code>

4. Execute o programa com o comando Python. Você precisará fornecer a URL da página do Slido como um argumento:<br>
<code>python main.py --url https://app.sli.do/event/xyz123</code>

<i>Substitua "https://app.sli.do/event/xyz123", sem aspas, pela URL da página do Slido que você deseja consultar.
Essa opção gera uma saída na tela com a tabela (exemplo):</i><br>
<table>
  <tr>
    <th>QUEM</th>
    <th>VOTOS</th>
    <th>PERGUNTA</th>
  </tr>
  <tr>
    <td>Anonymous</td>
    <td>4</td>
    <td>O que é Python?</td>
  </tr>
</table>

<i>Você pode também inserir outros argumentos especificando o nome do arquivo de saída e um formato csv, json ou txt.<br>
Nesse caso não será gerado saída na tela, somente no arquivo, na pasta /output de execução desse programa.<br>Exemplo:</i><br>
<code>python main.py --url https://app.sli.do/event/xyz123 -f csv -o file_name</code>

<b>Esse programa é apenas para fins educacionais e de aprendizado. Certifique-se de respeitar os termos de serviço do Slido ao usar este programa.</b>