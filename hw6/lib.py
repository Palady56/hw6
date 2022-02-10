# В отдельном файле (пусть будет lib.py) написать функцию, которая требует от пользователя ответить да или нет (Y/N)
# и возвращает True/False в зависимости от того, что он ввел. В основном файле (пусть будет main_file.py) попросить
# пользователя ввести с клавиатуры строку и вывести ее на экран. Используя импортированную из lib.py функцию спросить
# у пользователя, хочет ли он повторить операцию (Y/N). Повторять пока пользователь отвечает Y и прекратить когда
# пользователь скажет N.

def foo():
    while True:
        print('Are u sure? (Y/N): ')
        res = input()

        if res == 'Y' or res == 'y':
             print("Positive answer: {}".format(res))
        elif res == 'N' or res == 'n':
            print("Negative answer: {}".format(res))
            break
        else:
            print("Wrong value: {}".format(res))
    return res
