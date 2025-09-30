import os

def create_dir_if_not_exist(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory created at {path}")
    else:
        print(f"Directory already exists at {path}")

# Example usage
create_dir_if_not_exist('/path/to/newdir')
