class Courses:   
    def __init__(self):
        self.courselist=[]
        self.units=0        
    def addsub(self):
       print("your current courses are:")
       print(person.courselist)
       x=input("To add a course enter 1; To remove a course enter 2 ")
       if(x=='1'):
           name=input("please enter the new course name ")
           unit1=int(input("enter its unit "))
           person.courselist.append(name)
           person.units+=unit1
           thisdict[name]={}
           thisdict.get(name)["unit"]=unit1
       if(x=='2'):
           name=input("which course you want to remove ")
           if name in person.courselist:
               person.courselist.remove(name)
               person.units-=thisdict.get(name)["unit"]
               thisdict.pop(name)
           else:
               print("error")
    def gmeet(self):
        print("your current courses are:")
        print(person.courselist)
        x=input("to add a link enter 1 to remove enter 2 ")
        cname=input("please enter the course name ")
        if(x=='1'):
            url=input("please enter the link for gmeet ")
            if cname in person.courselist:
               thisdict.get(cname)["glink"]=url
            else:
               print("error")
        if(x=='2'):
            thisdict.get(cname).pop("glink")
    def notes(self):
        print("your current courses are:")
        print(person.courselist)
        x=input("to add a note enter 1 to remove enter 2 ")
        cname=input("please enter the course name ")
        if(x=='1'):
            note1=input("please enter the note ")
            if cname in person.courselist:
               thisdict.get(cname)["note"]=note1
            else:
               print("error")
        if(x=='2'):
            thisdict.get(cname).pop("note")
    def material(self):
        print("your current courses are:")
        print(person.courselist)
        x=input("to add a resource material enter 1 to remove enter 2 ")
        cname=input("please enter the course name ")
        if(x=='1'):
            rm=input("please enter the material ")
            if cname in person.courselist:
               thisdict.get(cname)["material"]=rm
            else:
               print("error")
        if(x=='2'):
            thisdict.get(cname).pop("material")
    def summary(self):
        print("your current courses are:")
        print(person.courselist)
        print("the total units till now")
        print(person.units)
    def detail(self):
        print("your current courses are:")
        print(person.courselist)
        x=input("which course details do you want ")
        for a,b in thisdict.get(x).items():
            print(a,b)           
person=Courses()
y=100
thisdict={}
while(y!=0):
    print("enter 1 to add or subract a course")
    print("enter 2 to add or remove gmeet link")
    print("enter 3 to add or remove notes")
    print("enter 4 to add or remove resource material")
    print("enter 5 to print all the details of any course")
    print("enter 6 to see course list and total units")
    print("enter 0 to exit")
    choice=input()
    if(choice=='1'):
        person.addsub()
    if(choice=='2'):
        person.gmeet()
    if(choice=='3'):
        person.notes()
    if(choice=='4'):
        person.material()
    if(choice=='5'):
        person.detail()    
    if(choice=='6'):
        person.summary()                 
    if(choice=='0'):
        print("thanks for visiting")
        break
