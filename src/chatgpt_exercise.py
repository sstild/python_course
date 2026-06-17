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

# Задача 2
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

number = input("Введите число:")
number = int(number)
if number < 0:
    print("это число отрицательное")
elif number == 0:
    print("это 0")
else:
    print("это число положительное")