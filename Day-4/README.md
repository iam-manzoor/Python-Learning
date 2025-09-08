## Day - 4 Dictionary & Set in Python

1. **Dictionary in Python**
   - Dictionaries are used to store data values in `key:value` pairs
   - They are unordered(There is no index concept), mutable and dont allow duplicate keys.
   - Dict stores all types data in Python. Even we can store dict with in dict.
   - If key is string always enclose the key in double quote. Key can aslo be an intiger, or Float, or boolean.
   - Example dict
     ```
     dict = {
       "name" = "Arhan",
       "cgpa" = 9.6,
       "marks" = [95.96.99],
       12 : "Intiger"
     }
     ```
   - Refer `01-defineDictionary.py` script for examples.
  
   - **Dictionary Methods**
     - Dictionary also supports methods simillar to the List, tupple and string.
     - Below are the few methods supported by Dictionary.
     - `myDict.keys()` `myDict.values()` `myDict.items()` `myDict.get("key)` `myDict.update(newDict)`
    
2. **Sets in Python**
   - Set is the collection of the unordered items.
   - Each element in the set must be unique & immutable. We can add new element but we cant modify the existing element.
   - Example: `nums = {1,2,3,4}`
   - Repeated elements stored only once. Example `set2 = {1,2,2,2}` `set2 = {1,2}`
   - Empty Set `null_set = set()`
   - In set we can only store `boolean` `int` `string` `tuple` `float`. `List` & `dict` not allowed because they are muttable.
  
   - **Set Methids**
   - `set.add(el)` `set.remove(el)` `set.clear()` `set.pop()` are few methods.
   - To list all the methods supported by set execute `print(dir(set))`
