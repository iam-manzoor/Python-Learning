## Day 3 List & Tuple in Python

1. **Lists in Python**
- A built-in data type that stores set of values. Its sort of equalant to Array's in other programming languages.
- A list can store different types of elements. (String, intigger, float, list, dict)
  - Example `student=["Arhan",10,2.0]`
- String is immutable but the List's in Python is mutable.
  
  - **List slicing**
    - Example `list_name[starting_idx:ending_idx]` #Ending idx is not included.
    - Slicing result will get sublist.
    - Supports negative indexing as well.

  - **List Methods**
    - Below are the few methods from List.
    - `append` `sort` `reverse` `insert` Refer 03-listMethods.py script
    - Diff between `pop` and `remove` method?
      - `pop` works on the index. `remove` works on the value.
    - To list the methods supported by List. execute `print(dir(list))`
    - When you print method operations it will return `None`. You have to print list variable.
