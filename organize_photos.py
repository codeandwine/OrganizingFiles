import time
import os


def getting_files():
    files = os.listdir('Photos')
    photo_names = []

    for photo in files:
        photo_names.append(photo)
    extract_places(files, photo_names)


def extract_places(files, photos):
    place_names = []

    for photo in photos:
        temp = ''
        for i in photo:
            if (i.isalpha()):
                temp += i
            if i == '.':
                break
        if temp not in place_names:
            place_names.append(temp)
    making_folders(files, place_names)




getting_files()
