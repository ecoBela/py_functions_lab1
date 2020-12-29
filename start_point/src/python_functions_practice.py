def return_10():
    return 10

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 /num2

def length_of_string(teststring):
    return len(teststring)

def join_string(string1, string2):
    return string1 + string2

def add_string_as_number(num1, num2):
    return int(num1)+int(num2)

def number_to_full_month_name(index):
    month = ['none', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return month[index]


def number_to_short_month_name(index):
    months = ['none', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    short_month_name = []
    for month in months:
        split_month = month[0:3]
        short_month_name.append(split_month)
    # print(short_month_name[index])
    return short_month_name[index]

def volume_of_cube(num):
    return num **3


# def test_reverse_string(string):
#       return string[::-1]
# mytxtbackwards = test_reverse_string("God Help us!")
# print(mytxtbackwards)


