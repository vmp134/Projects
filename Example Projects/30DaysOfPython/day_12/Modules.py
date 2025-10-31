from random import random, randint
import math
import string

#1
def random_user_id():
    ret = ""
    select = string.ascii_letters + string.digits
    for i in range(5):
        ret += select[randint(0, len(select)-1)]
    print(ret)

#2
def user_id_gen_by_user():
    a = int(input())
    b = int(input())
    select = string.ascii_letters + string.digits
    for i in range(a):
        ret = ""
        for j in range(b):
            ret += select[randint(0, len(select)-1)]
        print(ret)

#3
def rgb_color_gen():
    return (randint(0,255),randint(0,255),randint(0,255))

#1
def list_of_hexa_colors(num):
    ret = []
    select = "abcdef1234567890"
    for i in range(num):
        hexdec = ""
        for j in range(6):
            hexdec += select[0, randint(0, len(select)-1)]
        ret.append(hexdec)
    return ret

#2
def list_of_rgb_colors(num):
    ret = []
    for i in range(num):
        ret.append((randint(0,255),randint(0,255),randint(0,255)))
    return ret

#3
def generate_colors(name, num):
    ret = []
    if name == 'hexa':
        select = "abcdef1234567890"
        for i in range(num):
            hexdec = ""
            for j in range(6):
                hexdec += select[0, randint(0, len(select)-1)]
            ret.append(hexdec)
    elif name == 'rgb':
        for i in range(num):
            ret.append((randint(0,255),randint(0,255),randint(0,255)))
    else: 
        print("Error: Name")
    return ret

#1
def shuffle_list(lst):
    ret = []
    for i in range(len(lst)):
        ret.append(lst.pop(randint(0, len(lst)-1)))
    return ret


#2
def randomArray():
    use = [0,1,2,3,4,5,6,7,8,9]
    ret = []
    for i in range(7):
        ret.append(use.pop(randint(0, len(use)-1)))
    return ret