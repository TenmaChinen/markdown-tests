import dj_setup
from classic_models.models import Office, Employee, Customer, Order, ProductLine, Product, OrderDetail, Payment
from pandas import DataFrame

query = Employee.objects.all()
query =  query.values()
df = DataFrame(data = query)
print(df)