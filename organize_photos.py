import time
import os


def getting_files():
    files = os.listdir('Photos')
    photo_names = []

    for photo in files:
        photo_names.append(photo)
        print(photo)


getting_files()
