import re
import sys
import argparse
from scraping import scrape_slido

def valida_url(url):
    """
    Function to validate the URL provided.
    Parameters: url (str) - The URL to validate.
    Returns True if the URL is valid, otherwise False.
    A valid URL is a string that matches the pattern: https://app.sli.do/event/[a-zA-Z0-9]+
    """
    print("Validating URL provided...")
    
    if not re.match(r'^https://app.sli.do/event/[a-zA-Z0-9]+', url):
        print(' URL is invalid or does not match the pattern: https://app.sli.do/event/[a-zA-Z0-9]+')
        return False
    print('URL is valid!')
    return True

def main():
    """ 
    Function to parse the arguments and call the scraping function.
    The function receives the arguments from the command line and calls the scraping function.
    IT uses the argparse module to parse the arguments. It has a help message and error handling.
    Try --help or -h to see the help message.
    """
    
    parser = argparse.ArgumentParser(description="This program extracts questions from a Slido page using web scraping.")

    # Defining the arguments
    parser.add_argument('--url', type=str, required=True, help="Slido URL to be processed. This parameter is required.")
    parser.add_argument('--format', '-f', type=str, help="Output format desired: txt, json or csv. When omitted, the output will be on the screen.")
    parser.add_argument('--output-file', '-o', type=str, help="File name when the type is txt, json or csv.")

    args = parser.parse_args() # Parse the arguments
    
    # Arguments validation, in order to provide a better user experience
    if not args.url:
        print("Error: The '--url' argument is required and cannot be empty.")
        parser.print_help()
        exit(1)

    if args.output_file and not args.format:
        print("Error: The '--output-file' argument can only be used if '--format' is provided.")
        parser.print_help()
        exit(1)
    
    # Assigning the arguments to variables
    url = args.url
    format = args.format if args.format else "screen"
    output_file = args.output_file if args.output_file else "output"

    # Validating the format
    valid_formats = ['txt', 'json', 'csv']
    if format not in valid_formats:
        print(f"Error: Invalid format '{format}'. Valid formats are: {', '.join(valid_formats)}")
        parser.print_help()
        exit(1)

    # Displaying the arguments
    save_to_file = True if format != "screen" else False
    print(f"URL provided: {url}")
    if save_to_file:
        print(f"This file will be created: output/{output_file}.{format}")
    else:
        print(f"The output will be on the screen. stdout.")


    if not valida_url(url): sys.exit() # Validating the URL
    df = scrape_slido(url) # Running the scraping function with the URL provided
    
    # Displaying or saving the output, according to the format selected.
    if format == 'txt':
        df.to_string(f'output/{output_file}.{format}')
    elif format == 'json':
        df.to_json(f'output/{output_file}.{format}', orient='records')
    elif format == 'csv':
        df.to_csv(f'output/{output_file}.{format}', index=False)
    else:
        print(df)

    if save_to_file: print(f"File is created: output/{output_file}.{format}")
    
    print("End of the program.")