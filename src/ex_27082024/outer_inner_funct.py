def outer_function():
    variable = 30
    def inner_function():
        print(variable)

    return inner_function()