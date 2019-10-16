class Employee:
    empCount = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def __repr__(self):
        return self.name

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
    n = input()
    s = input()
    y = Employee(n,s)
    alist_final.append(y)
    y.displayEmployee()
    print("Total Employee %d" % Employee.empCount)
print(alist_final)