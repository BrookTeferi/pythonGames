import random
import time
#The Color Choice Game(CCG)
def CGC():
    countuser=0
    countpc=0
    while True:
        print(15*'*' + "    WELCOME TO COLORS CHOICE GAME   "+ 15*'*')
        print(" PLEASE CHOOSE a colour of your choice from the list below")
        print(' Red=1 \n' + ' Yellow=2 \n' + ' Orange=3 \n' + ' Green=4 \n' + ' Blue=5 \n' + 'EXIT GAME=0 \n' )
        user_input=input(" PLEASE INSERT YOUR CHOICE:")
        print( "YOUR CHOICE : "+ str(user_input))
        if str(user_input)=="0":
            print("EXITING GAME!!!!!!!!!!!!!!")
            break
        time.sleep(1)
        PC_Random = int(random.randrange(1, 6))
        print("COMPUTER CHOICE : " + str(PC_Random))

        if int(user_input)> int(PC_Random):
            if int(user_input)< 6:
                countuser=countuser+1
                print("User score : " + str(countuser))
                print("COMPUTER score : " + str(countpc))
        elif int(user_input)< int(PC_Random):
            countpc = countpc + 1
            print("User score : " + str(countuser))
            print("COMPUTER score : " + str(countpc))
        elif int(user_input)== int(PC_Random):
            print("ITS A TIE")
        else:
            print(" PLEASE INSERT FROM THE LISTED VALUE")



CGC()