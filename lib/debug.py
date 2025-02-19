#!/usr/bin/env python3
#lib/testing/debug.py
from __init__ import CONN, CURSOR
from department import Department

import ipdb

Department.drop_table()
Department.create_table()

payroll = Department("Payroll", "Building A, 5th Floor")
print(payroll)  # <Department None: Payroll, Building A, 5th Floor>

payroll.save()  # Persist to db, assign object id attribute
print(payroll)  # <Department 1: Payroll, Building A, 5th Floor>

hr = Department("Human Resources", "Building C, East Wing")
print(hr)  # <Department None: Human Resources, Building C, East Wing>
hr.save()  # Persist to db, assign object id attribute
print(hr)  # <Department 2: Human Resources, Building C, East Wing>

hr.name = 'HR'
hr.location = "Building F, 10th Floor"
hr.update()
print(hr)  # <Department 2: Human Resources, Building C, East Wing>

it = Department("IT support", "Building D, 5th Floor")
print(it)
it.save()
print(it)

sales = Department("Sales and Marketing", "Building B, 4th Floor")
print(sales)
sales.save()
print(sales)


print("Delete Payroll")
payroll.delete()  # delete from db table, object still exists in memory
print(payroll) 

ipdb.set_trace()