#-----------------------------#
# Summative - Shopping List
# Reid A. Martin
# 6 October 2021
#-----------------------------#

import time


##--Lists--##

items = [] #blank lists
prices = []

##--Functions--##
    
def print_lists():
    print("\n\nHere is your list!\n-------------")
    for i in range(len(items)):
        print("You need to buy", items[i], ", and that costs $",prices[i]) #for the length of the list, it will print the item and the price
    total_cost()

def total_cost():
    total = 0
    for i in range(len(prices)):
        total = sum(prices)
    print(f"\nThe total cost is ${total}") #Adds together the prices to deliver a total cost
    
def add_item(): #Adds item to list
    add = input("What would you like to add?\n>")
    if add not in items: #if item isn't already in there it adds it and takes you further
        items.append(add)
        price_add = int(input("What is the price?\n>"))
        prices.append(price_add)
    elif add in items: # if the item is already in the list, it boots you to the menu
        print("That is already in your list!")
    
def remove_item(): #removes item that you type in, and the price that you also type in 
    print_lists() #If the item or price don't exist you get booted to menu
    remove = input("What would you like to remove?\n>")
    if remove in items:
        price_remove = float(input("How much does the item cost?\n>"))
        if price_remove in prices:
            items.remove(remove)
            prices.remove(price_remove)
        else:
            print("nice try bucko")
    else:
        print("Ya... That's not in there...")
    
    
def clear_list(): #clears the lists
    items.clear()
    prices.clear()
    print("List Cleared!")
    
def leave_prog(): #says goodbye
    print("\n\nThanks for using the shopping list!")
    time.sleep(2)
    print_lists()
    time.sleep(3)
    print("Goodbye!")

    
##--Main Code--##


while 1:
    choose_menu = input("\nWhat would you like to do? Add - 1, Remove - 2, Print - 3, Clear List - 4, Leave - 5\n>").lower()
    #main menu, let people input what they want to do, and changes any text input to lowercase for easier commands
    if choose_menu == "1" or choose_menu == "add": #triggers add item
        add_item()
    elif choose_menu == "2" or choose_menu == "remove":#triggers remove
        remove_item()
    elif choose_menu == "3" or choose_menu == "print": #triggers print list
        print_lists()
    elif choose_menu == "4" or choose_menu == "clear list": # triggers clear list
        clear_list()
    elif choose_menu == "5" or choose_menu == "leave": #triggers leave program
        leave_prog()
        break
    else:
        print("Huh?") #so you can't break the menu
        
        
