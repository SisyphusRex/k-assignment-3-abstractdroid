# Assignment 3 - Inheritance, Abstract Classes, and Polymorphism

## Author

Walter Podewil

## Description

The Jawas on Tatooine have recently opened a droid factory and they want to hire you to write a program to hold a list of the available droids, and the price of each droid. The price is based on the type: (protocol, utility, janitor, or astromech), the material used, and the various options that a particular droid has. The Jawa will choose the various options for a specific droid when adding that droid to the list of droids.

A Jawa will be presented with a user interface to add a new Droid, or print the current Droid collection. Adding a new Droid will require input from the Jawa to create the new droid. Once all of the needed information is collected for the droid, the new droid will be added to the droid collection.

If a Jawa decides to print the collection of droids in inventory, the program should loop through all of the droids in the collection and print out all of the various properties of each droid as well as the total cost of the droid. You should try to use a combination of the `__str__` and `total_cost` method/attribute along with Polymorphism to reduce the amount of code needed to print the results of each droid.
**NOTE:** You may want to print each droid as a block of text rather than trying to cram all of the various properties for the droid onto a single line.

All of the prices for the various aspects of a droid are left up to you to determine. If I was doing it though, I would probably have a small set price for each of the following general options, and not get too specific to save time. ie:
1. A price for the droid model (protocol, utility, etc.)
2. A few different material choices (Something made up), each with a different price. Have at least 4 choices.
3. A few different color choices (Something made up), each with a different prince. Have at least 4 choices.
4. A price for each additional option. One of the various option bools listed below. (3 options selected * $10 per option = $30)
5. A price per quantity option such as: numberOfLanguages, and numberOfShips (3 ships * $10 per ship = $30)

The program comes with an Abstract Base Class (ABC) called `AbstractDroid` that must be implemented by subclasses and can **NOT** be altered. You **MUST** use it as is. It contains a public method called `calculate_total_cost`, and a public attribute called `total_cost`. The `calculate_total_cost` method should not return anything, so it's job is to access the properties of the droid and literally calculate the total cost and then store it in the `total_cost` variable. It should **NOT** return the total cost. It should only calculates it.
The `total_cost` attribute is how you will get access to the total cost of the droid. This will be zero until `calculate_total_cost` is called. Then it will have a value.
I don't want you to have `calculate_total_cost` return the calculated value because I wanted you to have to use both a method and a property in subclasses.
Failure to follow this requirement will mean zero points for those parts of the program that are not using it correctly.

You should put all of your user interface into a `UserInterface` class that will handle getting all of the necessary information from the Jawa, and display the feedback to the Jawa.

You should create a class for the collection of the Droids. The `DroidCollection` class should contain the list that holds the droids, and maintain any internal information needed to manage that list. It should have at least one and at most four `add` methods that will add droids to the list. Whether you use one method that then determines which type of droid to create and add to the list or four separate methods that each adds a specific type of droid to the list is up to you. The `UserInterface` class will prompt for the needed information to add a droid, and then when it has all of the info, it will send it to these `add` methods to get the droid added.

You should follow the concepts about inheritance talked about in class, and work hard at DRY (Don't Repeat Yourself) Principles.

**NOTE:** This is the main focus of this program. Utilize inheritance and polymorphism as efficiently as possible. The less duplicated code, the better you will do on this assignment.

## Classes

The following Droid classes can all be created in a file called `droids.py`. The only class that should not be in this file is the `AbstractDroid` that was provided to you and the `UserInterface` class, which should be in a file called `user_interface.py`.
In total, you will have the following python files:
* `main.py`
* `program.py`
* `abstract_droid.py`
* `droids.py`
* `user_interface.py`

The program should have another `Abstract Base Class` called `Droid` with the following variables, properties, constructors, methods, etc that inherits from the `AbstractDroid` class that is provided to you.

`Droid`:

* Variables: `material` (string), `color` (string), `total_cost` (float - required by ABC)
* Constructors: 2 parameter constructor (`string`, `string`)
* Public Methods:
	* `__str__`: return a formatted string containing the properties of the droid.
	* `calculate_total_cost`: Required by the ABC to calculate and store the total cost.
* Protected Methods:
	* Your Choice - But think about what might be able to be protected to save you work in derived classes.

There should be two child classes derived from the abstract class `Droid` with appropriate variables, methods and properties. Both of these droid types can be created by a Jawa in the system.

`Protocol`:

* Variables: `number_of_languages` (int)
* Constant: `COST_PER_LANGUAGE`
* Constructors: 3 parameter constructor (`string`, `string`, `int`)
	* Uses the base class (`Droid`) constructor
* Public Methods:
	* `__str__`: return a formatted string containing the variables
	* `calculate_total_cost`: Calculate the `total_cost` based on the number of languages and droid type. Then add those values to any costs that can be calculated by the base class.
* Protected Methods:
	* Your Choice - But think about what might be able to be protected to save you work in derived classes.

`Utility`:

* Variables: `toolbox` (bool), `computer_connection` (bool), `scanner` (bool)
* Constructors: 5 parameter constructor (`string`, `string`, `bool`, `bool`, `bool`)
	* Uses the base class (`Droid`) constructor
* Public Methods:
	* `__str__`: return a formatted string containing the variables
	* `calculate_total_cost`: Calculates `total_cost` by calculating the cost of each selected option and droid type. Then add those values to any costs that can be calculated by the base class.
* Protected Methods:
	* Your Choice - But think about what might be able to be protected to save you work in derived classes.

There should be two more derived classes from the class `Utility` with appropriate variables, methods and properties.
**NOTE:** Even though `Utility` is the base class for these droids, `Utility` itself is still a valid droid option that can be created in the system.

`Janitor`:

* Variables: `broom` (bool), `vacuum` (bool)
* Constructors: 7 parameter constructor (`string`, `string`, `bool`, `bool`, `bool`, `bool`, `bool`)
	* Uses the base class (`Utility`) constructor
* Public Methods:
	* `__str__`: return a formatted string containing the variables
	* `calculate_total_cost`: Calculate `total_cost` by calculating the cost of each selected option and droid type. Then add those values to any costs that can be calculated by the base class.
* Protected Methods:
	* Your Choice - But think about what might be able to be protected to save you work in derived classes.

`Astromech`:

* Variables: `navigation` (bool), `number_of_ships` (int)
* Constant: `COST_PER_SHIP`
* Constructors: 7 parameter constructor (`string`, `string`, `bool`, `bool`, `bool`, `bool`, `int`)
	* Uses the base class (`Utility`) constructor
* Public Methods:
	* `__str__`: return a formatted string containing the variables
	* `calculate_total_cost`: Calculate totalCost by calculating the cost of each selected option, the cost based on the number of ships, and the droid type. Then add those values to any costs that can be calculated by the base class.
* Protected Methods:
	* Your Choice - But think about what might be able to be protected to save you work in derived classes.

![Droid Class Diagram](https://barnesbrothers.ddns.net/cis226/assignmentImages/assignment_3.png "Droid Class Diagram")

## Solution Requirements

Solution Must:

* Allow Jawa to add a new droid of either (`Protocol`, `Utility`, `Janitor`, or `Astromech`) to the list
* Allow Jawa to print the list of droids out.
* Do **NOT** make any changes to the `AbstractDroid` class.
* Do **NOT** change the method signature or return type of the `calculate_total_cost` method
* Create abstract class `Droid` that implements `AbstractDroid`
* Derive two classes (`Protocol` and `Utility`) from the class `Droid`
* Derive two classes (`Janitor` and `Astromech`) from the class `Utility`
* Each derived class (`Protocol`, `Utility`, `Janitor`, and `Astromnech`) must either override the `__str__` and `calculate_total_cost` methods or elegantly use functionality from its parent to achieve what it needs.
* Create a `UserInterface` class
* Create a `DroidCollection` class
* Use `private`, `protected`, and `public` access modification appropriately.
* Use `@abstractmethod` decorator appropriately.
* Have sufficient comments about what you are doing in the code.

### Notes

If you did not do well on Assignment 1, you may want to look at the Assignment 1 Key that I did for some help related to UI classes, Collection classes, and structure.

It may be beneficial for you to create extra methods within the droid sub classes. You are not limited to the ones mentioned. You may even find it useful to make some additional ones that are protected.

You may not need to override the `__str__` method in child classes. You certainly can. But, if you do, you should try to delegate as much as possible to the parent class and only change what is needed for the child. The same goes for the `calculate_total_cost` method. The child classes should not be redoing the work of their parents if a call to the parents version can achieve the same effect.

## Grading
| Feature                            | Points |
| ---------------------------------- | ------ |
| `Droid` Class                      | 10     |
| `Protocol` / `Utility` Classes     | 15     |
| `Janitor` / `Astromech` Classes    | 15     |
| `__str__` / `calculate_total_cost` | 10     |
| `UserInterface` Class              | 10     |
| `DroidCollection` Class            | 10     |
| Add Droid Functionality            | 5      |
| Print List Functionality           | 5      |
| Access Modifiers Correct           | 5      |
| Abstract Methods Correct           | 5      |
| Documentation                      | 5      |
| README                             | 5      |
| **Total**                          | **100**|

## Outside Resources Used
geeksforgeeks.org/enumerate-in-python/
    Learned how to use enumerate rather than looping over range(len(<list>))

https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
    Learned how to find files in a directory

https://stackoverflow.com/questions/72063145/how-can-i-loop-through-all-the-py-files-in-my-current-directory-import-a-vari
    iterate through directory and import

https://stackoverflow.com/questions/8718885/importing-module-from-string-variable-using-import-gives-different-results
	import module based on string

https://docs.python.org/3/library/inspect.html
    inspect module

https://www.geeksforgeeks.org/string-capitalize-python/
    capitalize() method

https://stackoverflow.com/questions/59986625/how-to-simulate-two-consecutive-console-inputs-with-pytest-monkeypatch
    pytest series of user inputs

https://stackoverflow.com/questions/51700960/runtimeerror-generator-raised-stopiteration-every-time-i-try-to-run-app
    catch StopIteration for pytest

https://stackoverflow.com/questions/35998992/py-test-command-not-found-but-library-is-installed
    run pytest from terminal

https://stackoverflow.com/questions/12813633/how-to-assert-two-list-contain-the-same-elements-in-python
    assert whether lists are equal in different ways
## Known Problems, Issues, And/Or Errors in the Program
None as of 10/1/24

10/5/2024: Need to reformat __str__ methods in droid and subclasses to format for printing.  use concatenation before :<10 format

10/7/2024: Need to write method or enforce standard on dicts of qualities like color or material

10/8/2024: Need to add printing in color functionality to user_interface.py
    NOTE: I want to print the droids color options in that color, but when the droid_collection is printed out, the color is part of a string.  I will need to identify the color using regular expressions.

    NOTE: On second thought, printing the colors in their color would involve me hardcoding the colors to the program rather than dynamically searching for the qualitative attribute dict in the modules.

10/12/2024: Everything works, yet I am still not using regex to search every string for color and print in that color, perhaps get to it later
