# Flatway

Easily flat the lists and tuples in your python project.

## How to use?

- install package using `pip install flatway`
- import package in your project.

```python
from flatway.flatten import flatten

myList = [1,2,3,[4,5,6,[7,8,9,[10,11]]]]
depth = 3 # default to 1

flatList = flatten(myList , depth)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

myTuple = (1,2,3,(4,5,6,(7,8,9,(10,11))))
flatTuple = flatten(myTuple, depth)
# (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

deepOne = flatten(myList)
# [1, 2, 3, 4, 5, 6, [7, 8, 9, [10, 11]]]

```
