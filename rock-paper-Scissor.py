# rock paper scissor
# take r p or s as input
# computer is the oponnent
# winner gets 1 point
# tries 10 times
# who scores higher wins
def main():
    import random
    i = 0
    myp1 = 0
    comp1 = 0
    while(i<10):
        lst1 = ("rock","paper","scissor")
        compch1 = random.choice(lst1)
        while(1):
            mych1 = input("Enter r for rock p for paper s for scissor\n")
            if mych1 == "r" or mych1 == "p" or mych1 == "s":
                if (compch1 == "rock" and mych1 == "s") or (compch1 == "scissor" and mych1 == "p") or (compch1 =="paper" and mych1 =="r"):
                    comp1 = comp1+1
                    print(f"Computer chose {compch1} \t computer gets the point")
                elif (compch1 == "scissor" and mych1 == "r") or (compch1 == "paper" and mych1 == "s") or (compch1 =="rock" and mych1 =="p"):
                    myp1 = myp1+1
                    print(f"Computer chose {compch1} \t you get the point")
                else:
                    print(f"Computer chose {compch1} \t no one gets the point")
                break
            else:
                print("Wrong input try again")
                continue
        i = i + 1
    if myp1 > comp1:
        print(f"Your points {myp1}\nComputer points {comp1}\nCongratulations you win")
    elif myp1 < comp1:
        print(f"Your points {myp1}\nComputer points {comp1}\nHehehe looser You can't beat the computer")
    else:
        print(f"Your points {myp1}\nComputer points {comp1}\nDamn we are tied")
    a = input("Wanna play again y for yes n for no")
    if a == "y":
        main()
    else:
        exit()
main()






