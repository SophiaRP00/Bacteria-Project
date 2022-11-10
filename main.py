import numpy as np
import matplotlib.pyplot as plt

credits = "created by Nicklas: s224218, Sophia: s224222, Jonas: s224191"

            ##################################
            ### This script was created by ###
            ### Jonas, Nicklas and Sophia  ###
            ##################################

def dataLoad():
    ####################################################
    ### Start of the function checks if file exists. ###
    ### If it exists, load the file                  ###
    ### Otherwise, write error message and retry     ###
    ####################################################

    print("Please write the name of the file you want to load data from.\nYou can write 'exit', if you want to go back to the menu\n")    
    while True:
        try:
            filenameChoice = input("Filename: ")
            if filenameChoice == "exit":
                return
            open(filenameChoice, "r")
            break
        except IOError:
            print("Invalid filename, please try again")
    print("File found and loaded!")

    #################################################################
    ### Converting file to Matrix and erasing errors              ###
    ### Using if loops to find line of error                      ###
    ### Writes the error, if no error -> stacks onto N x 3 Matrix ###  
    #################################################################

    error = ""
    tmp = np.loadtxt(filenameChoice, dtype=float)
    data = np.zeros(3)
    for n in range(tmp[:,0].size):
        valid = True
        if tmp[n,0] <= 10 or tmp[n,0] >= 60:
            error += "Invalid data on line " + str(n + 1) + ": Temperature not in range between 10-60 (ಠ_ಠ)\n"
            valid = False
        if tmp[n,1] <= 0:
            error += "Invalid data on line " + str(n + 1) + ": Growth rate is not a positive number (¬_¬)\n"
            valid = False
        if tmp[n,2] < 1 or tmp[n,2] > 4:
            error += "Invalid data on line " + str(n + 1) + ": Not a valid bacteria (╯°□°）╯︵ ┻━┻\n"
            valid = False

        if valid == True:
            data = np.vstack((data, tmp[n,:]))
            
    data = np.delete(data, 0, 0)

    if error != "":
        print("Errors has been found and deleted from the file: " + filenameChoice)
        input("Press enter To see the errors\n")
        print(error)
        input("Press enter to return to the menu\n")
    else:
        print("No errors found in file: " + filenameChoice)
        input("Press enter to return to the menu\n")
    return data

def dataFilter(data):

    #############################################
    ### The user chooses a filter via input() ###
    ### They can also write exit to go back   ###
    #############################################

    print("You can choose the following types of filtering:\n")
    print("1. Bacteria filter\n")
    print("2. Growth rate filter\n")
    print("You can write 'exit', if you want to go back to the menu\n")
    while True:
        filterChoice = input("Your choice: ")

        ######################################################
        ### If the user chooses bacteria filter,           ###
        ### They can again choose between the different    ###
        ### types of bacteria.                             ###
        ######################################################

        if filterChoice == "1":
            print("You chose to filter by bacteria\n")
            print("You can choose the following types of bacteria:\n")
            print("1. Salmonella enterica\n")
            print("2. Bacillus cereus\n")
            print("3. Listeria\n")
            print("4. Brochothrix thermosphacta\n")

            ######################################################
            ### The user chooses a bacteria, and the function  ###
            ### filters the dataset according to the bacteria. ###
            ######################################################

            bacterias = np.array([[1, "Salmonella enterica"], [2, "Bacillus cereus"], [3, "Listeria"], [4, "Brochothrix thermosphacta"]])
            while True:
                try:
                    bacteriaChoice = int(input("Please write the number of the bacteria you want to filter.\nYour choice: "))
                    if bacteriaChoice >= 1 and bacteriaChoice <= 4:
                        break
                    else:
                        print("Invalid number, please try again")
                except ValueError:
                    print("Invalid input, please try again")
            data = data[data[:,2] == bacteriaChoice]
            filter = "bacteria: " + bacterias[bacteriaChoice - 1, 1]
            print("Bacteria filter has been applied")
            input("Press enter to return to the menu\n")
            return data, filter
        
        ###########################################################
        ### If the user chooses growth rate filter,             ###
        ### They then choose between the upper and lower bounds ###
        ### of growth rates.                                    ###
        ### The function filters the dataset accordingly        ###
        ###########################################################

        elif filterChoice == "2":
            print("You chose to filter by growth rate\n")
            while True:
                try:
                    print("Please write the growth rate interval you want to filter.")
                    growthRateChoiceLower = float(input("\nLower bound: "))
                    if growthRateChoiceLower >= 0:
                        break
                    else:
                        print("Invalid number, please try again")
                except ValueError:
                    print("Invalid input, please try again")
            dataLower = data[data[:,1] >= growthRateChoiceLower]
            while True:
                try:
                    growthRateChoiceUpper = float(input("\nUpper bound: "))
                    if growthRateChoiceUpper >= 0 and growthRateChoiceUpper >= growthRateChoiceLower:
                        break
                    else:
                        print("Invalid number, please try again")
                except ValueError:
                    print("Invalid input, please try again")
            data = dataLower[dataLower[:,1] <= growthRateChoiceUpper]
            filter = "growth rate: " + str(growthRateChoiceLower) + " - " + str(growthRateChoiceUpper)
            print("Growth rate filter has been applied")
            input("Press enter to return to the menu\n")
            return data, filter
        elif filterChoice == "exit":
            break
        if filterChoice != "1" or filterChoice != "2" or filterChoice != "exit":
            print("Invalid input, please try again")

def dataStatistics(data, statistics):

    #####################################################################
    ### Function starts by defining the different types of statistics ###
    #####################################################################

    coldData = np.array([])                             
    hotData = np.array([])                              
    for n in range(data[:,0].size):                     
        if data[n,0] < 20:                              
            coldData = np.append(coldData, data[n,1])   
        elif data[n,0] > 50:                            
            hotData = np.append(hotData, data[n,1])     

    meanTemp = np.mean(data[:,0])
    meanGrowth = np.mean(data[:,1])
    stdTemp = np.std(data[:,0])
    stdGrowth = np.std(data[:,1])
    rows = data[:,0].size
    coldGrowth = np.mean(coldData)
    hotGrowth = np.mean(hotData)

    ##########################################################
    ### According to the users choice,                     ###
    ### the function prints the different statistics.      ###
    ##########################################################

    showed = 0
    if (statistics).lower == "mean temperature" or statistics == "1":
        showed = "\nMean temperature:\n" + str(meanTemp)
    elif (statistics).lower == "mean growth rate" or statistics == "2":
        showed = "\nMean growth rate:\n" + str(meanGrowth)
    elif (statistics).lower == "std temperature" or statistics == "3":
        showed = "\nStandard deviation temperature:\n" + str(stdTemp)
    elif (statistics).lower == "std growth rate" or statistics == "4":
        showed = "\nStandard deviation of growth rate:\n" + str(stdGrowth)
    elif (statistics).lower == "rows" or statistics == "5":
        showed = "\nNumber of rows:\n" + str(rows)
    elif (statistics).lower == "mean cold growth rate" or statistics == "6":
        showed = "\nMean cold growth rate:\n" + str(coldGrowth)
    elif (statistics).lower == "mean hot growth rate" or statistics == "7":
        showed = "\nMean hot growth rate:\n" + str(hotGrowth)
    print(showed)
    print("\nPlease write a number corresponding to your choice")

def dataPlot(data):
    #########################################################
    ### First plot - Number of Bacteria                   ###
    ### Counts how often each Bacteria appears in dataset ###
    ### Then plots the data regarding to each bacteria    ###
    #########################################################
    
    bacteria = np.zeros(4)
    for n in range(data[:,0].size):
        bacteria[int(data[n,2])-1] += 1
    
    x = np.array(["Salmonella enterica", "Bacillus cereus", "Listeria", "Brochothrix thermosphacta"])#bacteriaPlot[:,0]
    y = np.array([bacteria[0], bacteria[1], bacteria[2], bacteria[3]])
    plots = plt.bar(x, y, color = 'maroon', width = 0.5)
    plt.title("Bar Plot - Number of Bacteria")
    plt.xlabel("Bacteria")
    plt.ylabel("Number of Bacteria")
    plt.show()

    ################################################################
    ### Second data plot - Growth rate of Bacteria               ###
    ### Creating x-axis with temperature between 10-60C          ###
    ### Makes two variables for each bacteria                    ###
    ### Appends variables with data from the chosen dataset      ###
    ### Differentiates the plots using legend and colors         ###
    ################################################################

    salmX = np.array([])
    salmY = np.array([])
    bacilX = np.array([])
    bacilY = np.array([])
    listerX = np.array([])
    listerY = np.array([])
    brochoX = np.array([])
    brochoY = np.array([])

    for n in range(data[:,0].size):
        if data[n,2] == 1:
            salmX = np.sort(np.append(salmX, data[n,0]))
            salmY = np.sort(np.append(salmY, data[n,1]))
        elif data[n,2] == 2:
            bacilX = np.sort(np.append(bacilX, data[n,0]))
            bacilY = np.sort(np.append(bacilY, data[n,1]))
        elif data[n,2] == 3:
            listerX = np.sort(np.append(listerX, data[n,0]))
            listerY = np.sort(np.append(listerY, data[n,1]))
        elif data[n,2] == 4:
            brochoX = np.sort(np.append(brochoX, data[n,0]))
            brochoY = np.sort(np.append(brochoY, data[n,1]))
    plt.plot(salmX, salmY, color = 'salmon', label = "Salmonella enterica")
    plt.plot(bacilX, bacilY, color = 'seagreen', label = "Bacillus cereus")
    plt.plot(listerX, listerY, color = 'orchid', label = "Listeria")
    plt.plot(brochoX, brochoY, color = 'royalblue', label = "Brochothrix thermosphacta")

    plt.title("Growth rate by temperature")
    plt.xlabel("Temperature")
    plt.ylabel("Growth rate")
    plt.legend()
    
    plt.show()

    return

def main():
    filter = ""
    ########################################################
    ### initialization of program                        ###
    ### Creating input so user can choose program        ###
    ### User shall choose number from 1-5 to use program ###
    ########################################################
    while True:
        print("\n--------------------------------------------")
        print("| Welcome to the Bacteria Analysis Project |")
        print("-------------------------------------------- \n")
        print("    ############")
        print("    ### Menu ###")
        print("    ############")
        print("\nWhat do you want to do?\nPlease write a number from 1 - 5, according to your choice\n")

        ################################
        ### Shows the applied filter ###
        ################################
        if filter != "":
            print("------------------" + (len(filter) * "-") + "--")
            print("| Applied filter: " + filter + " |")
            print("------------------" + (len(filter) * "-" + "--\n"))
        
        print("1. Load data from file \n")
        print("2. Filter data \n")
        print("3. Show statistics\n")
        print("4. Generate diagrams/plot data\n")
        print("5. Reset filter\n")
        print("6. Exit program\n")
        choice = input("Your choice: ")

        #################
        ### Load data ###
        #################
        if choice == "1":
            print("\nYou chose to load data from file")
            loadedData = dataLoad()
            originalData = loadedData

        ###################
        ### Filter data ###
        ###################
        elif choice == "2":
            print("You have chosen to filter data")
            try:
                loadedData, filter = dataFilter(loadedData)
            except UnboundLocalError:
                print("ERROR: You have to load data first")
                input("Press enter to return to the menu\n")
        
        #######################
        ### Show statistics ###
        #######################
        elif choice == "3":
            print("\nYou chose to show statistics. (Write the number corresponding to your choice)\n")
            print("These are the options you can choose from:\n")
            print("1. Mean temperature\n")
            print("2. Mean growth rate\n")
            print("3. Standard deviation of temperature\n")
            print("4. Standard deviation of growth rate\n")
            print("5. Number of rows\n")
            print("6. Mean cold growth rate\n")
            print("7. Mean hot growth rate\n")
            print("8. Return to menu\n")
            while True:
                statisticChoice = input("Your choice: ")
                try:
                    if int(statisticChoice) > 0 and int(statisticChoice) < 8:
                        try:
                            dataStatistics(loadedData, statisticChoice)
                        except UnboundLocalError:
                            print("ERROR: You have to load data first")
                            input("Press enter to return to the menu")
                            break
                    elif int(statisticChoice) == 8:
                        break
                    else:
                        print("ERROR: You have to write a number from 1 - 8")
                except ValueError:
                    print("You have to write a non-decimal number")
        
        ##############################
        ### Generate diagrams/plot ###
        ##############################
        elif choice == "4":
            print("You chose to generate diagrams/plot data")
            try:
                dataPlot(loadedData)
            except UnboundLocalError:
                print("ERROR: You have to load data first")
                input("Press enter to return to the menu\n")
        
        ###########################
        ### Reset filtered data ###
        ###########################
        elif choice == "5":
            print("You chose to reset filter")
            try:
                loadedData = originalData
                filter = ""
                input("Filter has been reset. Press enter to return to the menu\n")
            except UnboundLocalError:
                print("ERROR: You have to load data first")
                input("Press enter to return to the menu\n")

        ####################
        ### Exit program ###
        ####################
        elif choice == "6":
            if input("Are you sure you want to leave? [y/n]\n") == "y":
                print("Thank you for using the Bacteria Analysis Project")
                print(credits)
                print('''\
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠤⠒⠒⠒⠒⠠⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠞⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⢻⠄⢠⠔⠒⠒⠒⠒⠒⢢⡀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀⠇⠀⠀⠀⠀⠀⠀⠀⢳⢸⠂⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⣀⣹⠞⠀⠀⠀⠀⠀⠀⠀⠀⣸⣼⠀⠀⠀⠀(goodbyee)
                ⠀⠀⠀⠀⠀⠀⠀⠹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠙⢲⠀⠀⠀⠀⠀⠀⠀⢠⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⢠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠀⠀⠀⠀⠀⠀⢸⡧⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⢀⡠⠔⢚⡟⡏⠉⠙⡇⠀⠀⣠⠟⡇⠀⠉⠁⠀⠒⠠⠄⣀⠀⠀⠀
                ⠀⣠⠔⠊⠁⠀⠀⢸⠀⡇⠀⢰⠃⣀⠜⠁⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡀
                ⡞⠀⠀⠀⠀⠀⠀⢸⣀⣇⣀⣸⣯⡁⠀⡠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹
                ⡇⠀⠀⠀⠀⠀⠀⠈⢹⣰⠛⡆⠀⠈⠉⢰⠃⠀⠀⠀⠀⣴⠶⡀⠀⠀⠀⠀⢸
                ⡇⠀⠀⠀⠀⠀⠀⠀⢸⣟⠀⡇⠀⠀⠀⢸⠀⠀⠀⠀⠀⢹⠀⢇⠀⢴⣦⠀⣏
                ⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣴⠃⠀⠀⠀⢸⡄⠀⠀⠀⠀⢈⠀⠈⣓⢻⡟⢱⡛                            
                ''')                
                break
    return

main()