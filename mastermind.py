from random import randint

n1 = randint(1,6)
n2 = randint(1,6)
n3 = randint(1,6)
n4 = randint(1,6)
c = 1

print("type a number from 1 to 6")
print()

while True:
    
    guess1 = int(input("guess the first number: "))
    print()
    guess2 = int(input("guess the second number: "))
    print()
    guess3 = int(input("guess the third number: "))
    print()
    guess4 = int(input("guess the fourth number: "))
    print()
   
    numberswrong = 0

    if guess1 != n1:

        numberswrong += 1

    if guess2 != n2:

        numberswrong += 1

    if guess3 != n3:

        numberswrong += 1

    if guess4 != n4:

        numberswrong += 1

    if numberswrong == 0:

        print()
        print('Well Done!')
        print('It took you ' + str(c) + ' tries to guess the number!')

        break

    else:

        print()
        print('You got ' + str(4-numberswrong) + ' numbers right.')
        print()

    c += 1
