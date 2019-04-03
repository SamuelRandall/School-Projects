#  File: sorting.py
#  Description: A driver that will sort various random lists and calculate the execution times using different sorting algorithms.
#  Student's Name: Samuel Randall
#  Student's UT EID: spr699
#  Course Name: CS 313E 
#  Unique Number: 51465
#
#  Date Created: 11/29/17
#  Date Last Modified:11/30/17

import random
import time
import sys
sys.setrecursionlimit(10000)

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1


def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

# function to return an almost sorted list
def almostSorted(sortList):

    elements = len(sortList)
    swaps = elements // 10
    
    count = 0
    
    while(count < swaps):
        num1 = random.randint(0, elements - 1)
        num2 = random.randint(0, elements - 1)
        
        if(num1 != num2):
            val1 = sortList[num1]
            val2 = sortList[num2]
            sortList[num1] = val2
            sortList[num2] = val1
            count += 1
            
    return sortList

def main():
    
    sortTypes = ["bubble", "insertion", "merge", "quick"]
    listTypes = ["Random", "Sorted", "Reverse", "Almost sorted"]
    sizes = [10, 100, 1000]
    
    bubbleResults = [[], [], [], []]
    insertionResults = [[], [], [], []]
    selectionResults = [[], [], [], []]
    mergeResults = [[], [], [], []]
    quickResults = [[], [], [], []]

    # first go through each size, then each type of list, then each type of method
    for sort in sortTypes:       
        for listType in listTypes: 
            for size in sizes: 
                temp = 0
                pos = -1
                
                for trial in range(5):
                    # generating the random list for each type of method
                    sortList = []
                    for num in range(size):
                        sortList.append(num)
                        
                    if(listType == "Random"):
                        random.shuffle(sortList)
                        pos = 0
                        
                    elif(listType == "Sorted"):
                        pos = 1
                        
                    elif(listType == "Reverse"):
                        sortList.reverse()
                        pos = 2
                        
                    elif(listType == "Almost sorted"):
                        sortList = almostSorted(sortList)
                        pos = 3
                        
                    elapsedTime = 0

                    # performing the timing of each method's algorithm
                    if(sort == "bubble"):
                        startTime = time.perf_counter()
                        bubbleSort(sortList)
                        endTime = time.perf_counter()
                        elapsedTime = endTime - startTime
                        
                    elif(sort == "insertion"):
                        startTime = time.perf_counter()
                        insertionSort(sortList)
                        endTime = time.perf_counter()
                        elapsedTime = endTime - startTime
                        
                    elif(sort == "merge"):
                        startTime = time.perf_counter()
                        mergeSort(sortList)
                        endTime = time.perf_counter()
                        elapsedTime = endTime - startTime
                        
                    elif(sort == "quick"):
                        startTime = time.perf_counter()
                        quickSort(sortList)
                        endTime = time.perf_counter()
                        elapsedTime = endTime - startTime
                        
                    temp += elapsedTime

                # calculating the average for each method and appending it into
                # associated table
                avg = temp / 5
                if(sort == "bubble"):
                    bubbleResults[pos].append(avg)
                    
                elif(sort == "insertion"):
                    insertionResults[pos].append(avg)
                    
                elif(sort == "merge"):
                    mergeResults[pos].append(avg)
                    
                elif(sort == "quick"):
                    quickResults[pos].append(avg)

    # printing the results                   
    count = 0
    for Type in listTypes:
        print("Input type =", Type)
        print("                    avg time   avg time   avg time")
        print("   Sort function     (n=10)    (n=100)    (n=1000)")
        print("-----------------------------------------------------")
        print("      bubbleSort    %.6f   %.6f   %.6f" %(bubbleResults[count][0],bubbleResults[count][1],bubbleResults[count][2]))
        print("   insertionSort    %.6f   %.6f   %.6f" %(insertionResults[count][0], insertionResults[count][1], insertionResults[count][2]))
        print("       mergeSort    %.6f   %.6f   %.6f" %(mergeResults[count][0], mergeResults[count][1], mergeResults[count][2]))
        print("       quickSort    %.6f   %.6f   %.6f" %(quickResults[count][0], quickResults[count][1], quickResults[count][2]))
        print("\n")
        count += 1
    
main()
