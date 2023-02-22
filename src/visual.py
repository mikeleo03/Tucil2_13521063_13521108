import matplotlib.pyplot as plt
import main


def visualize(listOfPoints) :
    fig = plt.figure(figsize=(11,7))
    ax = fig.add_subplot(111, projection='3d')

    for i in range (len(listOfPoints)) :
        x = listOfPoints[i][0]
        y = listOfPoints[i][1]
        z = listOfPoints[i][2]

        ax.scatter(x,y,z, color='red')
    
    plt.show()

def visualizeMinimum(listOfPoints) :
    fig = plt.figure(figsize=(11,7))
    ax = fig.add_subplot(111, projection='3d')

    for i in range (len(listOfPoints)) :
        x = listOfPoints[i][0]
        y = listOfPoints[i][1]
        z = listOfPoints[i][2]

        ax.scatter(x,y,z, color='black')
    
    point1, point2, dist = main.bruteForce(listOfPoints)

    ax.scatter(point1[0],point1[1],point1[2], color='red')
    ax.scatter(point2[0],point2[1],point2[2], color='red')

    # How to plot the line
    # ax.plot([point1[0],point2[0]],[point1[1],point2[1]],[point1[2],point2[2]],color='green')

    plt.show()