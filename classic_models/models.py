from django.db import models

class Office(models.Model):
    office_code = models.CharField(max_length=10, primary_key=True)
    city = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=50, null=False)
    address_line_1 = models.CharField(max_length=50, null=True)
    address_line_2 = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    postal_code = models.CharField(max_length=15, null=True)
    territory = models.CharField(max_length=10, null=True)


class Employee(models.Model):
    employee_number = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=50, null=False)
    first_name = models.CharField(max_length=50, null=False)
    extension = models.CharField(max_length=10, null=False)
    email = models.CharField(max_length=100, null=False)
    job_title = models.CharField(max_length=50, null=False)
    office = models.ForeignKey(to=Office, on_delete=models.CASCADE, max_length=10, null=False)
    # reported_employee = models.ForeignKey(to='self', on_delete=models.CASCADE, default=None, null=True)
    reported_employee = models.ForeignKey(to='self', on_delete=models.CASCADE, default=None, null=True, related_name='supervised_employee')


class Customer(models.Model):
    customer_number = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=50, null=False)
    contact_last_name = models.CharField(max_length=50, null=False)
    contact_first_name = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=50, null=False)
    address_line_1 = models.CharField(max_length=50, null=False)
    address_line_2 = models.CharField(max_length=50, null=True, default=None)
    city = models.CharField(max_length=50, null=False)
    state = models.CharField(max_length=50, default=None, null=True)
    postal_code = models.CharField(max_length=15, default=None, null=True)
    country = models.CharField(max_length=50, null=False)
    credit_limit = models.FloatField(default=None, null=True)
    sales_rep_employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE, default=None, null=True)
    # sales_rep_employee_number = models.ForeignKey(to=Employee, on_delete=models.CASCADE, default=None, null=True)

class Order(models.Model):
    order_number = models.AutoField(primary_key=True)
    order_date = models.DateField(null=False)
    required_date = models.DateField(null=False)
    shipped_date = models.DateField(null=True, default=None)
    status = models.CharField(max_length=15, null=False)
    comments = models.TextField(null=True)
    # customer_number = models.ForeignKey(to=Customer, on_delete=models.CASCADE, null=False)
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE, null=False)


class Payment(models.Model):
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE, null=True)
    # customer_number = models.ForeignKey(to=Customer, on_delete=models.CASCADE, null=True)
    check_number = models.CharField(max_length=50, null=False)
    payment_date = models.DateField(null=False)
    amount = models.FloatField(null=False)

    class Meta:
        unique_together = ['customer', 'check_number']


class ProductLine(models.Model):
    product_line = models.CharField(max_length=50, primary_key=True, null=False)
    text_description = models.CharField(max_length=4000, default=None, null=True)
    # html_description TEXT
    # image BYTEA


class Product(models.Model):
    product_code = models.CharField(max_length=15, primary_key=True)
    product_name = models.CharField(max_length=70, null=False)
    product_line = models.ForeignKey(to=ProductLine, on_delete=models.CASCADE, max_length=50, null=False)
    product_scale = models.CharField(max_length=10, null=False)
    product_vendor = models.CharField(max_length=50, null=False)
    product_description = models.TextField(null=False)
    quantity_in_stock = models.PositiveSmallIntegerField(null=False)
    buy_price = models.FloatField(null=False)
    msrp = models.FloatField(null=False)


class OrderDetail(models.Model):
    # order_number = models.ForeignKey(to=Order, on_delete=models.CASCADE, null=False)
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, null=False)
    # product_code = models.ForeignKey(to=Product, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, null=False)
    quantity_ordered = models.IntegerField(null=False)
    price_each = models.FloatField(null=False)
    order_line_number = models.SmallIntegerField(null=False)

    class Meta:
        unique_together = ['order', 'product']
