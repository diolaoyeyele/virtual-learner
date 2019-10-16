
class Employee:

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


alist_final =[]
for _ in range(2):
    n = input()
    s = input()
    y = Employee(n,s)
    alist_final.append(y)
    y.displayEmployee()
    print("Total Employee %d" % Employee.empCount)

print([str(x) for x in alist_final])