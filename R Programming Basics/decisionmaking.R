# decision making
age = 18

if(age >= 18){
  print("Drive and Vote")
} else if (age >= 16){
  print("Drive")
} else {
  print("wait")
}

# another way to do it with switch()
grade = "C"
switch(grade,
       "A" = print("Great"),
       "B" = print("Good"),
       "C" = print("Okay"),
       "D" = print("Bad"),
       "F" = print("oh man..."),
       print("no such grade"))