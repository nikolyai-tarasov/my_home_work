def log(filename=None):
    def decorator(func):
        def wrapper(*args, **kwargs):

            try:
                result = func(*args, **kwargs)
            except Exception as e:
                if filename is not None:
                    with open(filename, "a") as f:
                        f.write(f"{func.__name__} error:{e}. Inputs: {args}, {kwargs}\n")

                else:
                    print(f"{func.__name__} error:{e}. Inputs: {args}, {kwargs}")
            else:
                if filename is not None:
                    with open(filename, "a") as f:
                        f.write(f"{func.__name__} ok\n")
                else:
                        print(f"{func.__name__} ok")
            return result

        return wrapper

    return decorator
