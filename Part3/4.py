#  Izveidot dekoratoru, kas izprintēs funckijas nosaukumu, kad tā tiks izsaukta


def print_function_name(function):
    def wrapper():
        print(f"Executing: {function.__name__}")
        function()
    return wrapper


@print_function_name
def print_ok():
    print("Ok")


print_ok()


