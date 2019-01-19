# Factors
direction = c('up', 'left', 'right', 'down', 'left')
factorDir = factor(direction)

factorDir # notice how duplication is removed
myLevels = levels(x=factorDir)

print(myLevels)

dow = c('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

wDays = c('Tuesday', 'Thursday', 'Monday')

wdFact = factor(x=wDays, levels=dow, ordered = T)
print(wdFact)