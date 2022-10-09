#2) Є дев'ятиповерхівка, в якій 4 під'їзда. Номер під'їзда починається з одиниці.
#На одному поверсі 4 квартири. Напишитб програму яка, отримає номер квартири з клавіатури,
#та виведе на екран, на якому поверсі, в якому під'їзді розташована ця квартира.
#Якщо цієї квартири немає в цьому будинку, то теба повідомити про це користувачеві

floors = 9
entrances = 4
floor_flats = 4
number_flat = int(input("Input number of flat: "))

flats_entr1 = floor_flats * floors

if number_flat > entrances * floors * floor_flats or number_flat <= 0:
    print("There is no such flat in this house!")
else:
    entr = (number_flat - 1) // flats_entr1 + 1
    floor = ((number_flat - 1) - flats_entr1 * (entr - 1) ) // floor_flats + 1
    
    #if number_flat % flats_entr1 == 0:
        #entr = number_flat // flats_entr1
    #else:
        #entr = number_flat // flats_entr1 + 1
    #if number_flat % floor_flats == 0:
        #floor = (number_flat - flats_entr1 * (entr - 1) ) // floor_flats
    #else:
        #floor = (number_flat - flats_entr1 * (entr - 1) ) // floor_flats + 1
    print("Your flat in the ",entr," entrance on the ",floor," floor")
    
