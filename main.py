from get_readme_file import get_readme_file
from for_each_csv_item import for_each_csv_item
import time

request_count = 1

def handle_csv_row(user_name, repo_name):
    global request_count

    print "Attempt #" + str(request_count)

    get_readme_file(user_name, repo_name)
    time.sleep(2)
    request_count+= 1

if __name__ == '__main__':
    for_each_csv_item(handle_csv_row)
