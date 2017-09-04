import urllib2
from get_logger import logger
from filesystem_helpers import create_folder
from get_url_content import get_url_content
from get_content_first_url import get_content_first_url
from config import config
import os
import csv

# The CSV file containing all the data
readmes_csv_file_name = config['FILE_NAME_README_CSV']
readmes_folder = config['FOLDER_NAME_MAIN']

readmes_csv_path = os.path.join(readmes_folder, readmes_csv_file_name)
create_folder(readmes_folder)

def get_readme_url(user_name, repo_name, file_name):
  url = "https://raw.githubusercontent.com/" + user_name + "/" + repo_name + "/master/" + file_name
  return url

def get_readme_file(user_name, repo_name):
  # Get a list of URLs at which the readme content *might* exist
  url_list = [
    get_readme_url(user_name, repo_name, "README.md"),
    get_readme_url(user_name, repo_name, "README.markdown"),
    get_readme_url(user_name, repo_name, "readme.md"),
  ]

  content = get_content_first_url(url_list, get_url_content)
  csvWriter = csv.writer(open(readmes_csv_path, 'ab'))

  if content != False:
      csvWriter.writerow([user_name, repo_name, content])
      message = "SUCCESS | user: " + user_name + " | repo: " + repo_name
      logger.info(message)

      return True

  else:
      message = "ERROR | user: " + user_name + " | repo: " + repo_name
      logger.error(message)
      csvWriter.writerow([user_name, repo_name, "NULL"])

      return False
