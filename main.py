import numpy as np
import matplotlib.pyplot as plt

creditsShown = False
credits = "created by Nicklas: s224218, Sophia: s224222, Jonas: s224191"

def dataLoad(filename):
    ######################################################
    ### Converting file to Matrix                      ###
    ### Using if-else loops to find line for error     ###
    ### Writing what the error is and stacking if true ###
    ### By Jonas, Nicklas and Sophia                   ###   
    ######################################################

    tmp = np.loadtxt(filename, dtype=float)
    data = np.zeros(3)
    for n in range(tmp[:,0].size):
        stack = False
        if tmp[n,0] > 10 and tmp[n,0] < 60:
            stack = True
        else:
            print("Invalid data on line " + str(n + 1) + ": Not in range between 10-60 (ಠ_ಠ)\n")
        if tmp[n,1] > 0:
            stack = True
        else:
            print("Invalid data on line " + str(n + 1) + ": Not a positive number (¬_¬)\n")
        if tmp[n,2] >= 1 and tmp[n,2] <= 4:
            stack = True
        else:
            print("Invalid data on line " + str(n + 1) + ": Not a valid bacteria (╯°□°）╯︵ ┻━┻\n")
        if stack == True:
            data = np.vstack((data, tmp[n,:]))
    data = np.delete(data, 0, 0)
    return data

def dataStatistics(data, statistics):
    # Insert your code here
    return

def dataPlot(data):
    # Insert your code here
    return

def main():
    ########################################################
    ### initialization of program                        ###
    ### Creating input so user can choose program        ###
    ### User shall choose number from 1-5 to use program ###
    ########################################################

    print("\n" + credits + "\n\n\n" + "This program is a part of the 'Bakterie-dataanalyse' project.\n")
    input("############################\n" + "Press Enter to continue...\n" + "############################\n\n")

    print("############")
    print("### Menu ###")
    print("############")
    print("\nWhat do you want to do? Please write a number from 1 - 5, according to your choice\n")
    print("1. Load data from file \n")
    print("2. Filter data \n")
    print("3. Show statistics\n") #Uses the dataStatistics function
    print("4. Generate diagrams/plot data\n")
    print("5. Exit program\n")
    choice = input("Your choice: ")
    if choice == "1":
        print("\nYou chose to load data from file")
        print("Please write the name of the file you want to load data from.\nYou can write 'exit', if you want to go back to the menu\n")
        while True:
            try:
                filename = input("Filename: ")
                if filename == "exit":
                    main()
                data = dataLoad(filename)
                print("Data loaded successfully! :D\nYou will now be redirected to the menu\n")
                main()
                break
            except OSError:
                print("Invalid filename, please try again")


    return

main()