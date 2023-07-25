import textwrap, json, re
# l_exercises = [{'answer_text': 'SELECT * FROM payments LIMIT 10;', 'question_text': 'List all the records in the Payments table. Display only the first 10 rows of results.', 'sample': 'https://o.quizlet.com/s6CRKkbrFMSNvYkUrbJm7w.png'}, {'answer_text': 'SELECT check_number FROM payments LIMIT 10;', 'question_text': 'Display all the values for checkNumber in the Payments table.', 'sample': 'https://o.quizlet.com/zRTojj3d1wCRR8ANC9TIiA.png'}, {'answer_text': 'SELECT payment_date FROM payments LIMIT 10;', 'question_text': 'Display all the values for paymentDate in the Payments', 'sample': 'https://o.quizlet.com/3caCJrvcshSo30jHm4beqA.png'}, {'answer_text': 'SELECT amount FROM payments LIMIT 10;', 'question_text': 'Display all the values for amount in the Payments table.', 'sample': None}, {'answer_text': 'SELECT customer_number FROM payments LIMIT 10;', 'question_text': 'Display all the values for customerNumber in the Payments table.', 'sample': None}, {'answer_text': 'SELECT check_number FROM payments\nORDER BY check_number LIMIT 10;', 'question_text': 'Display all the values for checkNumber in the Payments table. Sort the results by checkNumber.', 'sample': None}, {'answer_text': 'SELECT check_number FROM payments\nORDER BY check_number DESC LIMIT 10;', 'question_text': 'Display all the values for checkNumber in the Payments table. Sort the results by checkNumber in descending order.', 'sample': None}, {'answer_text': 'SELECT payment_date FROM payments\nORDER BY payment_date LIMIT 10;', 'question_text': 'Display all the values for paymentDate in the Payments table. Sort the results by paymentDate.', 'sample': None}, {'answer_text': 'SELECT payment_date FROM payments\nORDER BY payment_date DESC LIMIT 10;', 'question_text': 'Display all the values for paymentDate in the Payments table. Sort the results by paymentDate in descending order.', 'sample': None}, {'answer_text': 'SELECT customer_number FROM payments\nORDER BY customer_number LIMIT 10;', 'question_text': 'Display all the values for customerNumber in the Payments table. Sort the results by customerNumber.', 'sample': None}, {'answer_text': 'SELECT customer_number FROM payments\nORDER BY customer_number DESC LIMIT 10;', 'question_text': 'Display all the values for customerNumber in the Payments table. Sort the results by customerNumber in descending order.', 'sample': None}, {'answer_text': 'SELECT check_number, payment_date FROM payments LIMIT 10;', 'question_text': 'Display the values for checkNumber and paymentDate in the Payments table.', 'sample': None}, {'answer_text': 'SELECT check_number, amount FROM payments LIMIT 10;', 'question_text': 'Display the values for checkNumber and amount in the Payments table. Display only hte first', 'sample': None}, {'answer_text': 'SELECT check_number, customer_number FROM payments LIMIT 10;', 'question_text': 'Display the values for checkNumber and customerNumber in the Payments table.', 'sample': None}, {'answer_text': 'SELECT DISTINCT(customer_number) FROM payments LIMIT 10;', 'question_text': 'Display a list of unique customerNumber values in the Payments table.', 'sample': None}, {'answer_text': 'SELECT MIN(amount) AS "smallest payment" FROM payments;', 'question_text': "Display the smallest amount value in the Payments table. Label the result 'Smallest Payment'.", 'sample': 'https://o.quizlet.com/gbzIpu70s4EGxP1W9en9gw.png'}, {'answer_text': 'SELECT MAX(amount) AS "largest payment" FROM payments;', 'question_text': 'Display the largest amount value in the Payments table. Label the result "Largest Payment"', 'sample': None}, {'answer_text': 'SELECT AVG(amount) FROM payments LIMIT 10;', 'question_text': 'Display the average amount value in the Payments table.', 'sample': None}, {'answer_text': 'SELECT MIN(payment_date) FROM payments LIMIT 10;', 'question_text': 'Display the earliest paymentDate value in the Payments table.', 'sample': None}, {'answer_text': 'SELECT MAX(payment_date) FROM payments LIMIT 10;', 'question_text': 'Display the latest paymentDate value in the Payments table.', 'sample': None}, {'answer_text': 'SELECT customer_number, SUM(amount) FROM payments\nGROUP BY customer_number LIMIT 10;', 'question_text': 'Display the customerNumber and the total payment amount assigned to that customerNumber in the Payments table. Display only the first 10 rows of results.', 'sample': None}, {'answer_text': 'SELECT customer_number, AVG(amount) FROM payments\nGROUP BY customer_number LIMIT 10;', 'question_text': 'Display the customerNumber and the average payment amount assigned to that customerNumber in the Payments table.', 'sample': None}, {'answer_text': 'SELECT COUNT(*) FROM payments LIMIT 10;', 'question_text': 'Calculate the number of rows in the Payments table.', 'sample': None}, {'answer_text': 'SELECT COUNT(DISTINCT(customer_number)) FROM payments\nLIMIT 10;', 'question_text': 'Count the number of unique customerNumber values in the Payments table.', 'sample': None}, {'answer_text': 'SELECT customer_number FROM payments\nWHERE customer_number < 200 LIMIT 10;', 'question_text': 'Display the customerNumber values for those customerNumbers in the Payments table that have values less than 200.', 'sample': None}, {'answer_text': 'SELECT customer_number FROM payments\nWHERE customer_number BETWEEN 200 AND 400 LIMIT 10;', 'question_text': 'Display the customerNumber values for those customerNumbers in the Payments table that have values between 200 and 400.', 'sample': None}, {'answer_text': 'SELECT customer_number FROM payments\nWHERE customer_number > 400 LIMIT 10;', 'question_text': 'Display the customerNumber values for those customerNumbers in the Payments table that have values greater than 400.', 'sample': None}, {'answer_text': "SELECT payment_date FROM payments\nWHERE payment_date < '2003-12-31' LIMIT 10;", 'question_text': 'Display the paymentDate values for those records in the Payments table in which the payment date is earlier than 12/31/2003.', 'sample': None}, {'answer_text': "SELECT payment_date FROM payments\nWHERE payment_date BETWEEN '2003-12-31' AND '2004-12-31' LIMIT 10;", 'question_text': 'Display the paymentDate values for those records in the Payments table in which the payment date is between 12/31/2003 and 12/31/2004.', 'sample': None}, {'answer_text': "SELECT payment_date FROM payments\nWHERE payment_date = '2005-02-02' LIMIT 10;", 'question_text': 'Display the paymentDate values for those records in the Payments table in which the payment date is 02/02/2005.', 'sample': None}, {'answer_text': 'SELECT amount FROM payments\nWHERE amount < (SELECT AVG(amount) FROM payments)\nORDER BY amount DESC LIMIT 10;', 'question_text': 'Display the amount values for those records in the Payments table in which the amount values is less than the average amount value in the Payments table. Sort the results by payment amount from highest to lowest amount. Display only the first 10 rows of results.', 'sample': 'https://o.quizlet.com/5DWkLtdOZs8YyW2tsxwIFg.png'}, {'answer_text': 'SELECT amount FROM payments\nWHERE amount > (SELECT AVG(amount) FROM payments) LIMIT 10;', 'question_text': 'Display the amount values for those records in the Payments table in which the amount values is less than the average amount value in the Payments table.', 'sample': 'https://o.quizlet.com/Ck4NbukWGQr7jYtxNIh8Tw.png'}, {'answer_text': 'SELECT c.customer_name, p.payment_date, p.amount FROM customers c\nJOIN payments p ON p.customer_number = c.customer_number ORDER BY c.customer_name LIMIT 10;', 'question_text': 'Display the customerName, paymentDate, and amount from the Payments and Customers tables. Display only the first 10 rows of results.', 'sample': 'https://o.quizlet.com/HnwSdDqQSM0Y8KEjWMkCBg.png'}, {'answer_text': 'SELECT c.customer_name, c.phone, MAX(p.payment_date) AS "last payment date"\nFROM customers c\nJOIN payments p ON p.customer_number = c.customer_number\nGROUP BY c.customer_name LIMIT 10;', 'question_text': 'Display the customerName, phone and latest paymentDate for each customer in the Payments and Customers tables. Label the latest paymentDate column as Last Payment Date. Display only the first 10 rows of results.', 'sample': 'https://o.quizlet.com/W4vipBaaF6RFUzbCINASsA.png'}, {'answer_text': 'SELECT country, COUNT(*) FROM customers\nGROUP BY country\nORDER BY country LIMIT 10;', 'question_text': 'Display a list of country values in the Customers table along with the number of customers in each country. The list should be in alphabetical order. Display only the first 10 rows of results.', 'sample': 'https://o.quizlet.com/B10JG13zKEFBysOzNao7bw.png'}, {'answer_text': 'SELECT c.country, COUNT(p.check_number) AS "payments"\nFROM customers c\nJOIN payments p ON p.customer_number = c.customer_number\nGROUP BY c.country\nORDER BY c.country LIMIT 10;', 'question_text': "Display a list of country values in the Customers table along with the number of payments for each country. Label the number of payments column 'Payments'. The list should be in alphabetical order. Display only the first 10 rows of results.", 'sample': 'https://o.quizlet.com/GgX38NsY35FfIktEvy-P9w.png'}, {'answer_text': 'SELECT order_number, order_date FROM orders LIMIT 10;', 'question_text': 'Display a list of orderNumber and orderDate values from the Orders table. Display only the first 10 rows of results.', 'sample': 'https://o.quizlet.com/7L6-kqw3IxcfxfHwP.yQXg.png'}, {'answer_text': 'SELECT c.customer_name, o.order_number, o.order_date FROM customers c\nJOIN orders o ON o.customer_number = c.customer_number LIMIT 10;', 'question_text': 'Display the customerName, orderNumber, and orderDate values from the Customers and Orders tables. Display only the first 10 rows of results.', 'sample': 'https://o.quizlet.com/Yupt4zHi2qDcscAwZHwPNQ.png'}, {'answer_text': 'SELECT o.order_number, o.order_date, FORMAT(SUM(od.quantity_ordered*od.price_each),2) AS "order value" FROM orders o\nJOIN order_details od ON od.order_number = o.order_number\nGROUP BY o.order_number LIMIT 10;', 'question_text': 'Display the orderNumber, orderDate, and value of each order from the Orders and order_details tables. The value of each order is calculated by multiplying quantityOrdered by priceEach. Label the calculated column "Order Value". Format the order value column so that only two digits are displayed after the decimal point. Display only the first ten results.', 'sample': 'https://o.quizlet.com/dMujZr6rV6PsGluxPZgsTw.png'}, {'answer_text': 'SELECT c.customer_name, o.order_number, FORMAT(SUM(od.quantity_ordered*od.price_each),2) AS "order value" FROM customers c\nJOIN orders o ON o.customer_number = c.customer_number JOIN order_details od ON od.order_number = o.order_number\nGROUP BY o.order_number LIMIT 10;', 'question_text': 'Display the customerName, orderNumber, and value of each order from the Orders and order_details tables. The value of each order is calculated by multiplying quantityOrdered by priceEach. Label the calculated column "Order Value". Format the order value column so that only two digits are displayed after the decimal point. Display only the first ten results.', 'sample': 'https://o.quizlet.com/m5sTr4KmhbbbsnE57h0tww.png'}, {'answer_text': 'SELECT c.customer_name, FORMAT(SUM(od.quantity_ordered*od.price_each),2) AS "value of all orders"\nFROM customers c\nJOIN orders o ON o.customer_number = c.customer_number\nJOIN order_details od ON od.order_number = o.order_number\nGROUP BY c.customer_number LIMIT 10;', 'question_text': 'Display the customerName, and value of all orders made by that customer. The value of each order is calculated by multiplying quantityOrdered by priceEach. Label the calculated column "Value of All Orders". Format the order value column so that only two digits are displayed after the decimal point. Display only the first ten results.', 'sample': 'https://o.quizlet.com/Uzj3WcJaFY-GsFt7m3PT8A.png'}, {'answer_text': 'SELECT o.customer_number, od.order_number, pr.product_name\nFROM order_details od\nJOIN products pr ON pr.product_code = od.product_code\nJOIN orders o ON o.order_number = od.order_number LIMIT 10;', 'question_text': 'Display the customerNumber, orderNumber, and productName values for each order using the Orders, order_details, and Products tables. Display only the first ten results.', 'sample': 'https://o.quizlet.com/b.oHVecKN8tuPLmoGzuxzA.png'}, {'answer_text': 'SELECT e.last_name, b.last_name FROM employees e\nJOIN employees b ON e.reports_to = b.employee_number;', 'question_text': 'Display the lastName of each Employee followed by the lastName of the Employee they report to. Display only the first ten results.', 'sample': 'https://o.quizlet.com/WPhr2nvxHjwWkMkeNLekxg.png'}, {'answer_text': 'SELECT b.first_name, b.last_name, e.first_name, e.last_name\nFROM employees e\nJOIN employees b ON e.reports_to = b.employee_number\nORDER BY b.last_name LIMIT 10;', 'question_text': 'Display the firstName and lastName of each manager followed by the firstName and lastName of each employee they supervise. Sort the results by the lastName of each manager. Display only the first ten results.', 'sample': 'https://o.quizlet.com/dgEr6APvgECz8u6xWIPvbg.png'}]

file = open('data.json','r', encoding='utf-8')
d_data = json.load(file)
file.close()

l_tables =d_data['tables']
l_fields =d_data['fields']
l_exercises =d_data['exercises']

pattern_keywords = '|'.join([f'({x})' for x in l_tables+l_fields])

markdown = ''

for idx, d_exercise in enumerate(l_exercises,1): 
    question_text = d_exercise['question_text']
    question_text = re.sub(pattern=f'{pattern_keywords}', repl= lambda x : f'<strong>{x.group(0)}</strong>', string=question_text)

    answer_text = d_exercise['answer_text']
    sample = d_exercise['sample']

    ans_template = f'''
<details>
<summary>Click here to see the answer</summary>

```sql
{answer_text}
```
</details>
    '''

    if sample:
        if 'https' in sample:
            sample_content = f"<img src='{sample}' alt='Image' style='flex: 1; max-width: 300px; min-height:100px; max-height: 200px;'>"
        else:
            sample_content = sample

        table_md = f'''
<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE {idx}</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>{question_text}</td>
    <td>{sample_content}</td>
</tr>
<tr>
<td colspan=2>
{ans_template}
</td>
</tr>
</table>
'''
    else:
        table_md = f'''
<table border=1 width=100%>
<tr><th align="left">EXERCISE {idx}</th></tr>
<tr>
    <td>{question_text}</td>
</tr>
</tr>
<tr>
<td>
{ans_template}
</td>
</tr>
</table>
'''

    markdown += textwrap.dedent(table_md)
    # markdown += ans_template

markdown = textwrap.dedent(markdown)

file = open('README.md', 'w', encoding='utf-8')
file.write(markdown)
file.close()