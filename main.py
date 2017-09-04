from get_readme_file import get_readme_file
from for_each_csv_item import for_each_csv_item
import time

request_count = 0
total_success = 0.0
total_failure = 0.0

def handle_csv_row(user_name, repo_name):
    global request_count
    global total_success
    global total_failure

    if get_readme_file(user_name, repo_name):
        total_success+= 1.0
    else:
        total_failure+= 1.0

    request_count+= 1
    print "Request #" + str(request_count) + ". Success rate: " + str((total_success / request_count) * 100) + "%"

if __name__ == '__main__':
    for_each_csv_item(handle_csv_row)
