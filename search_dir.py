import argparse
import os

count = 0


def get_directory():
    parser = argparse.ArgumentParser(description='Count the number of JSON files in a directory')
    parser.add_argument('path', help='Path to target directory')
    args = parser.parse_args()
    return args.path


target_dir = get_directory()


if not os.path.isdir(target_dir):
    print('Directory doesn\'t exist')
    exit(1)
else:
    for file in os.listdir(target_dir):
        if file.endswith(".json"):
            count = count + 1
print("Number of JSON files: " + str(count))
