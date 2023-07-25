import dj_setup
from classic_models.models import Office, Employee, Customer, Order, ProductLine, Product, OrderDetail, Payment
from pandas import DataFrame, set_option
set_option('display.max_columns', 1000)
set_option('display.width', 2000)

# EXERCISE 1

def get_exercise_1():
    query = Payment.objects.all()
    query = query[0:10]
    query = query.values()
    df = DataFrame(data=query)
    return df

# EXERCISE 2

def get_exercise_2():
    query = Payment.objects.all()[0:10]
    query = query.values('check_number')
    df = DataFrame(data=query)
    return df

# EXERCISE 3

def get_exercise_3():
    query = Payment.objects.all()
    query = query[0:10]
    query = query.values('payment_date')
    df = DataFrame(data=query)
    return df

# EXERCISE 4

def get_exercise_4():
    query = Payment.objects.all()
    query = query[0:10]
    query = query.values('amount')
    df = DataFrame(data=query)
    return df

# EXERCISE 5


def get_exercise_5():
    from django.db.models import F
    query = Payment.objects.all()
    query = query[0:10]
    query = query.annotate(
        customer_number=F('customer__customer_number')
    )
    query = query.values('customer_number')
    df = DataFrame(data=query)
    return df

# EXERCISE 6


def get_exercise_6():
    query = Payment.objects.all()
    query = query.order_by('check_number')
    query = query[0:10]
    query = query.values('check_number')
    df = DataFrame(data=query)
    return df

# EXERCISE 7


def get_exercise_7():
    query = Payment.objects.all()
    query = query.order_by('-check_number')
    query = query[0:10]
    query = query.values('check_number')
    df = DataFrame(data=query)
    return df

# EXERCISE 8


def get_exercise_8():
    query = Payment.objects.all()
    query = query.order_by('payment_date')
    query = query[0:10]
    query = query.values('payment_date')
    df = DataFrame(data=query)
    return df

# EXERCISE 9


def get_exercise_9():
    query = Payment.objects.all()
    query = query.order_by('-payment_date')
    query = query[0:10]
    query = query.values('payment_date')
    df = DataFrame(data=query)
    return df

# EXERCISE 10


def get_exercise_10():
    from django.db.models import F

    query = Payment.objects.all()
    query = query.annotate(customer_number=F('customer__customer_number'))
    query = query.order_by('customer_number')
    query = query[0:10]
    query = query.values('customer_number')
    df = DataFrame(data=query)
    return df

# EXERCISE 11


def get_exercise_11():
    from django.db.models import F

    query = Payment.objects.all()
    query = query.annotate(customer_number=F('customer__customer_number'))
    query = query.order_by('-customer_number')
    query = query[0:10]
    query = query.values('customer_number')
    df = DataFrame(data=query)
    return df

# EXERCISE 12


def get_exercise_12():
    from django.db.models import F

    query = Payment.objects.all()
    # query = query.annotate(customer_number=F('check_number'))
    query = query[0:10]
    query = query.values('check_number', 'payment_date')
    df = DataFrame(data=query)
    return df

# EXERCISE 13


def get_exercise_13():
    query = Payment.objects.all()
    query = query.values('check_number', 'amount')
    query = query[0:1]
    df = DataFrame(data=query)
    return df

# EXERCISE 14


def get_exercise_14():
    from django.db.models import F

    query = Payment.objects.all()
    query = query.annotate(
        customer_number=F('customer__customer_number')
    )
    query = query[0:10]
    query = query.values('check_number', 'customer_number')
    df = DataFrame(data=query)
    return df

# EXERCISE 15


def get_exercise_15():
    from django.db.models import F

    query = Payment.objects.all()
    query = query.annotate(customer_number=F('customer__customer_number'))
    query = query.values('customer_number')
    query = query.distinct()
    query = query[0:10]
    df = DataFrame(data=query)
    return df

# EXERCISE 16


def get_exercise_16():

    # Solution A
    from django.db.models import F
    query = Payment.objects.all()
    query = query.annotate(smallest_payment=F('amount'))
    query = query.order_by('amount')
    query = query.values('smallest_payment')
    query = query[0:1]
    df = DataFrame(data=query)

    # Solution B
    from django.db.models import Min
    query = Payment.objects.all()
    result = query.aggregate(smallest_payment=Min('amount'))
    
    result['smallest_payment'] = [result['smallest_payment']]
    df = DataFrame(data=result)
    return df

# EXERCISE 17


def get_exercise_17():
    # Solution A
    from django.db.models import F
    query = Payment.objects.all()
    query = query.annotate(largest_payment=F('amount'))
    query = query.order_by('-amount')
    query = query.values('largest_payment')
    query = query[0:1]
    df = DataFrame(data=query)

    # Solution B
    from django.db.models import Max
    query = Payment.objects.all()
    result = query.aggregate(largest_payment=Max('amount'))

    result['largest_payment'] = [result['largest_payment']]
    df = DataFrame(data=result)
    return df

# EXERCISE 18


def get_exercise_18():
    from django.db.models import Avg
    query = Payment.objects.all()
    result = query.aggregate(amount_average=Avg('amount'))
    result['amount_average'] = [result['amount_average']]

    df = DataFrame(data=result)
    return df

# EXERCISE 19


def get_exercise_19():

    # Solution A
    query = Payment.objects.all()
    query = query.order_by('payment_date')
    query = query.values('payment_date')
    result = query.first()

    # Solution B
    from django.db.models import Min
    query = Payment.objects.all()
    result = query.aggregate(payment_date=Min('payment_date'))

    result['payment_date'] = [result['payment_date']]
    df = DataFrame(data=result)
    return df

# EXERCISE 20


def get_exercise_20():

    # Solution A
    query = Payment.objects.all()
    query = query.order_by('-payment_date')
    query = query.values('payment_date')
    result = query.first()

    # Solution B
    from django.db.models import Max
    query = Payment.objects.all()
    result = query.aggregate(payment_date=Max('payment_date'))

    result['payment_date'] = [result['payment_date']]
    df = DataFrame(data=result)
    return df

# EXERCISE 21


def get_exercise_21():

    from django.db.models import Sum, F
    query = Payment.objects.all()
    query = query.annotate(customer_number=F('customer__customer_number'))
    query = query.values('customer_number')
    query = query.annotate(total_amount=Sum('amount'))
    query = query[0:10]

    df = DataFrame(data=query)
    return df

# EXERCISE 22


def get_exercise_22():

    from django.db.models import Avg, F
    query = Payment.objects.all()
    query = query.annotate(customer_number=F('customer__customer_number'))
    query = query.values('customer_number')
    query = query.annotate(average_amount=Avg('amount'))
    query = query[0:10]

    df = DataFrame(data=query)
    return df

# EXERCISE 23


def get_exercise_23():

    from django.db.models import Count
    query = Payment.objects.all()
    # total_rows = query.count()
    result = query.aggregate(total_rows=Count('*'))

    result['total_rows'] = [result['total_rows']]
    df = DataFrame(data=result)
    return df

# EXERCISE 24


def get_exercise_24():

    from django.db.models import Count, F

    query = Payment.objects.all()
    query = query.annotate(customer_number=F('customer__customer_number'))
    query = query.values('customer_number')
    query = query.distinct()
    query = query.annotate(count=Count('customer_number'))
    query = query[0:10]

    df = DataFrame(data=query)
    return df

# EXERCISE 25


def get_exercise_25():

    from django.db.models import F

    query = Payment.objects.annotate(
        customer_number=F('customer__customer_number'))
    query = query.filter(customer_number__lt=200)
    query = query.values('customer_number')
    query = query[0:10]

    df = DataFrame(data=query)
    return df

# EXERCISE 26


def get_exercise_26():

    from django.db.models import F

    query = Payment.objects.annotate(
        customer_number=F('customer__customer_number'))
    query = query.filter(
        customer_number__gte=200,
        customer_number__lte=400
    )
    query = query.values('customer_number')
    query = query[0:10]

    df = DataFrame(data=query)
    return df

# EXERCISE 27


def get_exercise_27():

    from django.db.models import F

    query = Payment.objects.annotate(
        customer_number=F('customer__customer_number'))
    query = query.filter(customer_number__gt=400)
    query = query.values('customer_number')
    query = query[0:10]

    df = DataFrame(data=query)
    return df

# EXERCISE 28


def get_exercise_28():

    query = Payment.objects.filter(payment_date__lt='2003-12-31')
    query = query.values('payment_date')
    query = query[0:10]

    df = DataFrame(data=query)
    return df

# EXERCISE 29


def get_exercise_29():

    query = Payment.objects.filter(
        payment_date__gte='2003-12-31',
        payment_date__lte='2004-12-31'
    )
    query = query.values('payment_date')
    query = query[0:10]

    df = DataFrame(data=query)
    return df

# EXERCISE 30


def get_exercise_30():

    query = Payment.objects.filter(payment_date='2005-02-02')
    query = query.values('payment_date')
    query = query[0:10]

    df = DataFrame(data=query)
    return df

# EXERCISE 31


def get_exercise_31():

    from django.db.models import Avg

    result = Payment.objects.aggregate(average_amount=Avg('amount'))
    average_amount = result['average_amount']

    query = Payment.objects.filter(amount__lt=average_amount)
    query = query.order_by('-amount')
    query = query.values('amount')
    query = query[0:10]

    df = DataFrame(data=query)
    return df

# EXERCISE 32


def get_exercise_32():

    from django.db.models import Avg

    result = Payment.objects.aggregate(average_amount=Avg('amount'))
    average_amount = result['average_amount']

    query = Payment.objects.filter(amount__gt=average_amount)
    query = query.values('amount')
    query = query[0:10]

    df = DataFrame(data=query)
    return df

# EXERCISE 33


def get_exercise_33():
    from django.db.models.functions import Lower
    from django.db.models import F

    query = Payment.objects.all()
    query = query.annotate(customer_name=F('customer__customer_name'))

    l_fields = ['customer_name', 'payment_date', 'amount']
    query = query.values_list(*l_fields)
    query = query.order_by(Lower('customer_name'))
    query = query[0:10]

    df = DataFrame(data=query, columns=l_fields)
    return df

# EXERCISE 34


def get_exercise_34():

    from django.db.models.functions import Lower
    from django.db.models import Max

    query = Payment.objects.all()
    query = query.values('customer__customer_name')
    query = query.annotate(
        phone=Max('customer__phone'),
        payment_date=Max('payment_date')
    )
    query = query.order_by(Lower('customer__customer_number'))
    query = query[0:10]

    df = DataFrame(data=query)
    return df


# EXERCISE 35

def get_exercise_35():

    from django.db.models.functions import Lower
    from django.db.models import Count

    query = Customer.objects.all()
    query = query.values('country')
    query = query.annotate(count=Count('*'))
    query = query.order_by(Lower('country'))
    query = query[0:10]

    df = DataFrame(data=query)
    return df

# EXERCISE 36


def get_exercise_36():

    from django.db.models.functions import Lower
    from django.db.models import Count, F

    query = Payment.objects.all()
    query = query.annotate(country=F('customer__country'))
    query = query.values('country')
    query = query.annotate(payments=Count('check_number'))
    query = query.order_by(Lower('country'))
    query = query[0:10]

    df = DataFrame(data=query)
    return df

# EXERCISE 37


def get_exercise_37():

    query = Order.objects.all()
    query = query.values('order_number', 'order_date')
    query = query[0:10]

    df = DataFrame(data=query)
    return df


# EXERCISE 38

def get_exercise_38():

    from django.db.models import F

    query = Order.objects.all()
    query = query.annotate(customer_name=F('customer__customer_name'))

    l_fields = ['customer_name', 'order_number', 'order_date']
    query = query.values_list(*l_fields)
    query = query[0:10]

    df = DataFrame(data=query, columns=l_fields)
    return df

# EXERCISE 39


def get_exercise_39():

    from django.db.models import Sum, F

    query = OrderDetail.objects.all()
    query = query.annotate(order_number=F('order__order_number'))
    query = query.values('order_number')
    query = query.annotate(
        order_date=F('order__order_date'),
        order_value=Sum(F('quantity_ordered') * F('price_each'))
    )
    query = query[0:10]

    df = DataFrame(data=query)
    return df

# EXERCISE 40


def get_exercise_40():

    from django.db.models import Sum, Max, F

    query = OrderDetail.objects.all()
    query = query.annotate(order_number=F('order__order_number'))
    query = query.values('order_number')
    query = query.annotate(
        customer_name=F('order__customer__customer_name'),
        order_value=Sum(F('quantity_ordered') * F('price_each'))
    )

    query = query[0:10]
    l_fields = ['customer_name', 'order_number', 'order_value']
    query = query.values_list(*l_fields)

    df = DataFrame(data=query, columns=l_fields)
    df.order_value = df.order_value.map('{:,.2f}'.format)
    return df

# EXERCISE 41


def get_exercise_41():

    from django.db.models import Sum, Max, F
    from django.db.models.functions import Lower

    query = OrderDetail.objects.all()
    query = query.annotate(
        customer_number=F('order__customer__customer_number')
    )
    query = query.values('customer_number')
    query = query.annotate(
        customer_name=F('order__customer__customer_name'),
        values_of_all_orders=Sum(F('quantity_ordered') * F('price_each'))
    )
    query = query[0:10]
    query = query.values('customer_name', 'values_of_all_orders')

    df = DataFrame(data=query)
    df.values_of_all_orders = df.values_of_all_orders.map('{:,.2f}'.format)
    return df

# EXERCISE 42


def get_exercise_42():

    from django.db.models import F
    query = OrderDetail.objects.all()
    query = query.annotate(
        customer_number=F('order__customer__customer_number'),
        order_number=F('order__order_number'),
        product_name=F('product__product_name'),
    )
    query = query[0:10]
    query = query.values('customer_number', 'order_number', 'product_name')

    df = DataFrame(data=query)
    return df

# EXERCISE 43


def get_exercise_43():
    query = Employee.objects.filter(reported_employee__isnull=False)
    query = query.values('last_name', 'reported_employee__last_name')
    query = query[0:10]

    df = DataFrame(data=query)
    return df

# EXERCISE 44


def get_exercise_44():

    from django.db.models import F

    query = Employee.objects.filter(reported_employee__isnull=False)
    query = query.annotate(
        manager_first_name=F('reported_employee__first_name'),
        manager_last_name=F('reported_employee__last_name')
    )

    l_fields = ['manager_first_name',
                'manager_last_name', 'first_name', 'last_name']
    query = query.values_list(*l_fields)
    query = query.order_by('manager_last_name')
    query = query[0:10]

    df = DataFrame(data=query, columns=l_fields)
    return df


if __name__ == '__main__':

    for idx in [12]:
        # for idx in range(1,45):
        func = eval(f'get_exercise_{idx}')
        df = func()
        print(df)
