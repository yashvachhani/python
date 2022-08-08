# pyhton object-oriented programming

class Employee:
   
   num_of_emps = 0
   raise_amount = 1.04

   def __init__(self,first,last,pay):
      self.first = first
      self.last = last
      self.pay = pay
      self.email = first + '.' + last + '@company.com'
      Employee.num_of_emps += 1

   def fullname(self):
      return f'{self.first}  {self.last}'

   def apply_raise(self):
      self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('yash','vachhani',88000)
emp_2 = Employee('tom','thomas',88000) 

print(emp_1.fullname())
print(emp_1.email)

print(Employee.fullname(emp_2))

# class variable and instancs variable
# give raise useing class variable

emp_2.raise_amount = 1.05

print(emp_1.pay)
print(emp_2.pay)
Employee.apply_raise(emp_1)
emp_2.apply_raise()
print(emp_1.pay)
print(emp_2.pay)

print(Employee.num_of_emps)

# class methods and staticmethods

