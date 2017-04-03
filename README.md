# python-basis

* Python is an interpreted language
* The interpreter and the extensive standard library are freely available from Python Web Site (https://www.python.org/)
* The interpreter is easily extended with new functions and data types implemented in C and C++
* Simpler than Java or C/C++ and more powerful than unix shell script or Windows batch files
* More error checking than C
* Python allows to split the program into modules, standard modules includes:
   * I/O
   * System calls
   * Sockets
   * UI

* Comparing to Java and C++
   * The high-level data types allows to express complex operations in a single statement
   * Statements grouping is done by indentation instead of beginning and ending brackets
   * No variable or arguments declarations are necessary


* Python standard library: https://docs.python.org/3/library/index.html#library-index


## Dev environment setup

1. Download and install python 3.6 from: https://www.python.org/downloads/mac-osx/ 
2. It is usually installed on /usr/local/bin/python3.6
3. After installed it can be invoked in command line by typing python3.6
4. To exit the prompt type: Control-D or type quit()
5. It is not necessary an IDE but some helpful IDEs can be:
   * PyCharm (Idea)
   * Netbeans
   * Eclipse

### Files encoding
By default files are treated as encoded in UTF-8

## Python sintax

### Comments

Comments starts with the hash character (#) and extend to the end of the physical line

### Operators

#### Arithmetic

* Plus +
* Minus -
* Multiply *
* Classic division /
* Floor division //
* Reminder %
* Power ** 
* Assignment =
* In interactive mode the last printed expression is assigned to variable "_"
* In addition to **int** and **float** python supports **Decimal** and **Fraction** and has built
 in support for complex numbers and uses **j** or **J** to indicate the imaginary part.
 
#### Boolean operators
* and
* or
* not

#### Comparisons

* Less than <
* Less than or equal <=
* Greater than >
* Greater than or equal >=
* Equal ==
* Not equal !=
* Object identity **is**
* Negated object identity **is not**
 
#### Bitwise operators

* Or |
* X-or ^
* And &
* Shift left <<
* Shift right >>
* Invert bits ~

More about data types: https://docs.python.org/3/library/stdtypes.html

#### Strings

* Strings are enclosed in single quotes or double quotes with the same meaning
* Special characters are escaped with backslashes 
* Raw strings are preceded by character r (r'Some string'), and using those ones escaped characters are not interpreted
* **Concatenation** is achieved using + operator
* Strings can be **repeated** using * operator 
* Characters in string can be indexed using [] operator, being the first character 0-index
* It is possible to use negative indexes to start counting from the right
* Slicing is supported using [begin_index:end_index] begin included, end excluded
* Begin or end can be omitted 
* Python strings are **immutable**
* String length is retrieved using built in function **len**

More information:

https://docs.python.org/3/library/stdtypes.html#textseq<br/>
https://docs.python.org/3/library/stdtypes.html#string-methods<br/>
https://docs.python.org/3/reference/lexical_analysis.html#f-strings<br/>
https://docs.python.org/3/library/string.html#formatstrings<br/>
https://docs.python.org/3/library/stdtypes.html#old-string-formatting<br/>

#### Lists

* Lists can be written as a sequence of comma separated values which can be different in type <br/>squares = [1, 4, 9, 16, 25]
* Lists can be indexed and sliced as strings
* Lists can be concatenated using +
* Lists are **MUTABLE**
* Using append method can be added new items to the list
* Assign to slice is also possible
* List length is retrieved using built in function **len** 

  
## Control flow

### If statement
```python
x = 10
if x < 0:
    print ('Negative value')
elif x == 0:
    print ('zero')
else:
    print('Positive value')
```

### For statement

For each style
```python
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
```

Using range
```python
for i in range(5):
    print(i)
```

* For supports break and continue as in Java or C but **adds support for else statement**

### Pass statements

pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action
```python
def new_function(parameter):
    pass
```

## Functions
```python
def new_function(parameter):
    return parameter
```

### Default argument values

### Keyword arguments

### Arbitrary argument lists

### Lambda expressions
  
### Handling exceptions
```python
def number(parameter):
    try:
        return int(parameter)
    except ValueError:
        return float(parameter)
```

## Data structures

### Lists

### Tuples

### Sequences

### Sets

### Dictionaries

## Modules

### Standard modules

### Packages

## Coding style (PEP 8)

* Use 4-space indentation, and no tabs.
* Wrap lines so that they don’t exceed 79 characters.
* Use blank lines to separate functions and classes, and larger blocks of code inside functions.
* When possible, put comments on a line of their own.
* Use docstrings.
* Use spaces around operators and after commas, but not directly inside bracketing constructs: a = f(1, 2) + g(3, 4).
* Name your classes and functions consistently; the convention is to use CamelCase for classes and lower_case_with_underscores for functions and methods. Always use self as the name for the first method argument (see A First Look at Classes for more on classes and methods).
* Don’t use fancy encodings if your code is meant to be used in international environments. Python’s default, UTF-8, or even plain ASCII work best in any case.
* Likewise, don’t use non-ASCII characters in identifiers if there is only the slightest chance people speaking a different language will read or maintain the code.



### Documentation strings

https://docs.python.org/3/tutorial/controlflow.html#documentation-strings

## Installing python modules  (pip)


## Python unit tests


## References

https://docs.python.org/3/tutorial/
http://stackoverflow.com/questions/81584/what-ide-to-use-for-python
https://docs.python.org/2/library/unittest.html
