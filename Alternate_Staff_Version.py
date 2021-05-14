# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: W1761768              # Date:  2019/11/28

# Create lists
Pass = [120, 100, 100, 80, 60, 40, 20, 20, 20, 0]
Defer = [0, 20, 0, 20, 40, 40, 40, 20, 0, 0]
Fail = [0, 0, 20, 20, 20, 40, 60, 80, 100, 120] 
# Set the counts
count1 = 0
count2 = 0
count3 = 0
count4 = 0
# Create a for loop
for i in range(len(Defer)):
    # According to the appendix checking if all conditions satisfy
    if Pass[i] + Defer[i] + Fail[i] == 120:
        if Pass[i] == 120:
            count1 += 1
        elif Pass[i] == 100 and Defer[i] == 20:
            count2 += 1
        elif Pass[i] == 100 and Fail[i] == 20:
            count2 += 1
        elif Pass[i] <= 20 and Fail[i] >= 80:
            count3 += 1
        else:
            count4 += 1


def staff(a):
    print('', '*'*a)

# Display the horizontal histogram


print('Progress', '\b:', end='')
staff(count1)
print('Trailing', '\b:', end='')
staff(count2)
print('Retriever', '\b:', end='')
staff(count4)
print('Excluded', '\b:', end='')
staff(count3)






