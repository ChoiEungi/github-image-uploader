from sys import argv
from urllib import parse


test_string = "스크린샷 2022-02-19 오후 9.03.13.png 스ㅎ크린샷 2022-02-19 오후 9.03.13.png".split()
# print(test_string)

def file_paht_parser(input_stirng):
    result = []
    path = ""
    for string in input_stirng:

        # if find extension like .png, .jpg
        if(check_extension(string)):

            if is_empty_string(path):
                file = string
            else:
                file = path + " " + string
            result.append(parse.quote(file))
            path = ""
            continue

        # if path have space
        if not is_empty_string(path):
            path = path + " " + string
            continue

        # if inital string
        path = string

    return result


def check_extension(to_check):
    file_name_extension = [".png", ".jpg"]
    for extension in file_name_extension:
        if extension in to_check:
            return True
    return False


def is_empty_string(string):
    if string == "":
        return True
    return False


if __name__ == "__main__":

    argv.pop(0) # except this file

    for file in file_paht_parser(argv):
        print(file, end=" ")


