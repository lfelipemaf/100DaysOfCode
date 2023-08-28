## Python Decorator Function
# import time
#
# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         function()
#     return wrapper_function
#
# @delay_decorator
# def say_hello():
#     print("Hello")
# @delay_decorator
# def say_bye():
#     print("Bye")
#
# def say_greetings():
#     print("How are you?")
#
#
# say_hello()
# say_bye()
# say_greetings()

# Exercise 1 - Create Your Own Python Decorator
import time

current_time = time.time()
# print(current_time)


def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}s")
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()

