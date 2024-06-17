# slido-scraping

This program is a web scraping tool that extracts questions from a Slido page. Slido is a question and answer platform used in conferences, meetings, and other events. This program can be useful for analyzing the questions asked in a specific event.

As far as I know, Slido does not provide APIs, which is why scraping technique is used, even though the site does not have well-defined IDs in the HTML.

<h1>HOW TO USE</h1>

1. Install the necessary dependencies:<br>
<code>pip install -r requirements.txt</code>

2. Clone the repository to your local computer:<br>
<code>git clone https://github.com/civitareale/slido-scraping</code>

3. Navigate to the project directory:<br>
<code>cd slido-scraping</code>

4. Run the program with the Python command. You will need to provide the URL of the Slido page as an argument:<br>
<code>python main.py --url https://app.sli.do/event/xyz123</code>

<i>Replace "https://app.sli.do/event/xyz123", without quotes, with the URL of the Slido page you want to query.
This option generates an output on the screen with the table (example):</i><br>
<table>
  <tr>
    <th>WHO</th>
    <th>LIKES</th>
    <th>QUESTIONS</th>
  </tr>
  <tr>
    <td>Anonymous</td>
    <td>4</td>
    <td>What is Python?</td>
  </tr>
</table>

<i>You can also enter other arguments specifying the output file name and a csv, json, or txt format.<br>
In this case, no output will be generated on the screen, only in the file, in the /output folder of this program's execution.<br>Example:</i><br>
<code>python main.py --url https://app.sli.do/event/xyz123 -f csv -o file_name</code>

<b>This program is for educational and learning purposes only. Be sure to respect Slido's terms of service when using this program.</b>