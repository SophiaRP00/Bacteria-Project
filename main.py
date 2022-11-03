import numpy as np

credits = "created by Nicklas: s224218, Sophia: s224222, Jonas: s22####"

def dataLoad(filename):
    ##########################
    ## Loads data from file ##
    filein = open(filename, "r")
    lines = filein.readlines()
    normalText = "".join(lines)
    ##########################

    #Converting file to Matrix

    # for row in filename:
    #     data = []
    #     data.append([int(x) for x in row.split()])

    tmp = np.loadtxt(filename, dtype=float)
    data = np.zeros(3)
    print(data)
    for n in range(tmp[:,0].size):
        stack = False
        if tmp[n,0] > 10 and tmp[n,0] < 60 and tmp[n,1] > 0 and tmp[n,2] >= 1 and tmp[n,2] <= 4:
            stack = True
            #data = np.vstack((data, tmp[n,:]))
        else:
            print("Invalid data on line " + str(n + 1) + ": Not in range between 10-60 ;_;"

        if tmp[n,1] > 0:
            stack = True
        else:
            print("Invalid data on line " + str(n + 1) + ": Not a positive number :(")

    data = np.delete(data, 0, 0)
    print(data)
    #print(data[:,2])

    return np.ones((3,4))

dataLoad('test.txt')

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
    print("Cool")

    return

#main()