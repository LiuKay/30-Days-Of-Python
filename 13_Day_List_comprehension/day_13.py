import inspect

lan = 'Python'
lst = list(lan)
print(type(lst))
print(lst)

lst = [i for i in lan if i.isupper()]
print(type(lst))
print(lst)

numbers = [i for i in range(11)]
print(numbers)

numbers = [i * i for i in range(11)]
print(numbers)

numbers = [(i * i * i) for i in range(11)]
print(numbers)

lst = [
    {
        'name': 'kai',
        'age': 18,
    },
    {
        'name': 'jack',
        'age': 12
    },
    {
        'name': 'tom',
        'age': 20
    }
]
ll = [p['name'] for p in lst if p['age'] < 20]
print(ll)

re = (lambda a, b: a + b)(2, 3)
print(re)


# lambda inside another function

def power(x):
    return lambda n: x ** n


print(type(power))
print(inspect.signature(power))

re = power(2)(3)
print(re)
