import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + "took " + str((end - start) * 1000) + "mil sec")
        return result

    return wrapper


@time_it
def calc_square(numbers):
    result = []
    for i in numbers:
        result.append(i * i)
    return result


@time_it
def calc_cube(numbers):
    result = []
    for i in numbers:
        result.append(i * i * i)
    return result


array = range(1, 10000)
out_square = calc_square(array)
out_cube = calc_cube(array)
