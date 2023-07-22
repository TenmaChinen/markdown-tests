import dj_setup

from classic_models.models import Employee
from pandas import read_sql_query
import sqlite3, pdb

conn = sqlite3.connect('classic_models.db')
conn.execute('PRAGMA foreign_keys = ON')

cursor = conn.execute('SELECT * FROM employees')
l_field_names = [x[0] for x in cursor.description]

sql_pk_field = 'employee_number'
sql_fk_field = 'reports_to'
dj_fk_model = 'reported_employee'
dj_fk_field = 'employee_number'

for record in cursor:
    d_sqlite_record = dict(zip(l_field_names, record))

    d_foreign_data = {}

    employee_number = d_sqlite_record[sql_pk_field]
    reports_to = d_sqlite_record[sql_fk_field]

    if reports_to is not None:
        employee = Employee.objects.get( employee_number = employee_number )
        reported_employee = Employee.objects.get( employee_number = reports_to )

        employee.reported_employee = reported_employee
        employee.save()
