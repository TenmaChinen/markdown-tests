import subprocess, json, re

def execute_sql(sql):
    sql = sql.replace('"','\\"').replace('\n',' ')

    result = subprocess.Popen(
        f'set "PGPASSWORD=IlovePostgreSQL" && psql -U postgres -d \"classic_models\" -c "{sql} --quiet"',
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )

    stdout, stderr = result.communicate()
    output = stdout.decode('utf-8').replace('\r','').rstrip()
    output = re.sub(pattern=r'\n\([0-9]{1,4} rows?\)', repl='', string=output)
    return output

def get_exercise_1():
    sql = \
    '''
        SELECT * FROM payments
        LIMIT 10;
    '''
    return sql

def get_exercise_2():
    sql = \
    '''
        SELECT check_number FROM payments
        LIMIT 10;
    '''
    return sql

def get_exercise_3():
    sql = \
    '''
        SELECT payment_date FROM payments
        LIMIT 10;
    '''
    return sql

def get_exercise_4():
    sql = \
    '''
        SELECT amount FROM payments
        LIMIT 10;
    '''
    return sql

def get_exercise_5():
    sql = \
    '''
        SELECT customer_number FROM payments
        LIMIT 10;
    '''
    return sql

def get_exercise_6():
    sql = \
    '''
        SELECT check_number FROM payments
        ORDER BY check_number
        LIMIT 10;
    '''
    return sql

def get_exercise_7():
    sql = \
    '''
        SELECT check_number FROM payments
        ORDER BY check_number DESC
        LIMIT 10;
    '''
    return sql

def get_exercise_8():
    sql = \
    '''
        SELECT payment_date FROM payments
        ORDER BY payment_date
        LIMIT 10;
    '''
    return sql

def get_exercise_9():
    sql = \
    '''
        SELECT payment_date FROM payments
        ORDER BY payment_date DESC
        LIMIT 10;
    '''
    return sql

def get_exercise_10():
    sql = \
    '''
        SELECT customer_number FROM payments
        ORDER BY customer_number
        LIMIT 10;
    '''
    return sql

def get_exercise_11():
    sql = \
    '''
        SELECT customer_number FROM payments
        ORDER BY customer_number DESC
        LIMIT 10;
    '''
    return sql

def get_exercise_12():
    sql = \
    '''
        SELECT check_number, payment_date FROM payments
        LIMIT 10;
    '''
    return sql

def get_exercise_13():
    sql = \
    '''
        SELECT check_number, amount FROM payments
        LIMIT 1;
    '''
    return sql

def get_exercise_14():
    sql = \
    '''
        SELECT check_number, customer_number FROM payments
        LIMIT 10;
    '''
    return sql

def get_exercise_15():
    sql = \
    '''
        SELECT DISTINCT(customer_number) FROM payments
        LIMIT 10;
    '''
    return sql

def get_exercise_16():
    sql = \
    '''
        SELECT MIN(amount) AS "smallest payment" FROM payments;
    '''
    return sql

def get_exercise_17():
    sql = \
    '''
        SELECT MAX(amount) AS "largest payment" FROM payments;
    '''
    return sql

def get_exercise_18():
    sql = \
    '''
        SELECT AVG(amount) FROM payments;
    '''
    return sql

def get_exercise_19():
    sql = \
    '''
        SELECT MIN(payment_date) FROM payments;
    '''
    return sql

def get_exercise_20():
    sql = \
    '''
        SELECT MAX(payment_date) FROM payments;
    '''
    return sql

def get_exercise_21():
    sql = \
    '''
        SELECT customer_number, SUM(amount) FROM payments
        GROUP BY customer_number
        LIMIT 10;
    '''
    return sql

def get_exercise_22():
    sql = \
    '''
        SELECT customer_number, AVG(amount) FROM payments
        GROUP BY customer_number
        LIMIT 10;
    '''
    return sql

def get_exercise_23():
    sql = \
    '''
        SELECT COUNT(*) FROM payments
        LIMIT 10;
    '''
    return sql

def get_exercise_24():
    sql = \
    '''
        SELECT COUNT(DISTINCT(customer_number)) FROM payments
        LIMIT 10;
    '''
    return sql

def get_exercise_25():
    sql = \
    '''
        SELECT customer_number FROM payments
        WHERE customer_number < 200
        LIMIT 10;
    '''
    return sql

def get_exercise_26():
    sql = \
    '''
        SELECT customer_number FROM payments
        WHERE customer_number BETWEEN 200 AND 400
        LIMIT 10;
    '''
    return sql

def get_exercise_27():
    sql = \
    '''
        SELECT customer_number FROM payments
        WHERE customer_number > 400
        LIMIT 10;
    '''
    return sql

def get_exercise_28():
    sql = \
    '''
        SELECT payment_date FROM payments
        WHERE payment_date < '2003-12-31'
        LIMIT 10;
    '''
    return sql

def get_exercise_29():
    sql = \
    '''
        SELECT payment_date FROM payments
        WHERE payment_date BETWEEN '2003-12-31' AND '2004-12-31'
        LIMIT 10;
    '''
    return sql

def get_exercise_30():
    sql = \
    '''
        SELECT payment_date FROM payments
        WHERE payment_date = '2005-02-02';
    '''
    return sql

def get_exercise_31():
    sql = \
    '''
        SELECT amount FROM payments
        WHERE amount < (SELECT AVG(amount) FROM payments)
        ORDER BY amount DESC
        LIMIT 10;
    '''
    return sql

def get_exercise_32():
    sql = \
    '''
        SELECT amount FROM payments
        WHERE amount > (SELECT AVG(amount) FROM payments)
        LIMIT 10;
    '''
    return sql

def get_exercise_33():
    sql = \
    '''
        SELECT c.customer_name, p.payment_date, p.amount
        FROM customers c
        JOIN payments p ON p.customer_number = c.customer_number
        ORDER BY c.customer_name
        LIMIT 10;
    '''
    return sql

def get_exercise_34():
    sql = \
    '''
        SELECT c.customer_name, MAX(c.phone), MAX(p.payment_date)
        AS "last payment date"FROM customers c
        JOIN payments p ON p.customer_number = c.customer_number
        GROUP BY c.customer_name
        ORDER BY c.customer_name
        LIMIT 10;
    '''
    return sql

def get_exercise_35():
    sql = \
    '''
        SELECT country, COUNT(*) FROM customers
        GROUP BY country
        ORDER BY country
        LIMIT 10;
    '''
    return sql

def get_exercise_36():
    sql = \
    '''
        SELECT c.country, COUNT(p.check_number) AS "payments"
        FROM customers c
        JOIN payments p ON p.customer_number = c.customer_number
        GROUP BY c.country
        ORDER BY c.country
        LIMIT 10;
    '''
    return sql

def get_exercise_37():
    sql = \
    '''
        SELECT order_number, order_date FROM orders
        LIMIT 10;
    '''
    return sql

def get_exercise_38():
    sql = \
    '''
        SELECT c.customer_name, o.order_number, o.order_date
        FROM customers c
        JOIN orders o ON o.customer_number = c.customer_number
        LIMIT 10;
    '''
    return sql

def get_exercise_39():
    sql = \
    '''
        SELECT o.order_number, o.order_date,
        TO_CHAR(SUM(od.quantity_ordered*od.price_each),'999,999,999.00')
        AS "order value"
        FROM orders o
        JOIN order_details od ON od.order_number = o.order_number
        GROUP BY o.order_number
        LIMIT 10;
    '''
    return sql

def get_exercise_40():
    sql = \
    '''
        SELECT MAX(c.customer_name), o.order_number,
        TO_CHAR(SUM(od.quantity_ordered*od.price_each),'999,999,999.00')
        AS "order value" FROM customers c
        JOIN orders o ON o.customer_number = c.customer_number
        JOIN order_details od ON od.order_number = o.order_number
        GROUP BY o.order_number
        LIMIT 10;
    '''
    return sql

def get_exercise_41():
    sql = \
    '''
        SELECT c.customer_name,
        TO_CHAR(SUM(od.quantity_ordered*od.price_each),'999,999,999,00')
        AS "value of all orders"
        FROM customers c
        JOIN orders o ON o.customer_number = c.customer_number
        JOIN order_details od ON od.order_number = o.order_number
        GROUP BY c.customer_number
        LIMIT 10;
    '''
    return sql

def get_exercise_42():
    sql = \
    '''
        SELECT o.customer_number, od.order_number, pr.product_name
        FROM order_details od
        JOIN products pr ON pr.product_code = od.product_code
        JOIN orders o ON o.order_number = od.order_number
        LIMIT 10;
    '''
    return sql

def get_exercise_43():
    sql = \
    '''
        SELECT e.last_name, b.last_name FROM employees e
        JOIN employees b ON e.reports_to = b.employee_number
        LIMIT 10;
    '''
    return sql

def get_exercise_44():
    sql = \
    '''
        SELECT b.first_name, b.last_name, e.first_name, e.last_name
        FROM employees e
        JOIN employees b ON e.reports_to = b.employee_number
        ORDER BY b.last_name
        LIMIT 10;
    '''
    return sql


if __name__ == '__main__':

    # for idx in range(1,45):
    for idx in [1]:
        sql = eval(f'get_exercise_{idx}')()
        output = execute_sql(sql=sql)
        print(output)

