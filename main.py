import unittest


class Person:
    def __init__(self, name, age, gender, salary):
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary
        self.wallet = 1000
        self.display()

    def display(self):
        print(
            f'Name: {self.name}, '
            f'Age: {self.age}, '
            f'Gender: {self.gender}, '
            f'Salary: {self.salary}, '
            f'Wallet: {self.wallet}'
        )

    def update(self, name, age, gender, salary):
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary

    def work(self):
        self.wallet += self.salary
        print(f'Wallet: {self.wallet}')

    def spend(self, amount):
        print(f'{amount = }, {self.wallet = }')
        if self.wallet >= amount:
            self.wallet -= amount
        else:
            print('Not enough money')
        print(f'Wallet: {self.wallet}')


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person('Gosha', 16, 'Male', 1000)

    '''def test_display(self):
        expected_output = 'Name: Gosha, Age: 16, Gender: Male, Salary: 1000, Wallet: 0'
        self.assertEqual(self.person.display(), expected_output)'''

    def test_update(self):
        self.person.update('Olya', 16, 'Female', 2000)
        self.assertEqual(self.person.name, 'Olya')
        self.assertEqual(self.person.age, 16)
        self.assertEqual(self.person.gender, 'Female')
        self.assertEqual(self.person.salary, 2000)

    def test_work(self):
        self.person.work()
        self.assertEqual(self.person.wallet, 2000)

    def test_spend_enough_money(self):
        self.person.spend(500)
        self.assertEqual(self.person.wallet, 500)

    '''def test_spend_not_enough_money(self):
        self.person.spend(2000)
        self.assertEqual(self.person.wallet, -500)'''


if __name__ == '__main__':
    unittest.main()
