import os
import logging
from config import config
from time import gmtime, strftime
from filesystem_helpers import create_folder, create_empty_file

def get_log_file_name(log_folder_path):
  file_name = "result-" + strftime("%Y-%m-%d_%H.%M.%S", gmtime()) + ".log"
  return os.path.join(log_folder_path, file_name)

def get_logger(log_file_path):
  # Helps us log the result of the script
  logger = logging.getLogger(__name__)
  logger.setLevel(logging.INFO)

  handler = logging.FileHandler(log_file_path)
  handler.setLevel(logging.INFO)

  # create a logging format
  formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
  handler.setFormatter(formatter)

  # add the handlers to the logger
  logger.addHandler(handler)

  return logger

# Define file paths and set up necessary files / folders
log_folder_path = os.path.join(config["FOLDER_NAME_MAIN"], "log/")
log_file_path = get_log_file_name(log_folder_path)

create_folder(log_folder_path)
create_empty_file(log_file_path)

logger = get_logger(log_file_path)
