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

    if (statistics).lower == "mean temperature":
        return meanTemp
    elif (statistics).lower == "mean growth rate":
        return meanGrowth
    elif (statistics).lower == "std temperature":
        return stdTemp
    elif (statistics).lower == "std growth rate":
        return stdGrowth
    elif (statistics).lower == "rows":
        return rows
    elif (statistics).lower == "mean cold growth rate":
        return coldGrowth
    elif (statistics).lower == "mean hot growth rate":
        return hotGrowth
    return

def dataPlot(data):
    ################################################
    ### First plot - Number of Bacteria          ###
    ### First plot - Number of Bacteria          ###
    ### creating the dataset                     ###
    ### Counting how often each Bacteria appears ###
    ### Then adding it as value in Data Plot     ###
    ################################################

    count = 0
    Bact = np.zeroes(4)

    for i in data[:,2]:
            Bact[i-1] += 1
    
    Bacteria = {'Salmonella Enterica':Bact[0], 'Bacillus Cereus':Bact[1], 'Listeria':Bact[2], 'Brochothrix Thermosphacta':Bact[3]} 
    c = list(Bacteria.keys()) 
    values = list(Bacteria.values()) 

    fig = plt.figure(figsize = (10, 5)) 
    plt.bar(Bacteria, values, color ='maroon',width=0.4)
    plt.xlabel("Types of Bacteria")
    plt.ylabel("Number of each Bacteria")
    plt.title("Bar Plot - Number of Bacteria")
    plt.show()

    ################################################################
    ### Second data plot - Growth rate of Bacteria               ###
    ### Creating tx-axis with temperature as data[0] from 10-60C ###
    ### Creating dataset                                         ###
    ### Creating the plot where each graph gets differen colour  ###
    ### Using Legend to make an info box about our graphs        ###
    ################################################################

    #JEG HAR FORSØGT AT LAVE DATA TIL PLOT 2. Ved ikke helt, hvad Y skal være
    x1 = data[:,0]
    y1 = Bact[0]

    plt.plot(x1,y1, color='yellow', label = 'Salmonella Enterica')

    x2 = data[:,0]
    y2 = Bact[1]

    plt.plot(x2,y2, color='red',label = 'Bacillus Cereus')

    x3 = data[:,0]
    y3 = Bact[2]

    plt.plot(x3,y3, color='blue' ,label = 'Listeria') 

    x4 = data[:,0]
    y4 = Bact[3]

    plt.plot(x4,y4, color='green',label = 'Brochothrix Thermosphacta')

    plt.xlabel('Temperature')
    plt.ylabel('Growth Rate')
    plt.title('Growth Rate of Bacteria')
    plt.legend()
    plt.show()

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
    #elif choice == "3":



    return

main()