## Day - 7 FIle Input/Output in Python

1. **FIle I/O**
   - I/O menas Input and Output
   - Python can be used to perform operations on a file. (read & write data)
   - Read, Write, Update, Delete and Append data within file.
   - To perform any of the above operation we need Open the file abd close it when the operation is completed.
   - In Write and Append mode the files will be created if it doesnt exist. 
   - Types of all files
     1. Text Files : .txt, .docx, .log, .csv, .yaml, .json etc.
     2. Binary Files : .mp4, .mpv. .png, .lpeg etc..
   - Be it a text or Binary files when stored in memory it will be in the binary format.
  
   - **Open, read & close File**
     - we have to open a fiel before reading or writing.
     - `f = open("fine_name","mode")` `r` read mode `w` write mode

   - **Different modes**
     - `r` Open for reading (default).
     - `r+` Reading and writing. The stream possioned at the begining of the line.
     - `w` Open from writing, truncating the file first. (Delete the exisitng content).
     - `w+` Reading and Writing but will truncate the file.
     - `x` Create a new file and open it for writing.
     - `a` open for writing, appending to the end of the file if it exists.
     - `a+` opens the file for reading and writing, but the stream is posioned at the end of the file.
     - `b` binary mode.
     - `t` text mode (default).
     - `+` open a disk file for updating (reading and writing).
    
   - **Reading a file**
     - `data = f.read()` reads entire file.
     - `data = f.read(5)` reads the number of characters specified.
     - `data = f.readline()` reads one line at a time.
     - Once the data is read we can not read it again. The pointer moves as we read the data. So to read again we have to open the file onde more time.

   - **Writing to a file**
     - `f = open("demot.txt","w")` Open the file in write mode.
     - `f.write("This is a new line")` Overwrite the entire file.

   - **Append to a file**
     - `f = open(demo.txt","a")` open the file in append mode.
     - `f.write("This is append operation")` Adds the line to the end of the file.

   - **with Syntax**
     - `with` auto clos the file
     ```
     with open("demo.txt", "a") as f:
       data = f.read()
       print(data)
     ```
