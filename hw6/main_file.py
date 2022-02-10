# import lib
#
# lib.foo()

# 2.Модифицируем ДЗ 2. Напишите с помощью функций!. Помните о Single Responsibility! Попросить ввести свой возраст
# (можно использовать константу или input()). Пользователь ввел значение возраста [year number] а на место [year string]
# нужно поставить правильный падеж существительного "год", который зависит от значения [year number].
# если пользователь ввел непонятные данные (ничего не ввел, ввел не число, неактуальный возраст и тд.) - вывести “не понимаю”
# если пользователю меньше 7 - вывести “Тебе [year number] [year string], где твои мама и папа?”
# если пользователю меньше 18 - вывести “Тебе [year number] [year string], а мы не продаем сигареты несовершеннолетним”
# если пользователю больше 65 - вывести “Вам уже [year number] [year string], вы в зоне риска”!
# в любом другом случае - вывести “Оденьте маску, вам же [year number] [year string]!”

a = int(input('Введите свой возраст: '))

b = a % 10
year_str = 0

def year():

    if b == 0:
        year_str = 'лет'
    elif b == 1:
        year_str = 'год'
    elif b >= 2 and b <= 4:
        year_str = 'года'
    elif b > 4:
        year_str = 'лет'
    else:
        pass


    if a <= 0:
        print('Не понимаю')
    elif a > 100:
        print('Не понимаю')
    elif a < 7:
        print('Тебе', a, year_str, 'где твои мама и папа?')
    elif a < 18:
        print('Тебе', a, year_str, ', а мы не продаем сигареты несовершеннолетним!')
    elif 65 < a < 101:
        print('Вам же', a, year_str, 'вы в зоне риска!')
    else:
        print('Оденьте маску, вам же', a, year_str)

year()