import dj_setup

from classic_models.models import Office, Employee, Customer, Order, ProductLine, Product, OrderDetail, Payment
from pandas import read_sql_query
import sqlite3, pdb

conn = sqlite3.connect('classic_models.db')
conn.execute('PRAGMA foreign_keys = ON')

l_table_names = ['offices', 'employees', 'customers', 'orders', 'product_lines', 'products', 'order_details', 'payments']
d_models = dict(
    offices=Office, employees=Employee, customers=Customer, orders=Order,
    product_lines=ProductLine, products=Product, order_details=OrderDetail, payments=Payment)

d_fk = dict(
    offices=[],
    employees=[(Office, 'office_code', 'office', 'office_code'),(Employee, 'reports_to','reported_employee', 'employee_number')],
    customers=[(Employee, 'sales_rep_employee_number', 'sales_rep_employee', 'employee_number')],
    orders=[(Customer, 'customer_number', 'customer', 'customer_number')], product_lines=[],
    products=[(ProductLine, 'product_line', 'product_line', 'product_line')],
    order_details=[(Order, 'order_number' , 'order', 'order_number'), (Product, 'product_code' , 'product', 'product_code')],
    payments=[(Customer, 'customer_number', 'customer', 'customer_number')]
)

for idx, table_name in enumerate(l_table_names):
    print(table_name)
    Model = d_models[table_name]
    sql_query = f'SELECT * FROM {table_name}'
    cursor = conn.execute(sql_query)
    l_field_names = [x[0] for x in cursor.description]

    for record in cursor:
        d_sqlite_record = dict(zip(l_field_names, record))

        if table_name == 'product_lines':
            d_sqlite_record.pop('html_description')
            d_sqlite_record.pop('image')

        d_foreign_data = {}

        for ForeignModel, sqlite_fk_field, dj_fk_model, dj_fk_field in d_fk[table_name]:
            
            sql_fk_value = d_sqlite_record.pop(sqlite_fk_field)

            if ForeignModel != Model and sql_fk_value is not None :
                
                d_query = { dj_fk_field: sql_fk_value }
                foreign_model = ForeignModel.objects.get(**d_query)

                d_foreign_data[dj_fk_model] = foreign_model

        try:
            model = Model(**d_sqlite_record, **d_foreign_data)
            model.save()
        except BaseException as error:
            print(error)
            pdb.set_trace()
