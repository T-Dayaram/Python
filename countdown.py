import random
import time

littles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
bigs = [25, 50, 75, 100]



while True: 
    try: bigschoice = int(input("How many big numbers? (up to 4): \n"))
    
    except ((if bigschoice > 4)):
        print("No more than 4. Try again please.")
        continue
    leftover =str(6 - bigschoice)
    littleschoice = int(input("How many little numbers? No more than: "+ (leftover) +".\n"))    

    if(littleschoice > (6 - bigschoice)):
        print("No more than "+ bigschoice + ". Try again please.")
    else:
        break

for i in range(bigschoice):
    print(random.choice(bigs), end="   ")

for i in range(littleschoice):
    print(random.choice(littles), end="   ")

print("\nAnd the target:", end="    ")
print(random.randint(100,999))

#for x in reversed(range(1, 31)):
#    print(x)
#    time.sleep(1);