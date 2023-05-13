# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student IIT ID: 20220283
# Student UoW ID: w1998819

# Date: 29/03/2023

def total():
    ans = user1 + user2 + user3
    return ans

#defining variables
dic = dict()
srange = [0, 20, 40, 60, 80, 100, 120] 

userids = []  #appends values of user ids entered
credit = []   #appends user scores
  
s = " " #string containing user progression outcome and credits
x = 0
i = 0

while x == 0:
    uid = input("Please enter your student ID: ")
    userids.append(uid) 
    while True:
        user1 = input("Please enter your credits at PASS: ")
        try:
            user1 = int(user1)
            if user1 in srange:
                credit.append(user1)
                break
            else:
                print("Out of Range")
        except ValueError:   
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
    

    if total() == 120:  
        if credit[0] == 120:
            print("Progress")
            s += "Progress - "

        elif credit[0] == 100:
            print("Progress (module trailer) ")
            s += "Progress (module trailer) - "

        elif credit[2] >= 80:
            print("Exclude")
            s += "Exclude - "

        else:
            print("Module Retriever")
            s += "Module Retriever - "

        s += ','.join([str(n) for n in credit]) #appeneds credit scores after the progression outcome using join function

        
        dic[userids[i]] = s   #assigning keys and values to dictionary
            
    else:
        print("Total Incorrect")

    while True:  
        loop = input("\nWould you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ")
        print("\n")
        if loop == "q":
            x = 1   
            break
        elif loop == "y":
            x = 0
            credit = []
            s = " "
            i += 1
            break  
        else:
            print("Invalid Option")

print(*[str(k) + ':' + str(v) for k,v in dic.items()], sep='  ') #prints dictionary by converting keys and values to string
