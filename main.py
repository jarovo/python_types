from typing import List, Dict, Union
from somelib import SomeObject


########################################################################################################################
# When we use name: str, the Ctrl+space shows more relevant options for string
#
# In Pycharm try writing a dot after the variable `name`. Pycharm will expand a menu with available methods for the
# variable's type. Compare the outputs.
def passing_of_arg_untyped(name):
    name
    pass


def passing_of_arg_typed(name: str):
    name
    pass


########################################################################################################################
# Unknown type leads to undetected errors.
#
# When the type is not specified and PyCharm doesn't have any other way to infer(deduce) the type, the dot menu will
# contain only the code completion options.
def unknown_argument_passing(object):
    object.fooo()


# Compare the above with situation where the type is defined.
def known_argument_passing(object: SomeObject):
    object.fooo()   # Pycharm displays warning about unresolved method on this line.


########################################################################################################################
# Example of using value of type that is other than was defined.

my_dict: Dict[str, int]
my_dict[3] = 0      # Pycharm displays warning on this line

# Here we defined my_dict to have keys of type str but then we tried to insert a value with key of different type, so
# PyCharm warns us about it.


########################################################################################################################
# Specifying the types helps to spot a

def check_untyped(a, b):
    a += b
    return a


def check_typed(a: List[str], b: List[str]) -> List[str]:
    a += b
    return a


lines = ["This time"]
tuple_var = "missing comma after the string definition"

# Note we defined a string, not a sequence

check_untyped(lines, var)
check_typed(lines, var)


########################################################################################################################
# Union is a Generic. It allows to specify a type of any

def resolve_str_or_int(obj: Union[str, int]) -> str:
    if isinstance(obj, str):
        # In here PyCharm knows that obj has to be of type str and will offer str's methods.
        return f"{obj} is str"
    elif isinstance(obj, int):
        # In here PyCharm knows that obj has to be of type int and will offer int's methods.
        return f"'{obj}' is int"
    else:
        raise Exception("Unexpected type")


resolve_str_or_int(3)                   # Returns "3 is int"
resolve_str_or_int("I am a string")     # Returns "'I am a string' is str"


########################################################################################################################
# Refactoring
#
# Let's define Type Door and Window and a Car.

class Door:
    def open(self):
        pass


class Window:
    def open(self):
        pass


class Car:
    windows: List        # Note the property `windows` does not well defined type.
    doors: List[Door]

    def open_all_doors(self):
        for door in self.doors:
            door.open()

    def open_all_windows(self):
        for window in self.windows:
            window.open()


# Now try:
# 1) Hover the mouse over the `door.open()` and `window.open()` is there a Difference?
# 2) Click on the word open on each of these lines. Do you spot the difference on lighted-up items?
# 3) Using refactoring, try changing the method names in `open_all_doors` and `open_all_windows` methods.

# Defining the types well enables you to work more effectively -- see and jump to where the method is defined.
# It also enables the algorithms of your integrated developer environment (IDE) to show and then perform some
# refactoring actions.
