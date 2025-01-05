# The Console - HBNB

<center>
<h1>The Console - HBNB</h1>
</center>

This repository represents the initial phase of a student project aimed at creating a clone of the AirBnB website. This phase introduces a backend interface, also known as a console, to manage program data. Through console commands, users can create, modify, and delete objects, as well as manage file storage. The system employs JSON serialization and deserialization to ensure persistent storage across sessions.

---

<center>
<h3>Repository Contents by Project Task</h3>
</center>

| Tasks                          | Files                                                                                                                   | Description                                                                 |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| 0: Authors/README File         | [AUTHORS](https://github.com/justinmajetich/AirBnB_clone/blob/dev/AUTHORS)                                               | Project authors                                                              |
| 1: Pep8                        | N/A                                                                                                                      | All code is PEP8 compliant                                                  |
| 2: Unit Testing                | [/tests](https://github.com/justinmajetich/AirBnB_clone/tree/dev/tests)                                                  | All class-defining modules are unit tested                                  |
| 3: Make BaseModel              | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py)                     | Defines a parent class to be inherited by all model classes                |
| 4: Update BaseModel w/ kwargs  | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py)                     | Adds functionality to recreate a class instance from a dictionary          |
| 5: Create FileStorage class    | [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py)   | Defines a class to manage a persistent file storage system                  |
| 6: Console 0.0.1               | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py)                                         | Adds basic functionality to the console program, enabling quit, empty lines, and ^D handling |
| 7: Console 0.1                 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py)                                         | Updates the console with methods to create, destroy, show, and update stored data |
| 8: Create User class           | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) | Dynamically implements a user class                                        |
| 9: Additional Classes          | [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) [/models/place.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/place.py) [/models/city.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/city.py) [/models/amenity.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/amenity.py) [/models/state.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/state.py) [/models/review.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/review.py) | Dynamically implements additional classes                                   |
| 10: Console 1.0                | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) | Modifies the file storage system and console to function dynamically with updates to all classes                         |

<br>
<br>

<center>
<h2>General Use</h2>
</center>

1. Begin by cloning this repository.

2. Once the repository is cloned, locate the "console.py" file and run it as follows:
```
/AirBnB_clone$ ./console.py
```

3. Upon executing this command, the following prompt should appear:
```
(hbnb)
```

4. This prompt signifies that you are now in the "HBnB" console. The console application offers a variety of commands for managing your data.

##### Commands

- **create**: Generates an instance based on the given class.
- **destroy**: Eliminates an object based on its class and UUID.
- **show**: Displays an object based on its class and UUID.
- **all**: Shows all objects the program has access to, or all objects of a specified class.
- **update**: Modifies existing attributes of an object based on its class name and UUID.
- **quit**: Exits the program (EOF will also exit the program).

##### Alternative Syntax

Users can issue a variety of console commands using an alternative syntax:

Usage: `<class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])`

Advanced syntax is implemented for the following commands:

- **all**: Shows all objects the program has access to, or all objects of a specified class.
- **count**: Returns the number of object instances by class.
- **show**: Displays an object based on its class and UUID.
- **destroy**: Eliminates an object based on its class and UUID.
- **update**: Modifies existing attributes of an object based on its class name and UUID.

<br>
<br>

<center>
<h2>Examples</h2>
</center>

<h3>Primary Command Syntax</h3>

###### Example 0: Create an object

Usage: `create <class_name>`

```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)
```

###### Example 1: Show an object

Usage: `show <class_name> <_id>`

```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)
```

###### Example 2: Destroy an object

Usage: `destroy <class_name> <_id>`

```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)
```

###### Example 3: Update an object

Usage: `update <class_name> <_id>`

```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```

<h3>Alternative Syntax</h3>

###### Example 0: Show all User objects

Usage: `<class_name>.all()`

```
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

###### Example 1: Destroy a User

Usage: `<class_name>.destroy(<_id>)`

```
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb) User.all()
["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

###### Example 2: Update User (by attribute)

Usage: `<class_name>.update(<_id>, <attribute_name>, <attribute_value>)`

```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb) User.all()
["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

###### Example 3: Update User (by dictionary)

Usage: `<class_name>.update(<_id>, <dictionary>)`

```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb) User.all()
["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

<br>
