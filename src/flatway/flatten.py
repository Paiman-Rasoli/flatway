from typing import List, Union, Tuple
import unittest
import math
import sys

MAX_SIZE_INTEGER = sys.maxsize


def _flattenIntoList(target: List , source: List, sourceLength: int, start: int, depth: int):
      targetIndex = start
      sourceIndex = 0
      while(sourceIndex < sourceLength):
            exists = bool(source[sourceIndex])
            if exists:
                  element = source[sourceIndex]
                  shouldFlatten = False
                  if depth > 0:
                        shouldFlatten = isinstance(element, list)
                  if shouldFlatten:
                        elementLength = len(element)
                        targetIndex = _flattenIntoList(target, element, elementLength, targetIndex, depth - 1)
                  else:
                        if targetIndex >= MAX_SIZE_INTEGER:
                              raise Exception("index too large")
                        else:
                              target.append(element)
                              targetIndex += 1
            sourceIndex += 1

      return targetIndex


def _flattenIntoTuple(target: List , source: List, sourceLength: int, start: int, depth: int):
      targetIndex = start
      sourceIndex = 0
      while(sourceIndex < sourceLength):
            exists = bool(source[sourceIndex])
            if exists:
                  element = source[sourceIndex]
                  casted = False
                  if isinstance(element, tuple):
                        element = list(element)
                        casted = True
                  shouldFlatten = False
                  if depth > 0:
                        shouldFlatten = isinstance(element, list)
                  if shouldFlatten:
                        elementLength = len(element)
                        targetIndex = _flattenIntoTuple(target, element, elementLength, targetIndex, depth - 1)
                  else:
                        if targetIndex >= MAX_SIZE_INTEGER:
                              raise Exception("index too large")
                        else:
                              if casted:
                                    target.append(tuple(element))
                                    casted = False
                              else:
                                    target.append(element)
                              targetIndex += 1
                              casted = False
            sourceIndex += 1

      return targetIndex


def flatten(input: Union[List, tuple], depth = 1) -> Union[List, tuple]:
      """
        Returns a new list or tuple with all sub-child elements concatenated into it recursively up to the specified depth.

        Args:
            input (List | Tuple) The list or tuple that must flat.
            depth (int) The depth, default = 1
      
        Returns:
              List: A flatten list or tuple
      """
      isTuple = isinstance(input, tuple)
      if not isinstance(input, (list, tuple)):
            raise Exception("The argument must have type list or tuple.")
      sourceLength = len(input)
      temp = []
      if isTuple:
            _flattenIntoTuple(temp, list(input), sourceLength, 0, depth)
      else:
            _flattenIntoList(temp, input, sourceLength, 0, depth)

      if isTuple:
            return tuple(temp)

      return temp


class TestFlatten(unittest.TestCase):

      def test_flatten_of_a_list(self):
            mockList = [1,2,3,4,5,[6,7,8,9]]
            expect = [1,2,3,4,5,6,7,8,9]
            flattenResult = flatten(mockList)

            self.assertListEqual(flattenResult , expect)
            self.assertEqual(flattenResult is expect, False)

      def test_flatten_of_a_tuple(self):
            mockTuple = (1,2,3,(4,5))
            expect = (1,2,3,4,5)
            flattenResult = flatten(mockTuple)

            self.assertTupleEqual(flattenResult , expect)

      def test_flatten_of_list_with_deep(self):
            mockList = [1,2,3,[4,5,6,[7,8,[9,10]]]]
            expect = list(range(1,11))
            flattenResult = flatten(mockList, 3)

            self.assertListEqual(flattenResult , expect)
            
      def test_flatten_of_tuple_with_deep(self):
            mockTuple = (1,2,3,(4,5,6,(7,8,(9,10))))
            expect = tuple(range(1,11))
            flattenResult = flatten(mockTuple , 3)
            
            self.assertTupleEqual(flattenResult , expect)



if __name__ == "__main__":
      unittest.main()