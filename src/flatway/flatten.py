from typing import List, Union, Dict
import sys

MAX_SIZE_INTEGER = sys.maxsize


def _flatten_into_list(target: List, source: List, source_length: int, start: int, depth: int):
    target_index = start
    source_index = 0
    while source_index < source_length:
        exists = bool(source[source_index])
        if exists:
            element = source[source_index]
            should_flatten = False
            if depth > 0:
                should_flatten = isinstance(element, list)
            if should_flatten:
                target_index = _flatten_into_list(target, element, len(element), target_index, depth - 1)
            else:
                if target_index >= MAX_SIZE_INTEGER:
                    raise Exception("index too large")
                else:
                    target.append(element)
                    target_index += 1
        source_index += 1

    return source_index


def _flatten_into_tuple(target: List, source: List, source_length: int, start: int, depth: int):
    target_index = start
    source_index = 0
    while source_index < source_length:
        exists = bool(source[source_index])
        if exists:
            element = source[source_index]
            casted = False
            if isinstance(element, tuple):
                element = list(element)
                casted = True
            should_flatten = False
            if depth > 0:
                should_flatten = isinstance(element, list)
            if should_flatten:
                target_index = _flatten_into_tuple(target, element, len(element), target_index, depth - 1)
            else:
                if target_index >= MAX_SIZE_INTEGER:
                    raise Exception("index too large")
                else:
                    if casted:
                        target.append(tuple(element))
                    else:
                        target.append(element)
                target_index += 1
        source_index += 1

    return target_index


def flatten(input_: Union[List, tuple], depth=1) -> Union[List, tuple]:
    """
      Returns a new list or tuple with all sub-child elements concatenated into it recursively up to the specified depth.

      Args:
          input_ (List | Tuple) The list or tuple that must flat.
          depth (int) The depth, default = 1

      Returns:
            List: A flatten list or tuple
    """
    is_tuple = isinstance(input_, tuple)
    if not isinstance(input_, (list, tuple)):
        raise Exception("The argument must have type list or tuple.")
    result = []
    if is_tuple:
        _flatten_into_tuple(result, list(input_), len(input_), 0, depth)
    else:
        _flatten_into_list(result, input_, len(input_), 0, depth)

    if is_tuple:
        return tuple(result)

    return result


def _flatten_into_dict(source: Dict, target, depth: int):
    for key, value in source.items():
        if isinstance(value , dict):
            should_flatten = False
            if depth > 0:
                should_flatten = True
            if should_flatten:
                _flatten_into_dict(value, target, depth - 1)
            else:
                target.update({key : value})
        else:
            target.update({key : value})
    return target


def flattenDict(input_: Dict, depth=1):
    """
    Args:
        input_: (dict)
        depth: (int) default 1

    Returns:
        Return a new dictionary with appending all sub dictionaries to the parent.
    """
    if not isinstance(input_, dict):
        raise Exception("The argument must have type dict.")
    result = {}
    _flatten_into_dict(input_, result, depth)
    return result
