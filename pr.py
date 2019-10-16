class Employee:
    'Common base class for all employeees'
    empCount = 0
    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary
        Employee.empCount += 1
    def __str__(self):
        return '{}(name={}, salary={})'.format(
                        self.__class__.__name__,
                        self.name,
                        self.salary)
    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print ("Name : ", self.name, ", Salary: ",self.salary)
global emp1
global emp2
global n
global s
emp1 = ''
emp2 = ''
alist = [emp1,emp2]
alist_final =[]
for y in alist:
    #global y
    y = Employee('n',2)
   # hemp = y
    alist_final.append(y)
    y.displayEmployee()
    #emp2.displayEmployee()
    print("Total Employee %d" % Employee.empCount)


#emp1 =  Employee(n,s)
#this is a fake comment
#emp2 = Employee("Manni",5000)
print([str(x) for x in alist_final])
#emp2.displayEmployee()
'''for x in alist:
    print(x.name)
    sal = str(input("enter salary"))
    if sal == str(x.salary):
        print ("you are correct")
    else:
        print ("that is incorrect")'''
