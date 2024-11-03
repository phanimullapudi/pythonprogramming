import requests
import time
import logging

# Set up logging
logging.basicConfig(filename='api_health_check.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def check_api_health(url):
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                logging.info(f'API is healthy. Status code: {response.status_code}')
            else:
                logging.error(f'API returned a non-200 status code. Status code: {response.status_code}')
        except requests.exceptions.RequestException as e:
            logging.error(f'Failed to reach the API. Exception: {e}')
        
        # Wait for 10 seconds before the next check
        time.sleep(10)

if __name__ == '__main__':
    api_url = 'https://httpbin.org/get'
    check_api_health(api_url)
