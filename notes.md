# Python Notes
- The extension for the Python file is **.py**
- In any programming or scripting language there are 4 important blocks to understand
1. Variables
2. Conditions
3. Loops
4. Functions

## Arithmetic operations
- `+` : Addition
- `-` : Subtraction
- `*` : Multiplication
- `/` : Division
- `//` : Floor Division
- `%` : Modulo Operator 
- `**` : Power

## Data types
- Integer  Eg : 1,2,3,4...
- Float   Eg : 1.2, 2.4, 3.0, ..
- Boolean Eg : True, False
- String Eg: 'a', "This is a string", "Today's weather is nice"
- List
- Tuple
- Set 
- Dict

## Order of Operation
- BODMAS or DMAS

#### String Methods

- `len()` used to calculate the length of the string.
- `upper()` used to write the string in upper case
- `capitalize()` used to convert the only first letter/character  of a string to capital and remaining all letters/characters to lower case.
- `count()` used to find the number of occurrences of characters/word inside a double quotes.
- `split()` used to differentiate the string using a delimiter. eg: " " --> space  "\n" --> new line character.
  - Here `splitlines()` is same as that of using 'split("\n")' gives us the same result.


### Indexing and slicing


## Indexing
- In python, the Indexing of an element starts from 0.
- We specify the index of an element inside the `[]`
- Python supports both +ve and -ve indexing, i.e, 0, 1 and -1, -2

## Slicing
- Here to print first 3 characters in a string we need to specify the starting and ending index in the [start-index:end-index-1], where the end-index is not included. e.g: `print(sample_str[0:3])` .  Here 0, 1, 2 indexes are only printed index 3 is not included.
- If the starting index is omitted or 0 , you no need to specify `[:3]` is same as `[0:3]`, Python consider it directly as 0.
- Similarly if the end index is not included or specified, Python considers it as the last index or final index. eg: `[10:]`. Python will print until the end of the string.
- Python prints like start, start+1, start+2, start+3, .... until end
- For -ve index slicing we need to specify like `[-4:-1]`, which means 
- We can use step size to fetch the elements at a specified interval. i.e, `[start:end:step]`
- If the step value is not specified then Python considers it as 1.
- To reverse a string we use `[::-1]`

### Properties of String
- String is Immutable, i.e, the elements that are once defined cannot be altered.
- String concatenation using `+`
- Multiplication of string `*`
- String supports both `+` and `*` operations on it.

## Print Formatting
- `.format()`

### Lists

## List Data Type

## Methods
- `.append()`  Using append you can only able to add one element at the end of the given list
- `.extend()`  Using extend you can add more than one element at the end of the given list
- Both append and extend methods are inplace operations i.e, they modify the original list. 
- `pop()`  To pop off an item from a list at a given index, and is an inplace operation.
- `reverse()` Reverse a given list and is a inplace operation.
- `sort()` Sort an given list and is an inplace operation
- `sorted()` Sort and return the sorted list only

## Nesting Lists
- Lists inside a list are called Nesting Lists.

## Unpacking the List
- Extract individual values from a list into individual variables.

## Properties of string
- List is a mutable data type i.e, the elements can be altered after they are defined
- It also supports `+` `*` i.e, extending the original list.

## Tuple data type
### Constructing Tuple
### Methods
### Properties

#### Defining and  Constructing Tuple
- A Tuple in a Python can be defined using `()` eg: (1, 2, 3)
- Tuples are used to store multiple items in a single variable.
- Tuple is one among 4 built-in data types in Python, used to store collections of data. The other 3 are List, Set and Dictionary all with different qualities and usage.

#### Properties of Tuple
- A tuple is a collection which is ordered and unchanged.
- Tuple is immutable, therefore it cannot support append and extend operations
- Tuple is Heterogeneous: Tuples can contain data of types
- Contains duplicates: Allows duplicates data
- Can unpack a Tuple.

### Methods
- `index()`
- `count()`


## Dictionary Data Type
- A dictionary is created using  a `{'key' : 'value'}` pair structure.
- Keys always should be of Immutable data type such as tuple, strings, numbers etc
- In dictionaries, the order in which the elements are inserted is retained.
- Nested dict data type
```python
 sample_dict = {
    "employee": {
        "name": "John",
        "age" : 30,
        "city" : "New York"
    }
}
```
## Methods in dict
- `keys()`
- `values()`
- `items()`

## Sets Data type
- The order of insertion in set is not retained.
- Set doesn't allow duplicates in the data set.
- To add elements to a set we use `add()` method.

### Typecasting
- Changing the datatype of a variable i.e, list --> tuple or list --> set etc


## Booleans
- `True` and `False` are only two values that possible with Boolean.


## Comparisons
- `==` compares the two values are equal or not, returns `true` if equal and `false ` if not equal.
- `!=` not equal to i.e, compares whether the values are equal or not
- `>`, `<`, `>=`, `<=`

### Chained comparisons
- Eg: `1 < 2 < 3` --> (1 < 2) and (2 < 3)
- `and` --> If both the conditions are true then only the result is true
- `or` --> If either of the conditions are true i.e, any one of the conditions are true then the result will be true
- `not` --> If true then it give false result, if false it gives true result.


## Conditions in Python
- `If-else` statement
- `If-elif-else` statement


## Loops in Python


### Membership operator
- We use membership operator to check whether an element is present inside the variable.
- 
