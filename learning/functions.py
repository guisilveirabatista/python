import random

def roll_dice(num):
    return random.randint(1, num)

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]