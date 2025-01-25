# Задание №1
import random


bonus = int(random.randint(10, 50) * 1000)
determinant = random.choice([True, False])
salary = int(input("What is your salary: "))
if determinant:
    salary_bonus = salary + bonus
    print(f"${salary_bonus}")
else:
    print(f"${salary}")
