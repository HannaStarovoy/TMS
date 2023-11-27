# 1
def make_sentence(words:list=['This', 'is', 'a', 'sentence']):
    return ' '.join(words) + '.'
words = ['hi', 'we', 'are']
print(make_sentence(words))

# 2
def sum_of_squares(*args: int):
    if args:
        return sum(i ** 2 for i in args)
    else:
        return 0
print(sum_of_squares())

# # 3
def greet(name:str, language:str='en'):
    languages = {'en' : 'Hello',
                'fr' : 'Bonjor',
                'ru' : 'Привет'}
    if language =='ru':
        return languages.get('ru') + ', ' + name + '!'
    elif language == 'fr':
        return languages.get('fr') + ', ' + name + '!'
    else:
        return languages.get('en') + ', ' + name + '!'

print(greet(name="Anna", language='fr'))

# 4
def print_info(**kwargs):
    if kwargs:
        for key, values in kwargs.items():
            print(f'{key}:{values}')
    else:
        print("No info given.")
print_info(name="Alex", age=25, city="Amsterdam")


# # 5
def print_table(**kwargs):
    if kwargs:
        print(' | '.join("{:<6} {:<13} ".format('Key', 'Value')))
        for key, values in kwargs.items():
            print(' | '.join("{:<6} {:<13}".format(key,   values)))


    else:
        print("No data given.")

print_table(name="Bob", age=30, city="Amsterdam")

# 6
def calculate(*args, operation='+'):
    if args:
        if operation == '+':
            return sum(args)
        elif operation == '-':
            diff = args[0]
            for i in args[1:]:
                diff -= i
            return diff
        elif operation == '*':
            multip = 1
            for i in args:
                multip *= i
            return multip
        elif operation == '/':
            divide = args[0]
            for i in args[1:]:
                divide /= i
            return divide
    else:
        return 0
print(calculate(1, 2, 3, operation="*"))

# 7
def print_triangle(height: int = 5):
    for i in range(height):
        print(' ' * (height - 1 - i) + '*' * (1 + i * 2))
print_triangle(height=20)


#8
def create_post(heading:str, content:str, author:str, category='general' ):
    post = {'heading':heading,
            'content':content,
            'author':author,
            'category':category}
    return post

s = create_post(
    heading= 'Oppenheimer',
    content ='aboutmovie',
    author='Christopher Jonathan James Nolan',)
print(s)

#9
def create_product(name:str, price, category:str, rating =0 ) :
    product = {'name':name,
            'price':price,
            'category':category,
            'rating':rating}
    return product

s = create_product(
    name= 'shoes',
    price = 1500,
    category='classic',)
print(s)

# 10
def create_student(name:str, surname,patronymic,  group:str, **kwargs) :
    student = {
            'name':name,
            'surname':surname,
            'patronymic':patronymic,
            'group':group}
    for key, value in kwargs.items():
        student[key]=value
    return student

s = create_student(
    name= 'Kate',
    surname = 'Ivanova',
    patronymic='Sergeevna',
    group=1,
    date = '19.10.2023',
    averagescore = 8,
    semester = 4,
    phonenumber = 123456789,
    adress = 'Minsk')
print(s)
