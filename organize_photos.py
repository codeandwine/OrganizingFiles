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


def making_folders(files, place_names):
    for place in place_names:
        os.mkdir(place, 0o755)
    move_files(files, place_names)


def move_files(files, place_names):
    for photo in files:
        for place in place_names:
            if place in photo:
                os.rename('Photos/'+photo, place + '/' + photo)


def organize_photos():
    getting_files()


if __name__ == '__main__':
    organize_photos()
