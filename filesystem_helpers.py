import os

def create_empty_file(path):
  with open(path, 'a'):
    os.utime(path, None)

def create_folder(folder):
  # Create the folder if it doesn't exist
  if not os.path.exists(folder):
      os.makedirs(folder)
