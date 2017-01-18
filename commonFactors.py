import random

# Decide if two numbers have a common factor
# Returns True or False
def commonfactor(a,b):
    # Identify smaller number
    smaller = a
    if b < smaller:
        smaller = b

    # Go through numbers from 2 to smaller,
    # check if it is a factor for both
    for i in range(2,smaller+1):
        if a % i == 0 and b % i == 0:
            return True

    # If get to this point, no common factor.
    return False


# Picks two numbers at random and checks if they
# have a common factor
# Returns True or False
def simulate(maxnum):
    n1 = random.randint(2,maxnum)
    n2 = random.randint(2,maxnum)
    return commonfactor(n1,n2)



# Main program: Do simulation many times,
# record and print out results
maxnum = 50
numtrials = 100000
count = 0
for i in range(numtrials):
    if simulate(50):
        count += 1

percent = 1 - count / numtrials
print("The probability of two numbers chosen between 2 and {} having a common factor is {:.2%}.".format(maxnum,percent))
