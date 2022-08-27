#!/usr/bin/python3

#For random related functions
import random

#For time related functions
import time

#Simulating dates because some people need the practice.

#After a delay print
def DelayPrint(Text,Delay,LineEnd):
    time.sleep(Delay)
    print(Text, flush=True, end = LineEnd)

#Return the first names of everyone from Cohort 3
def GetPeopleNames():
    #Open the first
    NFile = open('first names.txt','r')
    #Read the file and put every line into a list
    Names = NFile.read().splitlines()
    #Close the file
    NFile.close()
    #return the list
    return Names

#The Mcdonalds resturant data
def Getmcdonalds():
    return {
        "name": "MC Donalds",
        "price": "$",
        "travelcost": 0,
        "tip": 0,
        "menu": [{"item": "Fries","cost": 4},{"item": "4 Piece Nuggets","cost": 2},{"item": "Big Mac","cost": 5},{"item": "Milkshake","cost": 4}]
    }

#The Dunkin Donuts resturant data
def Getdunkindonuts():
    return {
        "name": "Dunkin Donuts",
        "price": "$",
        "travelcost": 15,
        "tip": 0,
        "menu": [{"item": "2 Donuts","cost": 4},{"item": "Coffee","cost": 1.50},{"item": "Iced Coffee","cost": 2},{"item": "Frozen Coffee","cost": 3}]
    }

#The Olive Garden resturant data
def Getolivegarden():
    return {
        "name": "Olive Garden",
        "price": "$$",
        "travelcost": 20,
        "tip": .15,
        "menu": [{"item": "Pasta","cost": 13},{"item": "Cheese Cake Slice","cost": 9},{"item": "Iced Coffee","cost": 2},{"item": "Alfredo","cost": 0,"sub": [{"item": "Chicken","cost": 19.50},{"item": "Shrimp","cost": 21},{"item": "Fettuccine","cost": 16},{"item": "Seafood","cost": 22}]}]
    }

#Some feelings
def Getfeelings():
    #List of feelings
    return ['terrible','bad','okay','good','excellent']

#Ask for the user's first name
def GetUser():
    #Ask for the user's first name
    return input("What is your first name? ")

#Ask for the user's money they are carrying
def GetMoney():
    #converting to int can fail and crash the program so just assume they are broke instead
    try:
        #Ask how much money the user has and convert it to int
        Money=int(input("Around how much money do you have with you?(Number Only) "))
        #Tell the user how much they have
        print("You have $"+str(Money),"with you.")
        return Money
    except:
        #User entered something that is not a int so assume they have no money
        print("Oh so you are broke then...with $0")
        return 0

#Yes or no Prompt
def YNPromt(Prompt):
    UserInput=input(Prompt+" Y/N: ")
    if UserInput[0].lower() == "y":
        return True
    elif UserInput[0].lower() == "n":
        return False
    else:
        print("Did not understand that assuming no.")
        return False

#Welcome the user and get some information from them
def Welcome(PeopleNames):
    #Welcome message
    print("Welcome to a Blind Date to Remeber Cohort 3 Edition.")
    #Get the user's first name
    User=GetUser()
    #Welcome the user using their first name
    print("Hello,",User,"get ready for your bind date!")
    #Ask how much money they are carrying
    Money=GetMoney()
    #Ask if user is part of cohort 3
    Cohort3Member=YNPromt("Are you a member of Cohort 3?")
    if Cohort3Member:
        #Special message for Cohort 3 members
        print("Enjoy your date with your classmate!")
        #Remove the user from the list of people, No dating yourself allowed
        PeopleNames.remove(User)
    #Randomly select a blind date for the user
    BlindDate=random.choice(tuple(PeopleNames))
    #return the data gathered as a list
    return [User,Money,Cohort3Member,BlindDate]

#Function to give a user a prompt and a list of options to select using a number
def Pick(Prompt, List):
    #Print the prompt
    print(Prompt)
    #A index to count the position the loop is at
    Index = 0
    #Loops throught he list of items
    for Item in List:
        #Prints the current index offset by 1 and the current dict from the list using the Identifier to name the item
        print(str(Index+1)+'. '+Item)
        #Increases the Index by 1
        Index+=1
    #Get the users selection
    UserInput = input("#> ")
    try:
        #Convert input to int
        UserSelection=int(UserInput)
    except:
        #User entered something that is not a int so assume they have no money
        print("I didn't understand that so lets go with the first one")
        UserSelection = 1
    #Remove 1 to correct it
    UserSelection-=1
    #If user selected out of bounds pick the first thing but if it's okay return their selection
    if UserSelection > len(List)-1 or UserSelection < 0:
        print("Your selection does not seem right let me pick for you then")
        return 0
    else:
        return UserSelection

#Returns a list of values from a list of dictionaries using a identifier
#Can go down a level if it finds a sub dictionary to find find sub items of a main item
def ListofDictVal(DictList,Identifier,Sub=False):
    #The final list to return
    List=[]
    #Go through the list of dictionaries
    for Item in DictList:
        #Ignore everything but dictionaries in the list
        if isinstance(Item,dict):
            #If the Sub flag is true check for the sub key in the keys list to see if there is a sub dictionary list
            if Sub and "sub" in Item.keys():
                #We have a sub entry
                #Check if the thing we are searching for is in the keys list on the main layer
                if Identifier in Item.keys():
                    #Found it, this is the main item from the main layer
                    MainItemVal = Item[Identifier]
                #Go through the sub entry list of dictionaries
                for SubItem in Item["sub"]:
                    #Check if the thing we are searching for is in the keys lists on the sub layer
                    if Identifier in SubItem.keys():
                        #Found it, this is the sub item from the sub layer
                        SubItemVal = SubItem[Identifier]
                    #If we have a main and sub item it's time to combine it to make a new item
                    if MainItemVal != None and SubItemVal != None:
                        #Spacer that makes it easier to combine two numbers
                        Spacer = 0
                        #If the main item value is a string use a space as the spacer instead to combine strings
                        if isinstance(MainItemVal,str):
                            Spacer = " "
                        #Combine and add to the final list
                        List.append(MainItemVal+Spacer+SubItemVal)
            #This is if there is no sub layer and it was found on the main layer so just addd it
            elif Identifier in Item.keys():
                List.append(Item[Identifier])
    #Return the final list
    return List

#Order at a resturant
def Order(Resturant):
    #List of the menu item names
    Items = ListofDictVal(Resturant["menu"],"item",True)
    #List of the the menu item prices
    Prices = ListofDictVal(Resturant["menu"],"cost",True)
    #List of the menu with item names and prices goes here
    Menu=[]
    #List of the items user orders goes here, represented by array indexes
    YourOrder=[]
    #List of the items the date orders goes here, represented by array indexes
    YourDatesOrder=[]
    #The total of the users order before tip
    YourTotal=0
    #The total of the dates order before tip
    YourDatesTotal=0
    #The total cost of everything goes here including tip
    Total=0
    #The percentage of the tip to be added to the bill
    TipPercent=Resturant["tip"]
    #Create the menu with the item name and the prices
    for Index in range(0,len(Items)-1):
        Item=Items[Index]
        if Prices[Index] == 0:
            Price = "$*"
        else:
            Price = "$"+str(Prices[Index])
        Menu.append(Item+" "+Price)
    #Option to finish ordering
    Menu.append("Done Ordering")
    #Option to redo the order
    Menu.append("Redo Order")
    #While loop to handle ordering
    while True:
        Choice=Pick("What Items would you like to order?",Menu)
        if Menu[Choice] == "Done Ordering":
            break
        elif Menu[Choice] == "Redo Order":
            YourOrder = []
        else:
            YourOrder.append(Choice)
        print("Your order so far is: ")
        for Selection in YourOrder:
            print(Menu[Selection])
    #The final items ordered by the user
    print("Your final order is: ")
    for Selection in YourOrder:
        YourTotal += Prices[Selection]
        print(Menu[Selection])
    #Randomly select a random number of items the date orders and show their final order
    print("Your date's final order is: ")
    for Index in range(0,random.randint(0,6)):
        Selection = random.randint(1,len(Items)-1)-1
        YourDatesOrder.append(Selection)
        YourDatesTotal += Prices[Selection]
        print(Menu[Selection])
    #Assign the total to the combined total of the user and the date
    Total = YourTotal+YourDatesTotal
    #print("Your Total: ",YourTotal)
    #print("Dates Total: ",YourDatesTotal)
    #print("Total Before Tip: ",Total)
    #Add in the tip to the total
    Total = Total + Total*TipPercent
    #print("Total with Tip: ",Total)
    #Return the total
    return Total

#The main function
def main():
    #List of the first names of people in cohort 3
    PeopleNames=GetPeopleNames()
    #List of the resturant choices
    Resturants=[Getmcdonalds(),Getdunkindonuts(),Getolivegarden()]
    #List of feelings
    Feelings=Getfeelings()
    #If the user wants to run away from the blind date when there is a chance to run
    UserRunFromDate=False
    #If the blind date wants to run away from the user when there is a chance to run
    BlindDateRunFromDate=False
    #The options to pay the bill
    PayOptions = []
    #Welcome function and the data it returns
    WelcomeData=Welcome(PeopleNames)
    #The user's first name from the welcome data
    User=WelcomeData[0]
    #The user's money from the welcome data
    Money=WelcomeData[1]
    #The randomly selected first name of the date from the welcome data
    BlindDate=WelcomeData[3]


    #Hardcoding for Testing
    #The user's first name from the welcome data
    #User="Richard"
    #The user's money from the welcome data
    #Money=100
    #The randomly selected first name of the date from the welcome data
    #BlindDate="Someone"


    #Select the resturant the date was planned at
    Resturant=Resturants[Pick("Which Resturant is your date at?(Number Only)",ListofDictVal(Resturants,"name"))]
    #telling the user their resturant selection
    print("Lets go to",Resturant["name"],"to meet your blind date!")
    #Gets the cost of the ride
    RideCost=Resturant["travelcost"]
    #Check if the user has enought to get to the resturant
    if RideCost > Money:
        #The cost to get to the resturant is more than the user has money so the date ends
        print("Hold on, "+User+" it seems you don't have enough money to get to your date...")
        #Tell the user they stood up their date and reveal them dramatically!
        DelayPrint("Your date ends here, you won't get a second date from standing up...",5,"\n")
        DelayPrint(BlindDate+'...',5,"\n")
        exit(1)
    else:
        #User has enought money so spend it
        print("Spent $"+str(RideCost)+" to get to",Resturant["name"])
        Money-=RideCost



    #Tell the user they arrived at the resturant and reveal their date dramatically
    print("You arrived at",Resturant["name"],"and meet your blind date...")
    DelayPrint("Your eyes meet and you see...",5,"\n")
    DelayPrint(BlindDate+'...',5,"\n")
    


    #This is the chance where someone runs
    DateFeels=random.choice(tuple(Feelings))
    UserFeels=Feelings[Pick("How do you feel knowing your blind date is "+BlindDate+"?",[Feeling.capitalize() for Feeling in Feelings])]
    print("After learning",BlindDate,"is your blind date you feel",UserFeels+".")
    #If the user feels terrible ask if they want to run away
    if UserFeels == Feelings[0]:
        #Ask if user wants to run away
        UserRunFromDate=YNPromt("Do you want to run away from this date?")
    #If the blind date feels terrible check if they want to run away
    if DateFeels == Feelings[0]:
        #Date is running at the first chance
        BlindDateRunFromDate=True
    #Check if someone is running from the date
    if UserRunFromDate and BlindDateRunFromDate:
        #What to do to runaway from a date
        print("You go to the bathroom...")
        #Run into your blind date when running away
        DelayPrint("When you reach the bathroom you bump into "+BlindDate+"...",5,"\n")
        #first akward meeting
        DelayPrint("...you both stare at eachother awkwardly and you go in first...",5,"\n")
        #Does this work in real life?
        DelayPrint("You climb through a window and run all the way home without looking back...",5,"\n")
        #second akward meeting
        DelayPrint("As you take a break from running you see someone running nearby...",5,"\n")
        #Eyes meet
        DelayPrint("Your eyes meet and you see...",5,"\n")
        DelayPrint(BlindDate+'...',5,"\n")
        #Wordess communication
        DelayPrint("...you both stare at eachother in shock and disbelief...then at the same time you both wordless run in opposite directions...",5,"\n")
        #No second date for you or your blind date, pretend this never happened
        DelayPrint("Your date ends here, you and "+BlindDate+" won't get a second date and will pretend this never happened.",5,"\n")
        exit(1)
    elif UserRunFromDate:
        #What to do to runaway from a date
        print("You go to the bathroom...")
        #Does this work in real life?
        DelayPrint("You climb through a window and run all the way home without looking back.",5,"\n")
        #No second date for you
        DelayPrint("Your date ends here, you won't get a second date from ditching "+BlindDate+".",5,"\n")
        exit(1)
    elif BlindDateRunFromDate:
        #What they did to runaway from a date
        print("You go to the table you saw "+BlindDate+" at...")
        #It's always the bathroom
        DelayPrint("When you reached the table they were gone...you saw them enter the bathroom...",5,"\n")
        #The tradgedy
        DelayPrint("You wait for them to come back but they never did...they never left the bathroom...",5,"\n")
        #Feels bad
        DelayPrint("Tired of waiting you lose your appetite and walk home...",5,"\n")
        #Sad
        DelayPrint("As you were walking home it suddenly starts to rain...you didn't bring a umbrella...",5,"\n")
        #No second date for you
        DelayPrint("Your date ends here, safe to say you won't get a second date from "+BlindDate+".",5,"\n")
        exit(1)


    #Meet your date
    print("You go to the table you saw "+BlindDate+" at...")
    #Greetings
    DelayPrint("After greetings and small talk you look at the menu.",5,"\n")
    #You and your date order your meals and the bill is calculated
    Bill=Order(Resturant)


    #Grace or prayer before eating
    DelayPrint("After ordering and waiting your meal arrives.",5,"\n")
    DelayPrint("Before you and "+BlindDate+" eat your meals...you must say...",5,"\n")
    DelayPrint("Rub-a-dub-dub...",5,"\n")
    DelayPrint("Thanks for the Grub...",5,"\n")
    DelayPrint("Then you two eat and finish your meals...",5,"\n")



    #This is where we reevaluate the date so far
    DateFeels=random.choice(tuple(Feelings))
    UserFeels=Feelings[Pick("How do you feel now about your date with "+BlindDate+"?",[Feeling.capitalize() for Feeling in Feelings])]
    print("After spending some time on your date with",BlindDate,"you now feel",UserFeels+".")



    #Create the bill paying options available based on the users money
    if Bill < Money:
        PayOptions.append("You cover the bill")
    if Bill/2 < Money:
        PayOptions.append("You spit the bill with your date")
    PayOptions.append("Your date covers the bill")


    #Paying the bill then check how much money the user has then go home
    DelayPrint("As your date comes to the end the bill arrives...",5,"\n")
    DelayPrint("When you glance at the bill you see it's $"+str(Bill)+"...",5,"\n")
    DelayPrint("You remember you have $"+str(Money)+"...",5,"\n")
    PayMethod=PayOptions[Pick("What will you do to pay?",PayOptions)]
    if PayMethod == "You cover the bill":
        #User pays the full bill
        print("You cover the bill of $"+str(Bill)+".")
        Money-=Bill
    elif PayMethod == "You spit the bill with your date":
        #User pays half the bill, splitting it with the date
        print("You split the bill of $"+str(Bill)+" with",BlindDate,".")
        Money-=Bill/2
    elif PayMethod == "Your date covers the bill":
        #Date pays the full bill
        print("Your date",BlindDate,"covers the bill of $"+str(Bill)+".")
    #Round the users money to 2 digits
    Money=round(Money,2)
    #Print out how much money the user has
    DelayPrint("After this date you have $"+str(Money)+" left.",5,"\n")
    DelayPrint("The date ends and you both go home.",5,"\n")



    #The Future of the user and the blind date based on this date
    if UserFeels == "terrible":
        #User feels terrible so no second date
        DelayPrint("You did not enjoy your date with "+BlindDate+".",5,"\n")
        DelayPrint("You won't do a second date with "+BlindDate+".",5,"\n")
        exit(1)
    elif UserFeels == "bad":
        if PayMethod == "Your date covers the bill":
            #User feels bad but didn't pay so may want a second date
            DelayPrint("You did not enjoy your date with "+BlindDate+".",5,"\n")
            DelayPrint("You may want to do a second date with "+BlindDate+".",5,"\n")
        else:
            #User feels bad and paid for it so no second date
            DelayPrint("You did not enjoy your date with "+BlindDate+".",5,"\n")
            DelayPrint("You won't do a second date with "+BlindDate+".",5,"\n")
            exit(1)
    elif DateFeels == "terrible":
        #Date feels terrible so no second date
        DelayPrint("It seems like "+BlindDate+" did not enjoy the date with you.",5,"\n")
        DelayPrint(BlindDate+" won't do a second date with you.",5,"\n")
        exit(1)
    elif DateFeels == "bad":
        if PayMethod == "You cover the bill":
            #Date feels bad but didn't pay so may want a second date
            DelayPrint("It seems like "+BlindDate+" did not enjoy the date with you.",5,"\n")
            DelayPrint(BlindDate+" may want to do a second date with you.",5,"\n")
        else:
            #Date feels bad and paid for it so no second date
            DelayPrint("It seems like "+BlindDate+" did not enjoy the date with you.",5,"\n")
            DelayPrint(BlindDate+" won't do a second date with you.",5,"\n")
            exit(1)
    else:
        #Both the user and the date feels good enough for a second date
        DelayPrint("It seems like you and "+BlindDate+" enjoyed the date.",5,"\n")
        DelayPrint("There is a second date in your futures.",5,"\n")



#Run the main function
main()