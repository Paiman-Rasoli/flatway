# Flatway

Easily flat list, tuple or dictionary in your python project.

## How to use?

- install package using `pip install flatway`
- import package in your project.

```python
from flatway.flatten import flatten, flattenDict

myList = [1,2,3,[4,5,6,[7,8,9,[10,11]]]]
depth = 3 
# default to 1

flatList = flatten(myList , depth)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

myTuple = (1,2,3,(4,5,6,(7,8,9,(10,11))))
flatTuple = flatten(myTuple, depth)
# (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

person = {"name" : "Paiman", "age" : 12, "info" : {"loveFootball" : True}}
flatPerson = flattenDict(person)
# {"name": "Paiman", "age": 12 , "loveFootball": true}
```
### Run the tests
`pytest src/tests/test_flatten.py`