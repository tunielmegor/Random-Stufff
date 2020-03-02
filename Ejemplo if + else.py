Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> n1=2
>>> n2=15
>>> if n1>n2:
... asdfasdfasdfasdfasd
  File "<stdin>", line 2
    asdfasdfasdfasdfasd
    ^
IndentationError: expected an indented block
>>> if n1>n2:
	print("el 1 es mayor")
... ... else:
... 	print("el 2 es mayor")
... 
el 2 es mayor
>>> 