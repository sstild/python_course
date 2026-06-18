# А. Типы данных

# Задача 1

# Создай переменные следующих типов:
# строка с твоим именем;
# целое число с твоим возрастом;
# дробное число с ростом;
# логическое значение (True или False).
# Выведи значение и тип каждой переменной.

name = "Ilya"
age = 40
height = 167.9
married = True
print("Переменная name =", name, "её тип:", type(name).__name__)
print("Переменная age =", age, "её тип:", type(age).__name__)
print("Переменная height =", height, "её тип:", type(height).__name__)
print("Переменная married =", married, "её тип:", type(married).__name__)
print()

# Задача 2

# Есть список:
# data = ["Ivan", 35, True, None, 3.14]
# Выведи для каждого элемента:

# Элемент 0: Ivan, тип str
# Элемент 1: 35, тип int
# ...

data = ["Ivan", 35, True, None, 3.14]
for index, item in enumerate(data):
    print(f"Элемент {index}: {item}, тип {type(item).__name__} ")
print()

# Задача 3

# Создай переменную:
# value = "123"
# Преобразуй её:
# в int;
# в float.
# Выведи результат и тип.

value = "123"
value = int(value)
print("Значение переменной value = ", value, "\b. тип переменной:", type(value).__name__, "\b.")
print()
value = float(value)
print("Значение переменной value = ", value, "\b. тип переменной:", type(value).__name__, "\b.")
print()

# Задача 4

# Проверь, какие результаты вернут выражения:
# bool("") false
# bool("abc") true
# bool(0) false
# bool(1) true
# bool([]) false
# bool([1]) true
# bool(None) false
# Сначала попробуй угадать ответ, потом проверь кодом.
print(bool(""))
print(bool("abc"))
print(bool(0))
print(bool(1))
print(bool([]))
print(bool([1]))
print(bool(None))
print()

# Б. Ветвления (if/elif/else)

# Задача 1

# Пользователь вводит число.
# Выведи: Положительное или Отрицательное или Ноль

number = input("Введите число:")
print(type(number))
if type(number) == str:
    number = int(number)
if number < 0:
    print("это число отрицательное")
elif number == 0:
    print("это 0")
else:
    print("это число положительное")
print()

# Задача 2

# Пользователь вводит возраст.
# Если: меньше 18 → "Несовершеннолетний"?
# # от 18 до 65 → "Взрослый"
# больше 65 → "Пенсионер"

number = input("Введите возраст:")
number = int(number)
if 0 < number < 18:
    print("Несовершеннолетний")
elif 18 < number < 65:
    print("Взрослый")
elif number > 65:
    print("Пенсионер")
else:
    print("Возраст не может быть отрицательным)")
print()

# Задача 3

# Есть переменная: enabled = True. "Если она истинна", вывести: "Учетная запись активна", иначе: "Учетная запись заблокирована"
# переделал, чтобы значение переменной завиесло от ввода данных, если что-то ввести с клавиатуры будет True, если просто нажать Enter будет False

enabled = bool(input("Если что-то ввести, то будет True, если не вводить жмакнуть Enter, будет False: "))
if enabled:
    print(enabled, "\b: что-то ввёл")
else:
    print(enabled, "\b: просто жмакнул Enter")
print()

# Задача 4

# Пользователь вводит пароль.
# Если пароль равен:"admin123", вывести: "Доступ разрешен", иначе: "Неверный пароль".

password = input("введите пароль: ")
if password == "admin123":
    print("Доступ разрешён")
else:
    print("Неверный пароль")
print()

# В. Циклы

# Задача 1

# Вывести числа от 1 до 10 через цикл for.

print("Числа от 1 до 10:")
for i in range(10):
    print(i + 1)
print()

# Задача 2

# Вывести только четные числа от 1 до 20.

print("Чётные числа от 1 до 20:")
for n in range(1,21):
    if n % 2 == 0:
        print(n)
print()

# Задача 3
# Посчитать сумму чисел:
# 1 + 2 + 3 + ... + 100
# через цикл.

summ = 0
for i in range(1, 101):
    summ += i
print("Сумма чисел от 1 до 100 =", summ)
print()


# Задача 4

# Есть список: users = ["ivan", "petr", "alex"]
# Вывести:
# Пользователь: ivan
# Пользователь: petr
# Пользователь: alex

users = ["Ivan", "Petr", "Alex"]
for index, item in enumerate(users):
    print(f"Пользователь: {item}")

# Задача 5

# Используя enumerate(), вывести:
# 0: ivan
# 1: petr
# 2: alex
users = ["Ivan", "Petr", "Alex"]
for index, item in enumerate(users):
    print(f"{index}: {item}")
print()

# optional
for pair in enumerate(users):
    print(pair)
print()

# Г. Коллекции

# List

# Задача 1

# Создай список из пяти серверов: # servers = [...]
# Выведи:
# первый элемент;
# последний элемент;
# длину списка.

servers = ["server1","server2","server3","server4","server5"]
print("Первый элемент", servers[0])
print("Последний элемент", servers[-1])
print("Длина списка", len(servers))
print()

# Задача 2

# Добавь новый сервер через append().
# Выведи список.
servers.append("server6")
print(servers)

# Задача 3

# Замени второй элемент списка на новый.

servers[1] = "serverN"
print(servers)

# Tuple

# Задача 4

# Создай кортеж:
# server = ("dc01", "10.0.10.10", 443)
# Выведи все элементы по индексам.

server = ("dc01", "10.0.10.10", 443)
for index,item in enumerate(server):
    print(f"{index}: {item}")
type(server)
type((1))
tuple = (1,)
print(tuple)
print(type(tuple))

# Задача 6
#
# Есть список:
# # groups = [
#     "Domain Users",
#     "Domain Users",
#     "Domain Admins",
#     "Backup Operators",
#     "Domain Admins"
# ]
# # Получи множество уникальных групп.

groups = [
    "Domain Users",
    "Domain Users",
    "Domain Admins",
    "Backup Operators",
    "Domain Admins"
]

unique_groups = set(groups)
unique_groups2 = list(set(groups))# преобразование списка в множество (set), и обратно в список, при этом дубли удаляются
print("set:", unique_groups)
print("list:", unique_groups2)
print()

# Задача 7
#
# Для множеств:
# a = {"ivan", "petr", "alex"}
# b = {"alex", "sergey"}
# Найди:
# объединение;
# пересечение;
# разность;
# симметрическую разность.
a = {"ivan", "petr", "alex"}
b = {"alex", "sergey"}
print(a)
print(b)
print("Объединение(|):", a | b)
print("Пересечение(&):", a & b)
print("Разность(-):", a - b)
print("Симметрическая Разность(^):", a ^ b)
print()

# Dict (словарь)
#
# Задача 8
#  Создай словарь пользователя:
# # user = {
#     "name": "Ivan",
#     "age": 35,
#     "city": "Karlsruhe"
# }
# # Выведи: имя, возраст.


user = {
     "name": "Ivan",
     "age": 35,
     "city": "Novgorod"
 }
print(user["name"],"\b,", user["age"])
print(f"{user['name']}, {user['age']}")

