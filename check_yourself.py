'''
1) Создайте класс Auto в нем реализуйте метод ride который выводит
сообщение 'Riding on a ground'.
Создайте класс Boat реализуйте метод swim, который выводит 'Floating on
water'.
Создайте класс Amphibian который наследуется от класса Auto и Boat.
Создайте от него объект obj и вызовите все методы.
Ввод:
obj = Amphibian()
obj.ride()
obj.swim()
Вывод:
Riding on a ground
Floating on water
'''
class Auto:
    def ride(self):
        print('Riding on a ground')

class Boat:
    def swim(self):
        print('Floating on water')
class Amphibian(Auto, Boat):
    pass

obj = Amphibian()
obj.ride()
obj.swim()

'''
2)Создайте класс ContactList, который должен наследоваться от встроенного
класса list.
В вашем классе должен быть реализован метод search_by_name, который
должен принимать имя и возвращать список всех совпадений.
Создайте экземпляр класса в переменной all_contacts и передайте список
ваших контактов.
Примерный ввод:
all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan'])
print(all_contacts.search_by_name('Olya'))
Метод search_by_name возвращает все строки содержащие подстроку
"Olya":
['Ivan Olya', 'Olya Ivan']
'''
class ContactList(list):
    def __init__(self, names):
        self.names = names

    def search_by_name(self, name):
        list1 = []
        for i in self.names:
            if i.startswith(name) or i.endswith(name):
                list1.append(i)
        return list1
        

all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan'])
print(all_contacts.search_by_name('Olya'))

'''
3) Напишите класс Person, который будет хранить информацию о
пользователе. У объекта будут следующие атрибуты экземпляра класса:
имя(name), фамилия(last_name), возраст(age), почта (email).
При инициализации объекта, передавать аргументы классу не нужно, все его
атрибуты по умолчанию будут равны None и также все они будут
приватными.
Поэтому реализуйте для каждого атрибута методы доступа get и set не
используя декораторы property и setter. У вас будут такие методы: get_name,
set_name, get_last_name, set_last_name, get_age, set_age, get_email,
set_email.
Создайте экземпляр john класса Person выедите все его атрибуты, затем
измените их как показано ниже и после снова выведите на экран.

Пример:
john = Person()
print(john.get_name()) # None
print(john.get_last_name()) # None
print(john.get_age()) # None
print(john.get_email()) # None
john.set_name('John')
john.set_last_name('Snow')
john.set_age(30)
john.set_email('johnsnow@gmail.com')
print(john.get_name()) # John
print(john.get_last_name()) # Snow
print(john.get_age()) # 30
print(john.get_email()) # johnsnow@gmail.com'
'''

class Person:
    def __init__(self,name, last_name, age, email) -> None:
        self.__name = name
        self.__last_name = last_name
        self.__age = age
        self.__email = email

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    
    def get_last_name(self):
        return self.__last_name
    
    def set_last_name(self, last_name):
        self.__last_name = last_name


    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age


    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email


john = Person('Erlan', 'Jukeshovich', 26, 'john@gmail.com')
print(john.get_name()) # None
print(john.get_last_name()) # None
print(john.get_age()) # None
print(john.get_email()) # None
john.set_name('John')
john.set_last_name('Snow')
john.set_age(30)
john.set_email('johnsnow@gmail.com')
print(john.get_name()) # John
print(john.get_last_name()) # Snow
print(john.get_age()) # 30
print(john.get_email()) # johnsnow@gmail.com'
