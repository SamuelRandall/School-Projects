#  File: ERsim.py
#  Description: Simulate an ER environment
#  Student's Name: Samuel Randall
#  Student's UT EID: spr699
#  Course Name: CS 313E 
#  Unique Number: 51465
#
#  Date Created: 10/19/17
#  Date Last Modified:10/19/17

class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]
    
    def __str__(self):
        return str(self.items)

# reads the file and operates on the content
def readFile(file, critQueue, fairQueue, serQueue):
    
    file = open(file, "r")

    for line in file:
        
        #convert the line into an array of words
        line = line.split()
        
        command = line[0]

        # start handling add command
        if command == "add":
            condition = line[1]
            name = line[2]

            print()
            print("Add patient %s to %s queue" % (name, condition))
            print()
            
            if condition == "Critical":
                critQueue.enqueue(name)
            elif condition == "Serious":
                serQueue.enqueue(name)
            else:
                fairQueue.enqueue(name)
                
            printQueues(critQueue, fairQueue, serQueue)

        # start handling 'treat' command               
        elif command == "treat":
            condition = line[1]
            
            # 'next' condition
            if condition == "next":
                
                print()
                print("Treat next patient")
                print()
                
                if not critQueue.isEmpty():
                    patient = critQueue.dequeue()
                    print("Treating '%s' from Critical queue" % (patient))
                    printQueues(critQueue, fairQueue, serQueue)
                    
                elif not serQueue.isEmpty():
                    patient = serQueue.dequeue()
                    print("Treating '%s' from Serious queue" % (patient))
                    printQueues(critQueue, fairQueue, serQueue)
                    
                elif not fairQueue.isEmpty():
                    patient = fairQueue.dequeue()
                    print("Treating '%s' from Fair queue" % (patient))
                    printQueues(critQueue, fairQueue, serQueue)
                    
                else:
                    print("No patients in queues")
                    
            # 'all' condition
            elif condition == "all":
                print()
                print("Command: Treat all patients")
                print()
                
                while not critQueue.isEmpty():
                    patient = critQueue.dequeue()
                    print("Treating '%s' from Critical queue" % (patient))
                while not serQueue.isEmpty():
                    patient = serQueue.dequeue()
                    print("Treating '%s' from Serious queue" % (patient))
                while not fairQueue.isEmpty():
                    patient = fairQueue.dequeue()
                    print("Treating '%s' from Fair queue" % (patient))
                    
                print("No patients in queues")
                    
            # handles the 'treat condition' condition
            else:
                print()
                print("Treat next patient on %s queue" % (condition))
                print()
                
                if condition == "Critical":
                    if not critQueue.isEmpty():
                        patient = critQueue.dequeue()
                        print("Treating '%s' from Critical queue" % (patient))
                    else:
                        print("No patients in queue")
                elif condition == "Serious":
                    if not serQueue.isEmpty():
                        patient = serQueue.dequeue()
                        print("Treating '%s' from Serious queue" % (patient))
                    else:
                        print("No patients in queue")
                else:
                    if not fairQueue.isEmpty():
                        patient = fairQueue.dequeue()
                        print("Treating '%s' from Fair queue" % (patient))
                    else:
                        print("No patients in queue")

        # handing of 'exit' command
        if command == "exit":
            print()
            print("Command: Exit")
            print()
            return
        
    file.close()

    
# print all of the queues, used in each condition
def printQueues(cQueue, fQueue, sQueue):
    print("Queues are:")
    print("Fair: %s" % (fQueue))
    print("Serious: %s" % (sQueue))
    print("Critical: %s" % (cQueue))

def main():

    # create the queues that will be used
    crit = Queue()
    fair = Queue()
    ser = Queue()

    readFile("ERsim.txt", crit, ser, fair)

main()
