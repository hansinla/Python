from math import *

cosX = cos(radians(255))
sinX = sin(radians(255))

answerX = cosX * 2 - sinX * 3
answerY = sinX * 2 + cosX * 3

#print("j'x:",answerX,"\nj'y:", answerY)

x = 0
for i in range(1, 181):
    x+=i

#print("After 180 rotations:",x % 360,"degrees.")


cosX = cos(radians(95))
sinX = sin(radians(95))

answerX = cosX * 6 - sinX * 8
answerY = sinX * 6 + cosX * 8

#print("j'x:",answerX,"\nj'y:", answerY)

cosX = cos(radians(45))
sinX = sin(radians(45))

answerX = cosX * 1 - sinX * 1
answerY = sinX * 1 + cosX * 1

print("j'x:",answerX,"\nj'y:", answerY)
    
