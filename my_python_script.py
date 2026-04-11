print("My first python script in VS Code")
print("Fly you fools!")
import random

greetings = [
    "Hello, Git!",
    "Greetings, developer!",
    "Welcome to branching!",
    "Hi there, coding friend!",
    "Happy coding!",
]


def get_random_greeting():
    return random.choice(greetings)


print(get_random_greeting())
print("Learning about branches today!")
