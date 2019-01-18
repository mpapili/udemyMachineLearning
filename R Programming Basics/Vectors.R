# Vectors
numbers = c(3,2,0,1,8)
print(numbers)

# index starts at 1
print(numbers[1]) # returns 3

# number of items
print(length(numbers))

# get item from the end
numbers[length(numbers)]

# reverse index
print(numbers[-1])

# multiple indices (pass vector)
print( numbers[ c(2,3) ] )

# get values within a range
print( numbers[2:3] )

# change individual elements
numbers[4] = 2
print(numbers[4])

# change multiple elements (pass a vector)
numbers[c(3,4)] = 2
print(numbers)

# sort in decreasing order
numbers = sort(numbers, decreasing=T)
print(numbers)

# sort in increasing order
numbers = sort(numbers, decreasing=F)
print(numbers)

# generate a sequence
oneToTen = 1:10    # numbers 1-10 in a vector
print(oneToTen)

# generate a sequence with logic
add3 = seq(from=3, to=27, by=3)  # counting by 3's till 27
print(add3)

# another example:
evens = seq(from=2, to=20, by=2)
print(evens)

# IS A VALUE IN A VECTOR?
sprintf("4 in evens %s", 4 %in% evens)
