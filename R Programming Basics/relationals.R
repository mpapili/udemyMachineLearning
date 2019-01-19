# Relationals

sprintf("4 == 5 : %s", 4 == 5)
sprintf("4 != 5 : %s", 4 != 5)
sprintf("4 > 5 : %s", 4 > 5)
sprintf("4 <=5 : %s", 4 <= 5)

print(class(4 == 5))


oneTo20 = c(1:20) # vector one to twenty
isEven = oneTo20 %% 2 ==  0   
print(isEven)


justEvens = oneTo20[oneTo20 %% 2 == 0]
print(justEvens)