import os

file = os.path.join(os.getcwd(), 'file_numbers.txt')
open(file, mode='w', encoding='utf-8')


def my_function(file_path):
    number = input('Введите число: ')
    if number.isdigit():
        if int(number) == 0:
            with open(file_path, mode='a', encoding='utf-8') as file_txt:
                number_ = f'{number}\n'
                file_txt.writelines(number_)

        elif number != 0:
            with open(file_path, mode='a', encoding='utf-8') as file_txt:
                number_ = f'{number}\n'
                file_txt.writelines(number_)
            my_function(file_path)
    else:
        with open(file_path, mode='a', encoding='utf-8') as file_txt:
            number_ = f'{0}\n'
            file_txt.writelines(number_)
        with open(file_path, mode='r', encoding='utf-8') as f:
            count = 0
            for i in f.readlines():
                count = count + int(i)
            print(count)











my_function(file)