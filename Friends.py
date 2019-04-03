#  File: Friends.py
#  Description: Use linked lists to implement the friend functionality
#  Student's Name: Samuel Randall
#  Student's UT EID: spr699
#  Course Name: CS 313E 
#  Unique Number: 51465
#
#  Date Created: 11/7/17
#  Date Last Modified:11/12/17

# User is basically a stripped Node class
class User (object):
    def __init__(self,name):
        self.name = name
        self.friends = UnorderedList()
        self.next = None            # always do this -- saves a lot
                                  # of headaches later!

    def getData (self):
        return self.name            # returns a POINTER

    def getNext (self):
        return self.next            # returns a POINTER

    def setNext (self,newNext):
        self.next = newNext         # changes a POINTER

    def __str__(self):
        return str(self.name)

    
class UnorderedList ():

    def __init__(self):
        self.head = None

    def isEmpty (self):
        return self.head == None

    def add (self,item):
        # add a new Node to the beginning of an existing list
        temp = User(item)
        temp.setNext(self.head)
        self.head = temp

    def length (self):
        current = self.head
        count = 0

        while current != None:
         count += 1
         current = current.getNext()

        return count

    def search (self,item):
        current = self.head
        found = False

        while current != None and not found:
            if current.getData() == item:
                found = True
            current = current.getNext()

        return found


    # next few functions pulled from previous assignment
    def __str__ (self):
        current = self.head
        string = ""
        count = 0
        length = self.getLength()

        # maximum 10 items to a line
        for i in range(length):
            string += str(current.getData()) + "  "
            current = current.getNext()
            count += 1
            if count % 10 == 0:
                string += "/n"
            
        return string

    def getItem(self, item):
        current = self.head.getNext()
        found = False

        while not found:
            if current.getData().name == item:
                found = True
            else:
                current = current.getNext()

        return current.getData()
    
    def delete (self, item):
        #   Delete an item from an unordered list
        #   if found, return True; otherwise, return False
        current = self.head
        previous = None
        found = False

        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
            
        if found:
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())

        return found

# takes in the name of the file and the unordered list to work with
def readFile(file, Accounts):
    
    file = open(file)

    for line in file:

        line = line.split()

        command = line[0]

        # creates a person in the Accounts list
        if command == "Person":
            if Accounts.search(line[1]):
                print(line[1], "already has an account")
            else:
                Accounts.add(line[1])
                print(line[1], "now has an account")

        # adds people to each other's friends list's
        elif command == "Friend":
            if not Accounts.search(line[1]) or not Accounts.search(line[2]):
                if not Accounts.search(line[1]):
                    print(line[1], "does not have an account")
                else:
                    print(line[2], "does not have an account")
            
            elif line[1] == line[2]:
                print("A person cannot friend him/herself")
                
            else:
                current = Accounts.head
                found = False
                while current != None and not found:
                    if current.getData() == line[1]:
                        if current.friends.search(line[2]):
                            print(line[1], "and", line[2], "are already friends")
                        else:
                            current.friends.add(line[2])
                            print(line[1], "and", line[2], "are now friends")
                        found = True
                    
                    current = current.getNext()

                current = Accounts.head
                while current != None and not found:
                    if current.getData() == line[2]:
                        if not current.friends.search(line[1]):
                            current.friends.add(line[1])
                        found = True
                    
                    currrent = current.getNext()

        # removes two people from each other's friends list's
        elif command == "Unfriend":
            if not Accounts.search(line[1]) or not Accounts.search(line[2]):
                if not Accounts.search(line[1]):
                    print(line[1], "does not have an account")
                    
                else:
                    print(line[2], "does not have an account")
                    
            elif line[1] == line[2]:
                print("You cannot unfriend yourself")
                
            else:
                current = Accounts.head
                while current != None:
                    if current.getData() == line[1]: 
                        if current.friends.delete(line[2]):
                            print(line[1], "and", line[2], "are not longer friends")
                            
                        else:
                            print(line[1], "and", line[2], "were not friends")
                            
                        break
                    current = current.getNext()
                    
                # removing from other user's friend list
                current = Accounts.head
                while current != None:
                    if current.getData() == line[2]:
                        current.friends.delete(line[2])
                        break
                    
                    current = current.getNext()

        # when called will list out the friends of the called user 
        elif command == "List":
            if Accounts.search(line[1]):
                current = Accounts.head
                while current != None:
                    if current.getData() == line[1]:
                        
                        currentFriend = current.friends.head
                        
                        if currentFriend == None:
                            print(line[1], "has no friends.")
                            
                        else:
                            print(line[1], "friends list:")
                            
                            while currentFriend != None:
                                print(currentFriend.getData())
                                currentFriend = currentFriend.getNext()                               
                        break
                    
                    current = current.getNext()
            else:
                print(line[1], "does not have an account")

        # will check whether or not two people are friends                      
        elif command == "Query":
            if Accounts.search(line[1]) and Accounts.search(line[2]):
                current = Accounts.head
                friendStatus = False
                
                while current != None:
                    if current.getData() == line[1]:
                        friend = current.friends.head
                        
                        while friend != None:
                            if friend.getData() == line[2]:
                                friendStatus = True
                                break
                            
                            friend = friend.getNext()
                        break
                    current = current.getNext()
                if friendStatus:
                    print(line[1], "and", line[2], "are friends")
                else:
                    print(line[1], "and", line[2], "are not friends")
                            
            elif line[1] == line[2]:
                print("Users cannot query themselves")

            else:
                if not Accounts.search(line[1]):
                    print(line[1], "doesn't have an account")
                else:
                    print(line[2], "doesn't have an account")

        # exits the file
        elif command == "Exit":
            print("Exiting...")
            break
    

def main():
    # method call
    people = UnorderedList()
    readFile("FriendData.txt", people)
    
main()
