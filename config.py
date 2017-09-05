from time import gmtime, strftime
from datetime import datetime

today = datetime.today()
result_file_name = "result-" + today.strftime("%a-%m-%d-%I%M%p") + ".csv"

config = {
    "FOLDER_NAME_MAIN": "readme-data",
    "FILE_NAME_README_CSV": result_file_name,
    "PATH_CSV_SOURCE": "readme-data/user_projects_1.csv"
}
