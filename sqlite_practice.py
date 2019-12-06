class Employee:

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay

	@property
	def email(self):
		return '{}.{}@gmail.com'.format(self.first, self.last)

	@property
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def __repr__(self):
		return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)




import sqlite3

# conn = sqlite3.connect('employee.db')
conn = sqlite3.connect(':memory:')      # :memory: for test mode db

c = conn.cursor()

c.execute("""CREATE TABLE employees (
		first text,
		last text,
		pay iteger
		)""")

def insert_emp(emp):
	with conn:
		c.execute("INSERT INTO employees VALUES (:first,:last,:pay)", 
			{'first':emp.first,'last':emp.last, 'pay':emp.pay}) 
		# c.execute("INSERT INTO employees VALUES (?,?,?)",        | another way to INSERT
		# 	(emp_1.first, emp_1.last, emp_1.pay))                  | to DB


def get_emp_by_name(lastname):
	c.execute("SELECT * FROM employees WHERE last=:last",
	 	{'last':lastname})  #  Select data from database
	return c.fetchall()


def update_pay(emp, pay):
	with conn:
		c.execute("""UPDATE employees SET pay = :pay 
			WHERE first = :first AND last = :last""",
			{'first':emp.first, 'last': emp.last, 'pay': pay})

def remove_emp(emp):
	with conn:
		c.execute("DELETE from employees WHERE first = :first AND last = :last",
			{'first':emp.first, 'last': emp.last})

emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 80000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emp_by_name('Doe')
print(emps)

update_pay(emp_2, 95000)
remove_emp(emp_1)

emps = get_emp_by_name('Doe')
print(emps)
conn.close()



