# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student IIT ID: 20220283
# Student UoW ID: w1998819

# Date: 29/03/2023

from time import time  #importing time library to randomize file names

def total():
    ans = user1 + user2 + user3
    return ans

s = str(round(time() * 10)) #assigning variables
fo = open("Credits - " + s + ".txt", "a")  

srange = [0, 20, 40, 60, 80, 100, 120]  #range of inputs

string = " "
histo = []
credit = []  #appends values of current inputs
all_credit = []  #appends values of all given inputs

x = 0
i = 0
a = 0
b = 0

while x == 0:  #main loop which allows to input values of many students
    while True:  #loops continues until it receives an integer 
        user1 = input("Please enter your credits at PASS: ")
        try:
            user1 = int(user1)
            if user1 in srange:
                credit.append(user1)
                break
            else:
                print("Out of Range")
        except ValueError:   #prints error in cases of ValueError
                print("Integer Required")
                
    while True:
        user2 = input("Please enter your credits at DEFER: ")
        try:
            user2 = int(user2)
            if user2 in srange:
                credit.append(user2)
                break
            else:
                print("Out of Range")
        except ValueError:
                print("Integer Required")

    while True:  
        user3 = input("Please enter your credits at FAIL: ")
        try:
            user3 = int(user3)
            if user3 in srange:
                credit.append(user3)
                break
            else:
                print("Out of Range")
        except ValueError:
                print("Integer Required")
    

    if total() == 120:  #only when total is 120, code is continued
        all_credit.append(credit)
        if credit[0] == 120:
            print("Progress")
            histo.append("Progress")
        elif credit[0] == 100:
            print("Progress (module trailer)")
            histo.append("Progress (module trailer)")
        elif credit[2] >= 80:
            print("Exclude")
            histo.append("Exclude")
        else:
            print("Module Retriever")
            histo.append("Module Retriever")

    else:
        print("Total Incorrect")

    while True:  #loops until valid answer is entered
        loop = input("\nWould you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ")
        print("\n")
        if loop == "q":
            x = 1   #main loop breaks when x != 0 and exits  to next code outside the loop
            break
        elif loop == "y":
            x = 0
            credit = []
            break  #breaks through current loop and returns to main loop
        else:
            print("Invalid Option")

print("-"*60, "\nHistogram")

count_p = histo.count("Progress")
count_t = histo.count("Progress (module trailer)")
count_r = histo.count("Module Retriever")
count_e = histo.count("Exclude")

print("Progress ", count_p, ": ", "*"*count_p, "\nTrailer ", count_t, ": ", "*"*count_t, "\nRetriever ", count_r, ": ", "*"*count_r, "\nExcluded ", count_e, ": ", "*"*count_e)
print("\n")
print(len(histo), "outcomes in total.")

print("-"*60, "\nPart 2 :")

l = len(histo)

while i < l:
    for element in all_credit[a]: #credit list inside all_credit is converted to string
        if b < 2:
            string += str(element) + ", "
            b += 1
        else:
            string += str(element)
            
    print(histo[a]," - ",string)  #progression outcome and all_credit elements are printed in order
    fo.write(histo[a]) #appending to text file
    fo.write(" - ")
    fo.write(string)
    fo.write("\n")
    a += 1  #changes element number of the list to print next progression outcome
    i += 1
    b = 0
    string = " "

print("-"*60, "\nPart 3 :")
fo = open("Credits - " + s + ".txt", "r")  #reads text file and prints output
print(fo.read())

fo.close()


