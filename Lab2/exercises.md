# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

Yes, in the Python Standard Library, the names of dictionary and list member functions generally align well with their actions. For example, functions like pop in dictionaries accurately describe the action of removing a key-value pair, and functions like append in lists clearly indicate their purpose of adding elements. The library's function names are generally descriptive and intuitive, minimizing the potential for confusion.

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

A dictionary and a list differ in their underlying data structures and purposes.

Dictionary: It's a collection of unique key-value pairs stored in a hash table, ideal for quick lookups based on keys.

List: It's an ordered collection of elements, allowing duplicates, and uses integer indexing, suitable for maintaining an ordered sequence of items.

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

Yes, a list in Python allows for random access, meaning you can access any element by specifying its index, such as myList[7]. Lists are ordered collections, and you can retrieve elements by their position in the list using integer indexing.

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

Pros:
Versatility: Can handle various data types, making them adaptable.
Simplicity: Provides a unified interface, reducing specialized code.
Reusability: Promotes code reuse across projects.
Interoperability: Facilitates communication between parts of a program.

Cons:
Performance Overhead: May introduce overhead due to type checking and conversion.
Complexity: Can become complex and require extensive documentation.
Potential Errors: Errors related to different data types can occur.
Limited Optimization: Optimizing for specific types can be challenging.
Compatibility Issues: Ensuring future compatibility can be a challenge.

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

The functions in the Requests module are well-named, using descriptive names that align with their HTTP request methods (e.g., get, post, put, delete, patch). This naming convention makes the library user-friendly and intuitive.

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

Some member functions in the lower-level classes of the Requests library can have a relatively larger number of arguments, which may provide flexibility but could also make them more complex to use. However, for common use cases, the library offers simpler high-level functions with fewer arguments.

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

Definition: It's a Python feature that allows a method to accept a variable number of keyword arguments.

Pros: It provides flexibility, forward compatibility, and a cleaner interface for methods with optional parameters.

Cons: It can reduce code explicitness, potentially lead to runtime errors, and increase complexity when overused.

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?

Why are some arguments set to None?: It indicates optional arguments with default behavior that can be overridden if needed.

Can arguments be set to anything besides None?: Yes, any valid default value can be used based on the method's behavior.

Why might it be good to set an argument by some predetermined value?: It ensures default behavior, offers flexibility for customization, maintains consistency, and serves as documentation for users.
