# Day - 6 Functions & Recursion in Python

1. **Functions in Python**
   - Block of statements that perform a specific task.
   - Function promote code reusability.
   - Function that doesnt return anything, on calling that function it will return **None**
   - function example
   ```
   def func_name(param1, param2...):  # (param1,param2,..) are called parameters
     # Execution statements
     return val

   func_name(2,4)                     # func_name() is fun call. (2,4) fun arguments
   ```
   - **Types in function**
     - Built-in-functions: `print` `len` `range` `type` etc.. Are part of ptyhon ships default.
     - User defined function. Written by the developers which are not available by default.

   - **Default Parameters**
     - Assigning a default value to parameter, which is used when no argument is passed.
     - Non default argument declared first. Default at the end in the parameter.
     - Arguments overwrite the default parameters declared in the function.
     - If the parameter has default value declare it at the end of the parameter list in the fun definition.

2. **Recursion in Python**
   - When a function calls itself repeatedly.
   - Its a loop in function.
   - Every recursive call creates a call stack in memory.
   - Example
   ```
   def rev_num(n):
      if n == 0:
         return
      print(n)
      rev_num(n-1)
   rev_num(6)
   ```
