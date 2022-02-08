wizard = "Wizard"
elf = "Elf"
human = "Human"
dragon = "Dragon"
orc = "Orc"

hp_wizard = 70
hp_elf = 100
hp_human = 150
hp_orc = 180
hp_dragon = 300

dmg_wizard = 150
dmg_elf = 100
dmg_human = 20
dmg_orc = 80
dmg_dragon = 50

print("1)   Wizard")
print("2)   Elf")
print("3)   Human")
print("4)   Orc")


while True:
    character = input("Choose your character:")

    if character == "1":
        character = wizard
        my_hp = hp_wizard
        my_dmg = dmg_wizard
        print("You are a wise Wizard!")
        break
    elif character == "2":
        character = elf
        my_hp = hp_elf
        my_dmg = dmg_elf
        print("You are a swift Elf!")
        break
    elif character == "3":
        print("You are a humble Human!")
        character = human
        my_hp = hp_human
        my_dmg = dmg_human
        break
    if character == "4":
        character = orc
        my_hp = hp_orc
        my_dmg = dmg_orc
        print("You are a proud Orc!")
        break
    else:
        print("Please make a valid selection of 1 (Wizard), 2 (Elf), 3 (Human), or 4 (Orc).")

print("You have " + str(my_hp) + " health-points (HP).")
print("Your hits have " + str(my_dmg) + " damage points.")

while True:
    hp_dragon = hp_dragon - my_dmg
    print("The ", character, " damaged the Dragon!")
    print("The Dragon has ", hp_dragon, " HP left!")
    
    if hp_dragon <= 0:
        print("You have slain the Dragon!")
        break    
    
    my_hp = my_hp - dmg_dragon
    print("The ", dragon, " damaged you!")
    print("You have ", my_hp, " HP left!")


    if my_hp <= 0:
        print("You have been slain by the Dragon!")
        break
