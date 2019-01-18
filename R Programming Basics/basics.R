# The Basics

# to inspect an object type use class()
print(class(4L)) # integer
print(class(T))  # bool
print(class(TRUE)) # same thing
print(class ('sample')) # string
print(class(charToRaw('sample')))  # bytes


# type testing (important)
print(is.integer(4L))   # True
print(is.integer('cow'))  # false
print(is.character('test'))   # true


# casting to certain types
print(as.integer(4)) # 4 to 4L
print(as.character(4)) # 4 to '4'
