def log(filename):
    def decorator(func):
        def wrapper(*args):
            result = func(*args)
            try:
                if filename != "":
                    return result
                else:
                    return open(filename, "my_function ok")
            except Exception as e:
                if filename != "":
                    return f"my_function ok"
                else:
                    return open(filename, f"my_function error: {e}. Inputs: {args}, ")

        return wrapper

    return decorator


@log(filename="mylog.txt")
def dauble_2(x):
    return x * x


print(dauble_2(4))
