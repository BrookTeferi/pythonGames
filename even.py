

n = int(input().strip())
if( n % 2 == 0 ):
    if (n > 20):
        print(" Not Weird")
    elif(n > 1 and n < 6):
        print(" Not Weird")
    elif (n > 5 and n < 21):
        print("Weird")
else:
    print("Weird")




