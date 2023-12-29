sample = 'a'
sample_str = "abc"
sample_str = """abc"""
sample_str = "Todays's weather is nice"
# 'Today's weather is nice'  --> Invalid string
sample_str = """Microsoft Windows [Version 10.0.19045.3803]
(c) Microsoft Corporation. All rights reserved.

C:\devops\repos>python
Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information."""

# """xyz"""  --> We can have a multi line string in triple quotes.
# ""xyz""  --> We cannot have a multi line string in double quotes.

# sample_str = "Microsoft Windows [Version 10.0.19045.3803] \
# (c) Microsoft Corporation. All rights reserved.\
# C:\devops\repos>python \
# Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32 "

#print(sample_str)
# we can use single quotes and backward slash also to print a multi line string but here the formatting of the lines is not followed or disturbed, where as while using the triple quotes the line format is not altered.

#print(len(sample_str))

#print(sample_str.upper())

#print(sample_str.capitalize())

#print(sample_str.count("Microsoft"))

#print(sample_str.split(" "))
#print(sample_str.split("\n"))
#print(sample_str.splitlines())

# sample_str = "Microsoft Windows [Version 10.0.19045.3803]"

## Indexing in Python

#print(sample_str[0])  
# printing first character i.e, M, where the index is 0 from left

#print(sample_str[2])  
# printing third character i.e, c, where the index is 2 from left

#print(sample_str[-1])  
# printing first character from right i.e, ], where the index is -1

#print(sample_str[-2]) 
# printing second character from right i.e, 3, where the index is -2


## Slicing in Python

#print(sample_str[0:3])    
#--> here 0, 1, 2 indexes are only printed index 3 is not included.
# Here to print first 3 characters in a string we need to specify the starting and ending index in the [start-index:end-index-1], where the end-index is not included.

#print(sample_str[0:4])
# Here 4th index is excluded
#print(sample_str[:4])

#print(sample_str[20:])
# Here python will print until the last index or end of the string

#print(sample_str[-1:-4])
# Here Python prints the empty space, because it executes like -1, -1+1, .....

#print(sample_str[-4:-1])
# Here Python will print -4, -3, -2 indexes and excludes -1, which execute like -4, -4+1=-3, -3+1=-2 and excludes -1.

#print(sample_str[-4:])
# Here python starts from -4 and goes on till end of the string

#print(sample_str[:])
# Here Python prints the whole string, starting and ending points are not specified.

#[start:end:step]

#print(sample_str[::2])
# Here the step size is 2 which is mentioned after '::'
# Here Python prints the First character and omit the second character then prints the third character and so on... every alternate character is being print.

#print(sample_str[1::2])
# Here the step size is 2 
# Here Python starts from the first index, omits the second index, print the third index and so on ... till the last index.

## To reverse a string ##
#[start:end:step]
# start : 0
# end : 
# step : -1
#print(sample_str[::-1])

### Properties of a string

# sample_str = "Microsoft Windows [Version 10.0.19045.3803]"
# sample_str[0] = 'P' # Is  not allowed
# print(sample_str)
  # 'str' object does not support item assignment

## String concatenation
# sample_str = "Microsoft Windows [Version 10.0.19045.3803]"
# sample_str = sample_str + "(c) Microsoft Corporation. All rights reserved." # OR
# sample_str + "(c) Microsoft Corporation. All rights reserved."
# print(sample_str)

## Multiplication of String
# sample_str = 'abc'
# sample_str *= 10
# print(sample_str)
# print(len(sample_str))

## Print Formatting
sample_str = "Microsoft Windows [Version 10.0.19045.3803]"

# sample_str = "{}".format(sample_str)
# print(sample_str)

# sample_str = "{0}{1}".format(sample_str, "abc")
# print(sample_str)

# sample_str = "{1}{0}".format(sample_str, "abc")
# print(sample_str)



