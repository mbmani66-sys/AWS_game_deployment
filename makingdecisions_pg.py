age = 10
if age ==10:
    print("you are ten years old.")

monsters = 3
coins = 4

coins > monsters
print(coins > monsters)
monsters == coins
print(monsters == coins)

monsters < coins
print(monsters < coins)
coins > monsters 
print(coins > monsters)

(monsters == 3) and (coins == 4)
print((monsters == 3) and (coins == 4))
(monsters == 7) or (coins == 4)
print((monsters == 7) or (coins == 4))

score = 110
snails = 3
(score > 100) and (snails >=4)
print((score > 100) and (snails >=4))

spells = 11
if (spells > 10):
    print("you gained the title enchanter!")

ghosts = 3
if ghosts > 1:
    print("It's so spooky!")
elif ghosts >0:
    print("Get that ghost!")
else:
    print("Ghosts all gone!")

game_over = True
if game_over:
    print("Game Over!")
else:
    print("Keep playing!")    


for count in range(1,11):
    print("you are the high scorer!")   

robots = ["Bing", "Bleep", "Bloop"]
for robot in robots:
    print("I am a robot. My name is " + robot)     

    robots = ["Bing", "Bleep", "Bloop"]
Colours = ["red", "orange", "purple"]
index = 0 
for each in robots:
    print("My name is " + robots[index] + ".I am " + Colours[index])
    index = index + 1

answer = input("Throw a water baloon? (y/n)")
while answer == "y":
    print("splash!!!")
    answer = input("Throw another water balloon? (y/n)")
print("Goodbye!")       

