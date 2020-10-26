from playerfile import Player

# import playerfile -- this is one way to import

tim = Player("tim")
print(tim)
tim.level += 1
print(tim)
tim.lives -= 1
print(tim)
tim.level -= 1
print(tim)

tim.level -= 1
print(tim)
tim.level -= 1
print(tim)

tim.score = 10
print(tim)
# if setter and getter is declared in class , then python automatically uses function to get or set the values.

