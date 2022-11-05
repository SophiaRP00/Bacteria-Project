import numpy as np
import matplotlib.pyplot as plt

creditsShown = 0
credits = "created by Nicklas: s224218, Sophia: s224222, Jonas: s224191"
dataChoice = "2"

def isFile():
    print("\nYou chose to load data from file")
    print("Please write the name of the file you want to load data from.\nYou can write 'exit', if you want to go back to the menu\n")    
    while True:
        try:
            filenameChoice = input("Filename: ")
            open(filenameChoice, "r")
            print("File found and loaded! \nYou will now be returned to the menu")
            return filenameChoice
        except IOError:
            if filenameChoice == "exit":
                break
            print("Invalid filename, please try again")

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
    
    ###### Loop to make cold growth and hot growth ######
    coldData = np.array([])                             #
    hotData = np.array([])                              #
    for n in range(rows):                               #
        if data[n,0] < 20:                              #
            coldData = np.append(coldData, data[n,1])   #
        elif data[n,0] > 50:                            #
            hotData = np.append(hotData, data[n,1])     #
    #####################################################

    meanTemp = np.mean(data[:,0])
    meanGrowth = np.mean(data[:,1])
    stdTemp = np.std(data[:,0])
    stdGrowth = np.std(data[:,1])
    rows = data[:,0].size
    coldGrowth = np.mean(coldData)
    hotGrowth = np.mean(hotData)

    if (statistics).lower == "mean temperature" or statistics == "1":
        return meanTemp
    elif (statistics).lower == "mean growth rate" or statistics == "2":
        return meanGrowth
    elif (statistics).lower == "std temperature" or statistics == "3":
        return stdTemp
    elif (statistics).lower == "std growth rate" or statistics == "4":
        return stdGrowth
    elif (statistics).lower == "rows" or statistics == "5":
        return rows
    elif (statistics).lower == "mean cold growth rate" or statistics == "6":
        return coldGrowth
    elif (statistics).lower == "mean hot growth rate" or statistics == "7":
        return hotGrowth
    return

def dataPlot(data):
    ################################################
    #First plot - Number of Bacteria 
    ### First plot - Number of Bacteria          ###
    # creating the dataset 
    ### Counting how often each Bacteria appears ###
    ### Then adding it as value in Data Plot     ###
    ################################################

    count = 0
    Bact = np.zeroes(4)

    for i in data[:,2]:
            Bact[i-1] += 1
    
    Bacteria = {'Salmonella Enterica':Bact[0], 'Bacillus Cereus':Bact[1], 'Listeria':Bact[2], 'Brochothrix Thermosphacta':Bact[3]} 
    courses = list(data.keys()) 
    values = list(data.values()) 

    fig = plt.figure(figsize = (10, 5)) 
    plt.bar(bacteria, values, color ='maroon',width=0.4)
    plt.xlabel("Types of Bacteria")
    plt.ylabel("Number of each Bacteria")
    plt.title("Bar Plot - Number of Bacteria")
    plt.show()
    return

def main():
    ########################################################
    ### initialization of program                        ###
    ### Creating input so user can choose program        ###
    ### User shall choose number from 1-5 to use program ###
    ########################################################
    while True:
        print("\n--------------------------------------------")
        print("| Welcome to the Bacteria Analysis Project |")
        print("-------------------------------------------- \n")
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
            filenameChoice = isFile()
        
        elif choice == "2":
            print("hi")
            print(filenameChoice)
            #dataLoad(filenameChoice)
            
        
        elif choice == "3":
            while True:
                print("\nYou chose to show statistics. (You can write either the specific number or the specific text to get the statistic)\n")
                print("These are the options you can choose from:\n")
                print("1. Mean temperature\n")
                print("2. Mean growth rate\n")
                print("3. Standard deviation of temperature\n")
                print("4. Standard deviation of growth rate\n")
                print("5. Number of rows\n")
                print("6. Mean cold growth rate\n")
                print("7. Mean hot growth rate\n")
                print("8. Exit program\n")
                try:
                    statisticChoice = input("Your choice: ")
                    if (statisticChoice).lower == "exit program" or statisticChoice == "8":
                        main()
                    print(dataStatistics(data, statisticChoice))
                    # print("Data loaded successfully! :D\nYou will now be redirected to the menu\n")
                    # main()
                    break
                except OSError:
                    print("Invalid number/text :( please try again")
    return

main()