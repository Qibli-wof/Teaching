#in this task you must create a python application for inventory, it must create a list of things and then let you keep track of how many there are of each thing, 
#letting you update the count and seeing it along the oher tools
#your set of tools will be: keyboards, bottles, tea packets, coffee beans, commits.

#afterwards your work will be graded and tested, good luck


#teachers example:


items_dict = {
"keyboards": 0,
"commits": 0,
"tea packets": 0,
"bottles": 0,
"coffee beans": 0
}

# above is self explanitory, creates a directory with the following values

option = 0
items_option = ""
items_value = int() #will make the value be null, essentially empty but still be assigned as a intiger

#above this the option value is 0 instead of null with as in items_value becouse in items_value 0 could be used as a value whereas in option 0 will not be used
#allowing for more troubleshooting

def clear():
        print("\n" *50)
#a dirty way to clear the screen by flooding it with new empty lines, a better way would be to accsess the od to send clear messages but that would be os dependant
#forcing me to add detection for os and different solution for each one, and im just too lazy for that
#TODO: add os level clear message

def ask():
        print("pick a option \n")
        print("1: display options")
        print("2: change or add value in database")
        print("3: exit \n")
        global option
        option = input("")
#asks the user about selecting a option, the global value is added so the function can accsess it

def change_dict():
        print(items_dict)
        items_option = input("what item would you like to change, or would like to add? \n")
        items_value = input("and what shall be the new value of this item? \n")
        items_dict[items_option] = items_value
        clear()
#prints out the dictionary contents and asks about a name and a value, passing that onto the dictionary


#the actual stuff that runs starts here

ask() # calls the function above, obviusly

while(option != "3"):          #the while here is so it will stop if the value is 3, 3 is set for exiting
        if(option == "1"):     #the " marks for the numbers are used becouse the input() always spews out info in a string, i could convert it to a int to make it look a bit cleaner tho
                clear()        #TODO: turn input() output into int if it is one, before checking its number
                ask()
        elif(option == "2"):
                clear()
                change_dict()
                ask()
        elif(option == "0"):
                clear()
                print("error: option value not changed (0)")
                ask()
        else:
                clear()
                print("error: option value out of bounds (0-3)")
                ask()




