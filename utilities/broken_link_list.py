import requests
from bs4 import BeautifulSoup
from utilities.custom_logger import custom_logging as cl
import logging


def brokenLinkCheck(driver):
    log = cl(logging.DEBUG)
    sitemap = driver.current_url
    log.info("Current Link checking for Broken Links : "+sitemap)

    r = requests.get(sitemap)
    html = r.content

    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a')
    urls = [link.get('href') for link in links
            if link.get('href') and link.get('href')[0:4] == 'http']

    results = []
    for i, url in enumerate(urls,1):
        try:
            r = requests.get(url)
            report = str(r.status_code)
            if r.history:
                history_status_codes = [str(h.status_code) for h in r.history]
                report += ' [HISTORY: ' + ', '.join(history_status_codes) + ']'
                result = (r.status_code, r.history, url, 'No error. Redirect to ' + r.url)
            elif r.status_code == 200:
                result = (r.status_code, r.history, url, 'No error. No redirect.')
            else:
                result = (r.status_code, r.history, url, 'Error?')
        except Exception as e:
            result = (0, [], url, e)

        results.append(result)

    # Sort by status and then by history length
    results.sort(key=lambda result: (result[0], len(result[1])))

    log.error('Broken Links : ')
    for result in results:
        if result[0] != 200:
            log.error("Code : {} && Link : {}".format(result[0], '-', result[2]))