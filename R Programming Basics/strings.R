# Strings
str1 = "this is a string"

# number of characters
nchar(str1)

# comparisons
# letters compared alphabetically
sprintf("Dog > Egg : %s", "Dog" > "Egg")

# combine strings
str2 = paste("OW!", "Bear", sep=" ")
print(str2)

# take substrings
substring = substr(x=str2, start=4, stop=7)
print(substr)

# replace text
subbedStr = sub(pattern="OW", replacement="Hawk", x=str2)
print(subbedStr)

# string vector
strVect = strsplit('A dog ran fast', ' ')
print(strVect)