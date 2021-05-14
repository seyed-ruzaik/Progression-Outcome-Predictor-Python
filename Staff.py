# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: W1761768              # Date:  2019/11/28


# Set the variables
count1 = 0
count2 = 0
count3 = 0
count4 = 0
total = 0
# Create a while loop and break if the user enters 'q'
while True:
    try:
        # Getting the user inputs
        x = input("Pass:")
        if x == 'q':
            break
        x = int(x)
        y = int(input("Defer:"))
        z = int(input("Fail:"))
        # Checking weather all the inputs add up to 120 or not
        if x % 20 == 0 and y % 20 == 0 and z % 20 == 0:
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


def staff(a):
    print('', "*"*a)

# Display the histogram


print('Progress', count1, '\b:', end='')
staff(count1)
print('Trailing', count2, '\b:', end='')
staff(count2)
print('Retriever', count4, '\b:', end='')
staff(count4)
print('Excluded', count3, '\b:', end='')
staff(count3)
total = count1+count2+count3+count4
print(total, 'outcomes in total.')
