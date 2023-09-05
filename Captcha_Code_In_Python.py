import datetime
import random
lower_alphabet="abcdefghijklmnopqrstuvwxyz"
upper_alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols="`~!@#$%^&*()_-+={[}]|\:;<,>.?/ "
digits="0123456789"
Captcha_Code=""
total="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+={[}]|\:;<,>.?/ 0123456789"
i=0
index=0
high_score_easy=0
high_score_medium=0
high_score_hard=0
high_score_custom=0
inventory=[]
Five_Captcha_Code=0
Perfect_Test=0
Open_Inventory=0
Perfect_Test_Easy=0
Perfect_Test_Medium=0
Perfect_Test_Hard=0
Perfect_Test_Custom=0
correct=0
wrong=0
five_test=0
refresh_inventory=0
Character=0
Characters_Custom=0
High_Score_Check=0
tests_taken=0
captcha_made=0
def test(good,bad,Mode,high_score,Loop,place,Codes,combined,Perfect_T,Perfect,tests,Characters=Characters_Custom,least=0,most=0):
    good=0
    bad=0
    print(Mode, "Mode High Score:", high_score,"%")
    for i in range(Loop):
        if(Mode!="Custom"):
            Characters=random.randrange(least,most)
        else:
            Characters=Characters_Custom
        for i in range(Characters):
            place=random.randrange(0,94)
            Codes=Codes+combined[place]
        print(Codes)
        answer=input("Enter this Captcha Code, ")
        if(answer==Codes):
            print("Correct Answer!")
            good=good+1
            print("You have gotten", good,"correct out of", good+bad, "questions since so far which is", good/(good+bad)*100,"% accuracy")
            Codes=""
        else:
            print("Wrong Answer!")
            bad=bad+1
            print("You have gotten", good,"correct out of ",good+bad, "questions since so far which is", good/(good+bad)*100,"% accuracy")
            Codes=""
    if(good>high_score):
        high_score=good
        print("New", Mode, "Mode High Score:", good/(good+bad)*100,"%")
    if(good/(good+bad)*100==100):
        print("Great Job! You are the Captcha Captain! 100% accuracy!")
        if(Perfect_T<100):
            Perfect_T=Perfect_T+100
            print("Achievement Cleared: Get 100% In Any Test")
        if(Perfect<100):
            Perfect=Perfect+100
            print("Achievement Cleared: Get 100% In Any", Mode, "Test")
    elif(80<=good/(good+bad)*100<100):
        print("Good Job! You will go perfect next time!", good/(good+bad)*100,"% accuracy!")
    elif(60<=good/(good+bad)*100<80):
        print("Good Try! Do not worry, you still got more than 50%!", good/(good+bad)*100,"% accuracy!")
    elif(40<=good/(good+bad)*100<60):
        print("It is okay! You can do better!", good/(good+bad)*100,"% accuracy!")
    elif(20<=good/(good+bad)*100<40):
        print("At least you got some correct!", good/(good+bad)*100,"% accuracy!")
    else:
        print("Either you are not that good at Captcha Codes or you are a robot!", good/(good+bad)*100,"% accuracy!")
    tests=tests+1
while True:
    print("The date is", datetime.date.today())
    print("1. Create a number of Captcha Codes")
    print("2. Take a quiz to make sure you are not a robot")
    print("3. See your inventory of Captcha Codes")
    print("4. See your achievements")
    print("5. See Your Stats")
    print("6. Exit")
    choice=int(input("Enter your choice "))
    if(choice==1):
        Loop=int(input("How many Captcha Codes would you like to make? "))
        if(Loop<1 or Loop%1!=0):
            print("Invalid Input")
        else:
            for i in range(Loop):
                Characters=int(input("How many characters do you want there to be in your Captcha Code? "))   
                if(Characters<1 or Characters%1!=0):
                    print("Invalid Input")
                else:
                    for i in range(Characters):
                        index=random.randrange(0,92)
                        Captcha_Code=Captcha_Code+total[index]
                    print("Your Captcha Code is", Captcha_Code)
                    captcha_made=captcha_made+1
                    inventory.append(Captcha_Code)
                    if(Five_Captcha_Code<100):
                        Five_Captcha_Code=Five_Captcha_Code+20
                        if(Five_Captcha_Code==100):
                            print("Achievement Cleared: Make 5 Captcha Codes")
                    Captcha_Code=""
                    
    elif(choice==2):
        while True:
            print("1. Easy Mode")
            print("2. Medium Mode")
            print("3. Hard Mode")
            print("4. Custom Game")
            choice_mode=int(input("Enter your choice "))
            if(choice_mode==1):
                test(correct,wrong,"Easy",high_score_easy,3,index,Captcha_Code,total,Perfect_Test,Perfect_Test_Easy,tests_taken,Character,5,7)
                break
            elif(choice_mode==2):
                test(correct,wrong,"Medium",high_score_medium,5,index,Captcha_Code,total,Perfect_Test,Perfect_Test_Medium,tests_taken,Character,7,9)
                break
            elif(choice_mode==3):
                test(correct,wrong,"Hard",high_score_hard,7,index,Captcha_Code,total,Perfect_Test,Perfect_Test_Hard,tets_taken,Character,9,11)
                break
            elif(choice_mode==4):
                Loop_Custom=int(input("Enter how many Captcha Codes you would like there to be? "))
                Characters_Custom=int(input("Enter how long you would like the Captcha Codes to be? "))
                test(correct,wrong,"Custom",high_score_custom,Loop_Custom,index,Captcha_Code,total,Perfect_Test,Perfect_Test_Custom,tests_taken)
                break
            else:
                print("Invalid Input")
    elif(choice==3):
        if(Open_Inventory<100):
            Open_Inventory=Open_Inventory+100
            print("Achievement Cleared: Open your inventory")
        print("Here is your inventory:")
        for i in inventory:
            print("   ",i)
        print()
        while True:
            print("1. Refresh")
            print("2. Exit")
            choice_2=int(input("Enter your choice "))
            if(choice_2==1):
                list=[]
                print("List Refreshed")
                if(refresh_inventory<100):
                    refresh_inventory=refresh_inventory+100
                    print("Achievement Cleared: Refresh Inventory")
                break
            elif(choice_2==2):
                break
            else:
                print("Invalid Input")

    elif(choice==4):
        print("Make 5 Captcha Codes:", end=" ")
        if(Five_Captcha_Code==100):
            print("Complete")
        else:
            print(Five_Captcha_Code,"%", "Complete")

        print("Get 100% In Any Test:", end=" ")
        if(Perfect_Test==100):
            print("Complete")
        else:
            print(Perfect_Test,"%", "Complete")

        print("Open Your Inventory:", end=" ")
        if(Open_Inventory==100):
            print("Complete")
        else:
            print(Open_Inventory,"%", "Complete")

        print("Refresh Your Inventory:", end=" ")
        if(refresh_inventory==100):
            print("Complete")
        else:
            print(refresh_inventory,"%", "Complete")

        print("Get 100% In Any Easy Test:", end=" ")
        if(Perfect_Test_Easy==100):
            print("Complete")
        else:
            print(Perfect_Test_Easy,"%", "Complete")

        print("Get 100% In Any Medium Test:", end=" ")
        if(Perfect_Test_Medium==100):
            print("Complete")
        else:
            print(Perfect_Test_Medium,"%", "Complete")

        print("Get 100% In Any Hard Test:", end=" ")
        if(Perfect_Test_Hard==100):
            print("Complete")
        else:
            print(Perfect_Test_Hard,"%", "Complete")

        print("Get 100% In Any Custom Test:", end=" ")
        if(Perfect_Test_Custom==100):
            print("Complete")
        else:
            print(Perfect_Test_Custom,"%", "Complete")

        print("See Your High Scores In The Tests:", end=" ")
        if(High_Score_Check==100):
            print("Complete")
        else:
            print(High_Score_Check,"%", "Complete")

    elif(choice==5):
        print("Easy Mode High Score:", high_score_easy)
        print("Medium Mode High Score:", high_score_medium)
        print("Hard Mode High Score:", high_score_hard)
        print("Custom Mode High Score:", high_score_custom)
        print("Captcha Codes Made:", captcha_made)
        print("Tests Taken:", tests_taken)
    elif(choice==6):
        leave=input("Are you sure you would like to leave? Warning: Variables and Values will not be saved ")
        leave=leave.lower()
        if(leave=="yes"):
            print("Bye! Have a great day")
            break
        elif(leave=="no"):
            odd=odd
            even=even
        else:
            print("Invalid Input. Please Try Again!")
    else:
        print("Invalid Input. Please Try Again!")
        
       
