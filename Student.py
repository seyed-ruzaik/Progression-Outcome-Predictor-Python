# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: W1761768              # Date:  2019/11/28

def student():
    try:
        # Getting the user inputs.
        x = int(input("Pass:"))
        y = int(input("Defer:"))
        z = int(input("Fail:"))
# Checking weather the above inputs are in range or not.
        if x % 20 == 0 and y % 20 == 0 and z % 20 == 0:
            # Checking weather all the inputs add up to 120 or not.
            if x+y+z == 120:
                # printing the progression outcome according to the conditions.
                if x == 120:
                    print("Progress")
                elif x == 100 and y == 20:
                    print("Progress – module trailer")
                elif x == 100 and z == 20:
                    print("Progress – module trailer")
                elif x <= 40 and z >= 80:
                    print("Exclude")
                else:
                    print("Do not Progress – module retriever")
            else:
                print("Total incorrect")
        else:
            print("Range error")
    except:
        print("Integers required")
# Call the function.
student()

