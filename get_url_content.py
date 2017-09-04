import urllib2
from get_logger import logger

def get_url_content(url):
    try:
        response = urllib2.urlopen(url)
        content = response.read()
        return content
    except Exception as e:
        logger.error(e)

    return False
