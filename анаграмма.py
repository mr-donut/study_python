# -*- coding: utf-8 -*-


def main():
    with open('гениальное решение.txt', 'r', ) as f:
        content = f.read().lower().splitlines()

    my_list = []
    for text_line in content:
        my_list.extend(text_line.split(' '))

    word = sorted(input('? '))

    for i in my_list:
        if word == sorted(i):
            print(i)


if __name__ == "__main__":
    main()