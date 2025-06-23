def greet(name):
    """
    Greets the user with the provided name.
    """
    return f"Hello, {name}! Welcome to MyFeature."


if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))