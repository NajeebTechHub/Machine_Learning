# map is a higher order function(HOF) cause it reciev function as input

# e.g1
print(list(map(lambda x:x**3,[1,3,4,5])))

# e.g2
l = [1,2,3,4,5,6,7]
print(list(map(lambda x:'even' if x%2 == 0 else 'odd', l)))

# e.g3
users = [{
    'name' : 'najeeb',
    'age' : 23,
    'gender' : 'male'
    },
    {
        'name':'haseeb',
        'age':21,
        'gender':'male'
    },
    {
        'name':'anees',
        'age':19,
        'gender':'male'
    }

]
print(list(map(lambda users:users['name'],users)))