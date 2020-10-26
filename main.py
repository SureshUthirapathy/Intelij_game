from enemy import Enemy,Troll, Vampyre, VampyreKing

# random_monster = Enemy("Basic_Enemy", 12, 1)
# print(random_monster)
# random_monster.take_damage(4)
# print(random_monster)

ugly_troll = Troll("pug")
print("ugly troll : {0}".format(ugly_troll))

another_troll = Troll("Ug",3)
print("another_troll : {0}".format(another_troll))

brother = Troll("Urg")
print(brother)

ugly_troll.grunt()
brother.grunt()

vamp1 = Vampyre("vamp1")
print(vamp1)

print("*" * 40)
while vamp1.alive:
    vamp1.take_damage(5)
    print(vamp1)

vampK = VampyreKing('suresh')
print(vampK)
vampK.take_damage(10)
print(vampK)