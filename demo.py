


try:
    print('inside'
          ' try')
    num = 10/1
    print('try successful')
except ArithmeticError:
    print('Divide By Zero')
else:
    print('inside else block')
finally:
    print('Finally Block...')  #resource -->


import sys
sys.exit(0)
class Employee:
    count = 1

    def __init__(self,enm,eage):
        self.empId = Employee.count     # eid --> Autoincrement -- object creation
        self.empName = enm
        self.empAge = eage
        Employee.count = Employee.count + 1

    def __str__(self):
        return f'''[{self.empId},{self.empName},{self.empAge}]'''

    def __repr__(self):
        return str(self)




employees = []  #excepted -- 10 emp details
def take_input_from_user():
    name = input('Enter Your Name : ')
    age = None
    try:
        age = int(input('Enter Your Age : '))
        emp = employees[1]

    except ValueError as e:
        #print(e.)
        print('Invalid Age entered....')
    except IndexError as e:
        pass
    except:             #BaseException
        pass
    emp = Employee(name,age)
    employees.append(emp)


if __name__ == '__main__':

    for item in range(10):
        take_input_from_user()

    print('here is the list of employee details')
    print(employees)