print("This is a parameter")


# name = input("What is your name?")
# print(name)

kjhi = "functions are fun".count("fun")
print(kjhi)
print("blue".upper())

countdown = [1,2,3]
countdown.reverse()
print(countdown)

message = "coding makes me happy"
print(message.replace("happy", ":D"))

def fruit_score():
    print(10)

fruit_score()    

def fruit_score(fruit):
    if fruit == "apple":
       print(10)
    elif fruit == "orange":
       print(5)

fruit_score("apple")
fruit_score("orange")

def fruit_score(fruit):
    if fruit == "apple":
        return 10
    elif fruit == "orange":
        return 5     

apple_score = fruit_score("apple")
orange_score = fruit_score("orange")

total = fruit_score("apple") + fruit_score("orange")
print(total)