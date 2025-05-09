import random


while True:
    choice =input("Roll the dise (y/n): ").lower()
    if choice == 'y' :
            dic1 = random.randint(1,6)
            dic2 = random.randint(1,6)
            print(f" {dic1} , {dic2}")

    elif choice == "n":
         print("thanks for playing")
         break
    else:
          print("invalid choice")