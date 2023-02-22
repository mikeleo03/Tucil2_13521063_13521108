import main

def bruteForce(listOfPoints) :
    shortest = main.EuclideanDist3(listOfPoints[0], listOfPoints[1])

    for i in range (len(listOfPoints)) :
        for j in range(len(listOfPoints)) :
            if (i != j) and (main.EuclideanDist3(listOfPoints[i], listOfPoints[j]) <= shortest):
                shortest = main.EuclideanDist3(listOfPoints[i], listOfPoints[j])
                a = listOfPoints[i]
                b = listOfPoints[j]
                
    return shortest

def bruteForceDistGeneral(listOfPoints, dimention) :
    shortest = main.EuclideanDistGeneral(listOfPoints[0], listOfPoints[1])

    for i in range (len(listOfPoints)) :
        for j in range(len(listOfPoints)) :
            if (i != j) and (main.EuclideanDistGeneral(listOfPoints[i], listOfPoints[j]) <= shortest):
                shortest = main.EuclideanDistGeneral(listOfPoints[i], listOfPoints[j])
                a = listOfPoints[i]
                b = listOfPoints[j]
                
    return a, b, shortest