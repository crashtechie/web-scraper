import os
from requests import get
from datetime import datetime, timezone
from bs4 import BeautifulSoup


def main():
    print('Welcome to Web Scraper!')
    #input_url = input('Enter the URL: ')
    input_url = 'https://www.google'
    html = get_html(input_url)
    print(html)
    print('\n\n', 'Done!')
    
def get_html(url):
    try:
        if url.startswith('http'):
            response = get(url)
            html = response.text
        else:  
            with open(url, 'r') as file_html:
                html = file_html.read()
        
        soup = BeautifulSoup(html, 'html.parser')
        return soup.prettify()
    except Exception as e:
        error_log(e)
        exit(1)
        
def error_log(error):
    try:
        utc_date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
        log_filename = f'error-{utc_date}.log'
        utc_datetime = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        if not os.path.exists('logs'):
            os.mkdir('logs')
        if not os.path.exists(f'logs/{log_filename}'):
            with open(f'logs/{log_filename}', 'w') as file_error:
                file_error.write(f'{utc_datetime} - Error: {error}\n')
        else:
            with open(f'logs/{log_filename}', 'a') as file_error:
                file_error.write(f'{utc_datetime} - Error: {error}\n')
    except Exception as e:
        print('Error: ', e)
        exit(1)

if __name__ == '__main__':
    main()