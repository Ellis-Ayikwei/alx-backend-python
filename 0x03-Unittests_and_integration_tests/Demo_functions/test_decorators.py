import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to run")
        return result
    return wrapper

@time_it
def slow_function():
    time.sleep(2)
    return "I am done"

print(slow_function())

@time_it
def telme_to_decorate():
    print("I am going to be decorated")
    return "I am the return value of the function"


print(telme_to_decorate())