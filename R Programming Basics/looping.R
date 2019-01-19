# Looping

# repeat loop
num = 1
repeat{
  print(num)
  num = num + 1
  if(num > 5){
    break
  }
}

# while loop that prints odd numbers
num = 5
while(num > 0){
  num = num - 1
  if(num %% 2 == 0){
    next # skips rest and loops back to top
  }
  print(num)
}


# for loop for vectors
oneTo5 = 1:5
for(i in oneTo5){
  print(i)
}