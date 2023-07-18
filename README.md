

| EXERCISE 1 | SAMPLE |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>List all the records in the Payments table. Display only the first 10 rows of results.</p> | <img src='https://o.quizlet.com/s6CRKkbrFMSNvYkUrbJm7w.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |


<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT * FROM payments LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 2 | SAMPLE |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display all the values for checkNumber in the Payments table.</p> | <img src='https://o.quizlet.com/zRTojj3d1wCRR8ANC9TIiA.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |


<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT check_number FROM payments LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 3 | SAMPLE |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display all the values for paymentDate in the Payments</p> | <img src='https://o.quizlet.com/3caCJrvcshSo30jHm4beqA.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |


<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT payment_date FROM payments LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 4 |
| :--- |
| <p style='font-size:16px;font-weight:bold;'>Display all the values for amount in the Payments table.</p> |
    

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT amount FROM payments LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 5 |
| :--- |
| <p style='font-size:16px;font-weight:bold;'>Display all the values for customerNumber in the Payments table.</p> |
    

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT customer_number FROM payments LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 6 |
| :--- |
| <p style='font-size:16px;font-weight:bold;'>Display all the values for checkNumber in the Payments table. Sort the results by checkNumber.</p> |
    

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT check_number FROM payments
ORDER BY check_number LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 7 |
| :--- |
| <p style='font-size:16px;font-weight:bold;'>Display all the values for checkNumber in the Payments table. Sort the results by checkNumber in descending order.</p> |
    

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT check_number FROM payments
ORDER BY check_number DESC LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 8 |
| :--- |
| <p style='font-size:16px;font-weight:bold;'>Display all the values for paymentDate in the Payments table. Sort the results by paymentDate.</p> |
    

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT payment_date FROM payments
ORDER BY payment_date LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 9 |
| :--- |
| <p style='font-size:16px;font-weight:bold;'>Display all the values for paymentDate in the Payments table. Sort the results by paymentDate in descending order.</p> |
    

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT payment_date FROM payments
ORDER BY payment_date DESC LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 10 |
| :--- |
| <p style='font-size:16px;font-weight:bold;'>Display all the values for customerNumber in the Payments table. Sort the results by customerNumber.</p> |
    

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT customer_number FROM payments
ORDER BY customer_number LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 11 |
| :--- |
| <p style='font-size:16px;font-weight:bold;'>Display all the values for customerNumber in the Payments table. Sort the results by customerNumber in descending order.</p> |
    

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT customer_number FROM payments
ORDER BY customer_number DESC LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 12 |
| :--- |
| <p style='font-size:16px;font-weight:bold;'>Display the values for checkNumber and paymentDate in the Payments table.</p> |
    

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT check_number, payment_date FROM payments LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 13 |
| :--- |
| <p style='font-size:16px;font-weight:bold;'>Display the values for checkNumber and amount in the Payments table. Display only hte first</p> |
    

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT check_number, amount FROM payments LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 14 |
| :--- |
| <p style='font-size:16px;font-weight:bold;'>Display the values for checkNumber and customerNumber in the Payments table.</p> |
    

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT check_number, customer_number FROM payments LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 15 |
| :--- |
| <p style='font-size:16px;font-weight:bold;'>Display a list of unique customerNumber values in the Payments table.</p> |
    

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT DISTINCT(customer_number) FROM payments LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 16 | SAMPLE |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the smallest amount value in the Payments table. Label the result 'Smallest Payment'.</p> | <img src='https://o.quizlet.com/gbzIpu70s4EGxP1W9en9gw.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |


<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT MIN(amount) AS 'smallest payment' FROM payments;
  ```
</details>

<br>
  

| EXERCISE 17 |
| :--- |
| <p style='font-size:16px;font-weight:bold;'>Display the largest amount value in the Payments table. Label the result "Largest Payment"</p> |
    

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT MAX(amount) AS "largest payment" FROM payments;
  ```
</details>

<br>
  

| EXERCISE 18 |
| :--- |
| <p style='font-size:16px;font-weight:bold;'>Display the average amount value in the Payments table.</p> |
    

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT AVG(amount) FROM payments LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 19 |
| :--- |
| <p style='font-size:16px;font-weight:bold;'>Display the earliest paymentDate value in the Payments table.</p> |
    

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT MIN(payment_date) FROM payments LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 20 |
| :--- |
| <p style='font-size:16px;font-weight:bold;'>Display the latest paymentDate value in the Payments table.</p> |
    

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT MAX(payment_date) FROM payments LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 21 |
| :--- |
| <p style='font-size:16px;font-weight:bold;'>Display the customerNumber and the total payment amount assigned to that customerNumber in the Payments table. Display only the first 10 rows of results.</p> |
    

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT customer_number, SUM(amount) FROM payments
GROUP BY customer_number LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 22 |
| :--- |
| <p style='font-size:16px;font-weight:bold;'>Display the customerNumber and the average payment amount assigned to that customerNumber in the Payments table.</p> |
    

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT customer_number, AVG(amount) FROM payments
GROUP BY customer_number LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 23 |
| :--- |
| <p style='font-size:16px;font-weight:bold;'>Calculate the number of rows in the Payments table.</p> |
    

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT COUNT(*) FROM payments LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 24 |
| :--- |
| <p style='font-size:16px;font-weight:bold;'>Count the number of unique customerNumber values in the Payments table.</p> |
    

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT COUNT(DISTINCT(customer_number)) LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 25 |
| :--- |
| <p style='font-size:16px;font-weight:bold;'>Display the customerNumber values for those customerNumbers in the Payments table that have values less than 200.</p> |
    

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT customer_number FROM payments
WHERE customer_number < 200 LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 26 |
| :--- |
| <p style='font-size:16px;font-weight:bold;'>Display the customerNumber values for those customerNumbers in the Payments table that have values between 200 and 400.</p> |
    

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT customer_number FROM payments
WHERE customer_number BETWEEN 200 AND 400 LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 27 |
| :--- |
| <p style='font-size:16px;font-weight:bold;'>Display the customerNumber values for those customerNumbers in the Payments table that have values greater than 400.</p> |
    

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT customer_number FROM payments
WHERE customer_number > 400 LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 28 |
| :--- |
| <p style='font-size:16px;font-weight:bold;'>Display the paymentDate values for those records in the Payments table in which the payment date is earlier than 12/31/2003.</p> |
    

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT payment_date FROM payments
WHERE payment_date < '2003-12-31' LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 29 |
| :--- |
| <p style='font-size:16px;font-weight:bold;'>Display the paymentDate values for those records in the Payments table in which the payment date is between 12/31/2003 and 12/31/2004.</p> |
    

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT payment_date FROM payments
WHERE payment_date BETWEEN '2003-12-31' AND '2004-12-31' LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 30 |
| :--- |
| <p style='font-size:16px;font-weight:bold;'>Display the paymentDate values for those records in the Payments table in which the payment date is 02/02/2005.</p> |
    

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT payment_date FROM payments
WHERE payment_date = '2005-02-02' LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 31 | SAMPLE |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the amount values for those records in the Payments table in which the amount values is less than the average amount value in the Payments table. Sort the results by payment amount from highest to lowest amount. Display only the first 10 rows of results.</p> | <img src='https://o.quizlet.com/5DWkLtdOZs8YyW2tsxwIFg.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |


<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT amount FROM payments
WHERE amount < (SELECT AVG(amount) FROM payments)
ORDER BY amount DESC LIMIT 10 LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 32 | SAMPLE |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the amount values for those records in the Payments table in which the amount values is less than the average amount value in the Payments table.</p> | <img src='https://o.quizlet.com/Ck4NbukWGQr7jYtxNIh8Tw.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |


<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT amount FROM payments
WHERE amount > (SELECT AVG(amount) FROM payments) LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 33 | SAMPLE |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the customerName, paymentDate, and amount from the Payments and Customers tables. Display only the first 10 rows of results.</p> | <img src='https://o.quizlet.com/HnwSdDqQSM0Y8KEjWMkCBg.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |


<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT c.customer_name, p.payment_date, p.amount FROM customers c
JOIN payments p ON p.customer_number = c.customer_number ORDER BY c.customer_name LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 34 | SAMPLE |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the customerName, phone and latest paymentDate for each customer in the Payments and Customers tables. Label the latest paymentDate column as Last Payment Date. Display only the first 10 rows of results.</p> | <img src='https://o.quizlet.com/W4vipBaaF6RFUzbCINASsA.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |


<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT c.customer_name, c.phone, MAX(p.payment_date) AS 'last payment date'
FROM customers c
JOIN payments p ON p.customer_number = c.customer_number
GROUP BY c.customer_name LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 35 | SAMPLE |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display a list of country values in the Customers table along with the number of customers in each country. The list should be in alphabetical order. Display only the first 10 rows of results.</p> | <img src='https://o.quizlet.com/B10JG13zKEFBysOzNao7bw.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |


<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT country, COUNT(*) FROM customers
GROUP BY country
ORDER BY country LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 36 | SAMPLE |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display a list of country values in the Customers table along with the number of payments for each country. Label the number of payments column 'Payments'. The list should be in alphabetical order. Display only the first 10 rows of results.</p> | <img src='https://o.quizlet.com/GgX38NsY35FfIktEvy-P9w.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |


<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT c.country, COUNT(p.check_number) AS 'payments'
FROM customers c
JOIN payments p ON p.customer_number = c.customer_number
GROUP BY c.country
ORDER BY c.country LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 37 | SAMPLE |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display a list of orderNumber and orderDate values from the Orders table. Display only the first 10 rows of results.</p> | <img src='https://o.quizlet.com/7L6-kqw3IxcfxfHwP.yQXg.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |


<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT order_number, order_date FROM orders LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 38 | SAMPLE |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the customerName, orderNumber, and orderDate values from the Customers and Orders tables. Display only the first 10 rows of results.</p> | <img src='https://o.quizlet.com/Yupt4zHi2qDcscAwZHwPNQ.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |


<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT c.customer_name, o.order_number, o.order_date FROM customers c
JOIN orders o ON o.customer_number = c.customer_number LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 39 | SAMPLE |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the orderNumber, orderDate, and value of each order from the Orders and order_details tables. The value of each order is calculated by multiplying quantityOrdered by priceEach. Label the calculated column "Order Value". Format the order value column so that only two digits are displayed after the decimal point. Display only the first ten results.</p> | <img src='https://o.quizlet.com/dMujZr6rV6PsGluxPZgsTw.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |


<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT o.order_number, o.order_date, FORMAT(SUM(od.quantity_ordered*od.price_each),2) AS 'order value' FROM orders o
JOIN order_details od ON od.order_number = o.order_number
GROUP BY o.order_number LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 40 | SAMPLE |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the customerName, orderNumber, and value of each order from the Orders and order_details tables. The value of each order is calculated by multiplying quantityOrdered by priceEach. Label the calculated column "Order Value". Format the order value column so that only two digits are displayed after the decimal point. Display only the first ten results.</p> | <img src='https://o.quizlet.com/m5sTr4KmhbbbsnE57h0tww.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |


<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT c.customer_name, o.order_number, FORMAT(SUM(od.quantity_ordered*od.price_each),2) AS 'order value' FROM customers c
JOIN orders o ON o.customer_number = c.customer_number JOIN order_details od ON od.order_number = o.order_number
GROUP BY o.order_number LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 41 | SAMPLE |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the customerName, and value of all orders made by that customer. The value of each order is calculated by multiplying quantityOrdered by priceEach. Label the calculated column "Value of All Orders". Format the order value column so that only two digits are displayed after the decimal point. Display only the first ten results.</p> | <img src='https://o.quizlet.com/Uzj3WcJaFY-GsFt7m3PT8A.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |


<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT c.customer_name, FORMAT(SUM(od.quantity_ordered*od.price_each),2) AS 'value of all orders'
FROM customers c
JOIN orders o ON o.customer_number = c.customer_number
JOIN order_details od ON od.order_number = o.order_number
GROUP BY c.customer_number LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 42 | SAMPLE |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the customerNumber, orderNumber, and productName values for each order using the Orders, order_details, and Products tables. Display only the first ten results.</p> | <img src='https://o.quizlet.com/b.oHVecKN8tuPLmoGzuxzA.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |


<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT o.customer_number, od.order_number, pr.product_name
FROM order_details od
JOIN products pr ON pr.product_code = od.product_code
JOIN orders o ON o.order_number = od.order_number LIMIT 10;
  ```
</details>

<br>
  

| EXERCISE 43 | SAMPLE |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the lastName of each Employee followed by the lastName of the Employee they report to. Display only the first ten results.</p> | <img src='https://o.quizlet.com/WPhr2nvxHjwWkMkeNLekxg.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |


<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT e.last_name, b.last_name FROM employees e
JOIN employees b ON e.reports_to = b.employee_number;
  ```
</details>

<br>
  

| EXERCISE 44 | SAMPLE |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the firstName and lastName of each manager followed by the firstName and lastName of each employee they supervise. Sort the results by the lastName of each manager. Display only the first ten results.</p> | <img src='https://o.quizlet.com/dgEr6APvgECz8u6xWIPvbg.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |


<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
SELECT b.first_name, b.last_name, e.first_name, e.last_name
FROM employees e
JOIN employees b ON e.reports_to = b.employee_number
ORDER BY b.last_name LIMIT 10;
  ```
</details>

<br>
  