class Stud:
    def __init__(self,roll,name):
        self.roll=roll
        self.name=name
        self.nextstud=None

    def getInfo(self):
        print("Student Details:"+str(self.roll)+":"+(self.name))
        return

class StudList:
    def __init__(self):
        self.start=None
        self.last=None

   
    def traverse(self):
        if(self.start==None):
            print("The List is Empty!")
        else:
            print("Traversing the contents of the list:")
            ptr=self.start
            while(ptr!=None):
                ptr.getInfo()
                ptr=ptr.nextstud
   
    def appendstart(self,roll,name):
        newstud=Stud(roll,name)
        newstud.nextstud=self.start
        self.start=newstud

    
    def appendlast(self,roll,name):
        newstud=Stud(roll,name)
        if(self.start==None):
            self.start=newstud
            return
        last=self.start
        while(last.nextstud):
            last=last.nextstud
        last.nextstud=newstud

    
    def insert_position(self,pos,roll,name):
        newstud=Stud(roll,name)
        ptr=self.start
        for i in range(pos-1):
            ptr=ptr.nextstud
        newstud.roll=roll
        newstud.name=name
        newstud.nextstud=ptr.nextstud
        ptr.nextstud=newstud
 
   
    def delete_first(self):
        if(self.start==None):
            print("Nothing to remove")
            return None
        self.start=self.start.nextstud
    
    
    def deletelast(self):
        if self.start == None:
            print("List is Empty!,So delete of node is not possible.")
        else:
            ptr=self.start
            while ptr.nextstud.nextstud !=None:
                ptr=ptr.nextstud
            ptr.nextstud=None
    
    
    def delete_position(self,roll):
        if self.start is None:
            print("Can't delete list is Empty!")
            return
        if roll==self.start.roll:
            self.start=self.start.nextstud
            return
        ptr=self.start
        while ptr.nextstud !=None:
            if roll==ptr.nextstud.roll:
                break
            ptr=ptr.nextstud
        if ptr.nextstud ==None:
            print("Node is not Present!")
        else:
            ptr.nextstud=ptr.nextstud.nextstud

a=int(input("Enter the total no of students:"))
i=1
sycs = StudList()
while(i<=a):
    b=input("Enter the name:")
    c=int(input("Enter the roll no:"))
    z=Stud(c,b)
    sycs.appendlast(c,b)
    
    i+=1
sycs.traverse()
sycs.appendstart(101,"Allen")
sycs.traverse()
sycs.appendlast(106,"Niki")
sycs.traverse()
sycs.insert_position(4,105,"Julie")
sycs.traverse()
sycs.delete_first()
sycs.traverse()
sycs.deletelast()
sycs.traverse()
sycs.delete_position(104)
sycs.traverse()







    
    



