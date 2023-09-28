# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
	- MObject is a concrete class. This is because it has a constructor (__init__ method) defined, and there are no abstract methods within the class. Concrete classes can be instantiated, and they may or may not have concrete implementations for all their methods. In this case, MObject has a constructor but does not define any additional methods or attributes.
1. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	- The commented-out __del__ method in the 'Image' class is a destructor method. In Python, the __del__ method is called when an object is about to be destroyed or deallocated, typically when there are no more references to it. It is used for performing cleanup operations before an object is removed from memory. However, it is generally not recommended to use __del__ for cleanup purposes in Python, as there are more reliable ways to manage resources, such as using the context manager (with statement) or the __enter__ and __exit__ methods in a class.
1. What class does Texture inherit from?
	- The 'Texture' class inherits from the 'Image' class.
1. What methods and attributes does the Texture class inherit from 'Image'? 
	- The 'Texture' class inherits the following methods and attributes from the 'Image' class:

__init__(self, w, h) constructor method
getWidth(self) method
getHeight(self) method
getPixelColorR(self, x, y) method
getPixels(self) method
setPixelsToRandomValue(self) method
Attributes: m_width, m_height, m_colorChannels, m_Pixels
1. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
	- 'Texture' represents a specialized type of 'Image' with additional features or behaviors, so an 'is-a' (inheritance) relationship is appropriate. If 'Texture' had methods or attributes specific to textures that are not present in the generic 'Image' class, inheritance would make sense. 
1. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
	- Yes, Python automatically creates a default constructor if one is not explicitly defined in a class. This default constructor takes no arguments and does nothing, allowing you to create instances of the class.

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?

No, singleton patterns in Python are not inherently thread-safe. In a multi-threaded environment, there is a possibility that multiple threads could simultaneously check if the instance is None and then attempt to create it. This could result in multiple instances being created. To make a singleton thread-safe, we can use synchronization mechanisms like locks or the threading module. However, in the task2 code, it does not include thread-safety mechanisms, so it's not thread-safe by default.

*edit the code directly*  
  
