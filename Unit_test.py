import unittest
from unittest.mock import patch
import requests

class Employee:

	raise_amt = 1.05

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

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

	def monthly_schedule(self, month):
		response = requests.get(f'http://company.com/{self.last}/{month}')
		if response.ok:
			return response.text
		else:
			return 'Bad response!'



class TestEmployee(unittest.TestCase):

	
	@classmethod
	def setUpClass(cls):
		print('setUpClass')

	@classmethod
	def tearDownClass(cls):
		print('tearDownCLass') 

	def setUp(self):
		print('setUp')
		self.emp_1 = Employee('Corey', 'Schafer', 50000)
		self.emp_2 = Employee('Sue', 'Smith', 60000)

	def tearDown(self):
		print('tearDown\n')

	def test_email(self):
		print('test_email')
		self.assertEqual(self.emp_1.email, 'Corey.Schafer@gmail.com')
		self.assertEqual(self.emp_2.email, 'Sue.Smith@gmail.com')

		self.emp_1.first = 'John'
		self.emp_2.first = 'Jane'

		self.assertEqual(self.emp_1.email, 'John.Schafer@gmail.com')
		self.assertEqual(self.emp_2.email, 'Jane.Smith@gmail.com')

	def test_fullname(self):
		print('test_fullname')
		self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
		self.assertEqual(self.emp_2.fullname, 'Sue Smith')

		self.emp_1.first = 'John'
		self.emp_2.first = 'Jane'

		self.assertEqual(self.emp_1.fullname, 'John Schafer')
		self.assertEqual(self.emp_2.fullname, 'Jane Smith')

	def test_apply_raise(self):
		print('test_apply_raise')
		self.emp_1.apply_raise()
		self.emp_2.apply_raise()

		self.assertEqual(self.emp_1.pay, 52500)
		self.assertEqual(self.emp_2.pay, 63000)

	def test_monthly_schedule(self):
		with patch('requests.get') as mocked_get:
			mocked_get.return_value.ok = True
			mocked_get.return_value.text = 'Success'

			schedule = self.emp_1.monthly_schedule('May')
			mocked_get.assert_called_with('http://company.com/Schafer/May')
			self.assertEqual(schedule, 'Success')

			mocked_get.return_value.ok = False

			schedule = self.emp_2.monthly_schedule('June')
			mocked_get.assert_called_with('http://company.com/Smith/June')
			self.assertEqual(schedule, 'Bad response!')


if __name__ == "__main__":
	unittest.main()