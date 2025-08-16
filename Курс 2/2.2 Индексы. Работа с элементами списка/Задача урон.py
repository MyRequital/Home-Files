dragon = 120
vampyr = 110
troll = 30
mag = 30
ciclope = 100

damage = [["dragon", dragon], ["vampyr", vampyr], ["troll", troll], ["mag", mag], ["ciclope", ciclope]]

for monster in damage:
    print(f"Имя монстра: {monster[0]}, урон монстра {monster[1]}")
    if monster[1] < 100 and monster[0] != "mag":
        monster[1] += mag
print("-" * 40,
      "\nИзмененный урон монстров\n",
      "-" * 40)
for i in damage:
    print(f"Имя монстра: {i[0]}, Урон монстра: {i[1]}")
    print("*" * 40)