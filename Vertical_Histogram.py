# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: W1761768              # Date:  2019/11/28

# Set variables
count1 = 0
count2 = 0
count3 = 0
count4 = 0
# Creating a while and break if user enters 'q'
while True:

    try:
        # Getting the user inputs
        x = input("Pass:")
        if x == 'q':
            break
        x = int(x)
        y = int(input("Defer:"))
        z = int(input("Fail:"))
        # Checking weather their ranges are correct or not
        if x % 20 == 0 and y % 20 == 0 and z % 20 == 0:
            # Checking weather their total is correct or not
            if x + y + z == 120:
                # printing the progression outcome according to their conditions
                if x == 120:
                    count1 += 1
                    print("Progress")
                elif x == 100 and y == 20:
                    count2 += 1
                    print("Progress – module trailer")
                elif x == 100 and z == 20:
                    count2 += 1
                    print("Progress – module trailer")
                elif x <= 40 and z >= 80:
                    count3 += 1
                    print("Exclude")
                else:
                    print("Do not Progress – module retriever")
                    count4 += 1

            else:
                print("Total incorrect")
        else:
            print("Range error")
    except ValueError:
        print("Integers required")


def staff(count1,count2,count4,count3):
    print('Progress', end=' ')
    print('Trailing', end=' ')
    print('Retriever', end=' ')
    print('Excluded')

    while count1 != 0 or count2 != 0 or count4 != 0 or count3 != 0:
        if count1 != 0:
            print("  *", end="        ")
            count1 -= 1
        else:
            print("    ", end="       ")
        if count2 != 0:
            print("*", end="        ")
            count2 -= 1
        else:
            print(" ", end="        ")
        if count4 != 0:
            print("*", end="       ")
            count4 -= 1
        else:
            print(" ", end="       ")
        if count3 != 0:
            print("  *")
            count3 -= 1
        else:
            print(" ")


staff(count1, count2, count4, count3)
