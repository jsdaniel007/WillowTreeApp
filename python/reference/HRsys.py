#!/usr/bin/env python

# used for processing payroll
class PayrollSystem:
	def calculate_payroll(self, employees):
		print('Calculating Payroll')
		print('===================')
		for employee in employees:
			print(f'Payroll for: {employee.id} -> {employee.name}')
			print(f'-> Check amount: {employee.calculate_payroll()}')
			print('')


# Common Generic Interface for employee types
class Employee:
	def __init__(self, id, name):
		self.id = idea
		self.name = name

# Distinct Class inheriting from Employee class
class SalaryEmployee(Employee):
	# remember we have the id and name accessible as variables from previous

	def __init__(self, id, name, weekly_salary):
		super().__init__(id, name) #In addition to the superclass init...
		self.weekly_salary = weekly_salary #do this as well

	def calculate_payroll(self):
		return self.weekly_salary

# Distinct Class inheriting from Employee class
class HourlyEmployee(Employee):

	def __init__(self, id, name, hours_worked, hour_rate):
		super().__init__(id, name) #In addition to the superclass init...
		self.hours_worked = hours_worked #do this as well
		self.hour_rate = hour_rate

	def calculate_payroll(self):
		return self.hours_worked * self.hour_rate

# Distinct Class inheriting from SalaryEmployee
class CommissionEmployee(SalaryEmployee):

	def __init__(self, id, name, weekly_salary, commission):
		super().__init__(id, name, weekly_salary)
		self.commission = commission

	def calculate_payroll(self):
		fixed = super().calculate_payroll()
		return fixed + self.commission
