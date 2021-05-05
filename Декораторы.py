import numpy as np
import time
import locale
from typing import Tuple

"task №1"
def duration(any_function):
    def inner_call(*args, **kwargs):
        start_time = time.perf_counter()
        result = any_function(*args, **kwargs)
        end_time = time.perf_counter()
        duration_in_seconds = end_time - start_time
        string_to_print = f'Duration of "{any_function.__name__}" was: {duration_in_seconds} sec'
        print(string_to_print)
        return result
    return inner_call

@duration
def sleep_function():
  time.sleep(5)
  message = "I am awake!"
  return message

# sleep_function()

"task №2,3"
def start_time_in_ru_locale(loc: str or Tuple[str]):
    def real_decorator(any_function):
        def inner_call(*args, **kwargs):
            current_locale = locale.getlocale()
            locale.setlocale(locale.LC_ALL, loc)
            result = any_function(*args, **kwargs)
            current_time = time.strftime("%a, %d %b %Y, %H:%M:%S")
            string_to_print = f' "{any_function.__name__}" was launched in {loc} localization: {current_time}'
            print(string_to_print)
            locale.setlocale(locale.LC_ALL, current_locale)
            return result
        return inner_call
    return real_decorator

@start_time_in_ru_locale('ru')
def sleep_function():
  time.sleep(5)
  message = "I am awake!"
  return message

# print(sleep_function())

"task №4"
def check_classes(checks: list):
  def real_decorator(any_function):
    def inner_call(*args, **kwargs):
      for arg in args:
        assert isinstance(arg, tuple(checks))
        # flag = False
        # for check in checks:
        #   if type(arg) == check:
        #     flag = True
        #   else:
        #     pass
        # assert flag == True, f'variable does not belong to specified class'
      return any_function(*args, **kwargs)
    return inner_call
  return real_decorator

@check_classes([int, float, np.ndarray])
def sum_of_two_values(value_1, value_2):
  return value_1 + value_2

# sum_of_two_values(1, 10.3)
# sum_of_two_values(np.zeros((3, 5)), 10)
# sum_of_two_values('lol', 'kek')

"task №5"
def cache(func):
    def wrapper(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in memory:
            memory[cache_key] = func(*args, **kwargs)
        return memory[cache_key]
    memory = dict()
    return wrapper

@cache
def sum(a,b):
  time.sleep(5)
  return a + b

@cache
def res(a,b):
  time.sleep(5)
  return a - b

