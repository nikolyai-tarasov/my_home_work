def log(filename=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                print(result)
            except Exception as e:
                if filename is not None:
                    with open(filename, "a") as f:
                        f.write(f"{func.__name__} error:{e}. Inputs: {args}, {kwargs}\n")
                else:
                    return f"{func.__name__} error:{e}. Inputs: {args}, {kwargs}"
            else:
                if filename is not None:
                    with open(filename, "a") as f:
                        f.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")

        return wrapper

    return decorator


@log(filename="mylog.txt")
def dauble_2(x):
    return x / x


print(dauble_2(""))
