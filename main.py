import numpy as np

credits = "created by Nicklas: s224218, Sophia: s224222, Jonas: s22####"

def dataLoad(filename):
    ##########################
    ## Loads data from file ##
    filein = open(filename, "r")
    lines = filein.readlines()
    normalText = "".join(lines)
    
    ##########################

    print(normalText)

    return np.ones((3,4))

def dataStatistics(data, statistics):
    # Insert your code here
    return

def dataPlot(data):
    # Insert your code here
    return

def main():
    # initialization of program
    print("\n" + credits + "\n\n\n" + "This program is a part of the 'Bakterie-dataanalyse' project.\n")
    input("############################\n" + "Press Enter to continue...\n" + "############################")
    print("\n\n")
    print("############")
    print("### Menu ###")
    print("############")
    print("\n what do you want to do?")
    return

main()