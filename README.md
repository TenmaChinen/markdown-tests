
| EXERCISE 1 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>List all the records in the Payments table. Display only the first 10 rows of results.</p> | <img src='https://o.quizlet.com/s6CRKkbrFMSNvYkUrbJm7w.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT * FROM Payments LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 2 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display all the values for checkNumber in the Payments table.</p> | <img src='https://o.quizlet.com/zRTojj3d1wCRR8ANC9TIiA.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT checkNumber FROM Payments LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 3 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display all the values for paymentDate in the Payments</p> | <img src='https://o.quizlet.com/3caCJrvcshSo30jHm4beqA.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT paymentDate FROM Payments LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 4 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display all the values for amount in the Payments table.</p> |  |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT amount FROM Payments LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 5 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display all the values for customerNumber in the Payments table.</p> |  |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT customerNumber FROM Payments LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 6 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display all the values for checkNumber in the Payments table. Sort the results by checkNumber.</p> |  |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT checkNumber FROM Payments
ORDER BY checkNumber LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 7 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display all the values for checkNumber in the Payments table. Sort the results by checkNumber in descending order.</p> |  |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT checkNumber FROM Payments
ORDER BY checkNumber DESC LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 8 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display all the values for paymentDate in the Payments table. Sort the results by paymentDate.</p> |  |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT paymentDate FROM Payments
ORDER BY paymentDate LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 9 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display all the values for paymentDate in the Payments table. Sort the results by paymentDate in descending order.</p> |  |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT paymentDate FROM Payments
ORDER BY paymentDate DESC LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 10 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display all the values for customerNumber in the Payments table. Sort the results by customerNumber.</p> |  |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT customerNumber FROM Payments
ORDER BY customerNumber LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 11 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display all the values for customerNumber in the Payments table. Sort the results by customerNumber in descending order.</p> |  |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT customerNumber FROM Payments
ORDER BY customerNumber DESC LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 12 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the values for checkNumber and paymentDate in the Payments table.</p> |  |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT checkNumber, paymentDate FROM Payments LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 13 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the values for checkNumber and amount in the Payments table. Display only hte first</p> |  |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT checkNumber, amount FROM Payments LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 14 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the values for checkNumber and customerNumber in the Payments table.</p> |  |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT checkNumber, customerNumber FROM Payments LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 15 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display a list of unique customerNumber values in the Payments table.</p> |  |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT DISTINCT(customerNumber) FROM Payments LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 16 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the smallest amount value in the Payments table. Label the result 'Smallest Payment'.</p> | <img src='https://o.quizlet.com/gbzIpu70s4EGxP1W9en9gw.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT MIN(amount) AS 'Smallest Payment' FROM Payments;
  ```
</details>

<br>
  
| EXERCISE 17 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the largest amount value in the Payments table. Label the result "Largest Payment"</p> |  |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT MAX(amount) AS "Largest Payment" FROM Payments;
  ```
</details>

<br>
  
| EXERCISE 18 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the average amount value in the Payments table.</p> |  |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT AVG(amount) FROM Payments LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 19 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the earliest paymentDate value in the Payments table.</p> |  |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT MIN(paymentDate) FROM Payments LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 20 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the latest paymentDate value in the Payments table.</p> |  |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT MAX(paymentDate) FROM Payments LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 21 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the customerNumber and the total payment amount assigned to that customerNumber in the Payments table. Display only the first 10 rows of results.</p> |  |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT customerNumber, SUM(amount) FROM Payments
GROUP BY customerNumber LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 22 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the customerNumber and the average payment amount assigned to that customerNumber in the Payments table.</p> |  |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT customerNumber, AVG(amount) FROM Payments
GROUP BY customerNumber LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 23 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Calculate the number of rows in the Payments table.</p> |  |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT COUNT(*) FROM Payments LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 24 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Count the number of unique customerNumber values in the Payments table.</p> |  |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT COUNT(DISTINCT(customerNumber)) LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 25 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the customerNumber values for those customerNumbers in the Payments table that have values less than 200.</p> |  |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT customerNumber FROM Payments
WHERE customerNumber < 200 LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 26 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the customerNumber values for those customerNumbers in the Payments table that have values between 200 and 400.</p> |  |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT customerNumber FROM Payments
WHERE customerNumber BETWEEN 200 AND 400 LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 27 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the customerNumber values for those customerNumbers in the Payments table that have values greater than 400.</p> |  |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT customerNumber FROM Payments
WHERE customerNumber > 400 LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 28 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the paymentDate values for those records in the Payments table in which the payment date is earlier than 12/31/2003.</p> |  |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT paymentDate FROM Payments
WHERE paymentDate < '2003-12-31' LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 29 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the paymentDate values for those records in the Payments table in which the payment date is between 12/31/2003 and 12/31/2004.</p> |  |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT paymentDate FROM Payments
WHERE paymentDate BETWEEN '2003-12-31' AND '2004-12-31' LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 30 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the paymentDate values for those records in the Payments table in which the payment date is 02/02/2005.</p> |  |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT paymentDate FROM Payments
WHERE paymentDate = '2005-02-02' LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 31 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the amount values for those records in the Payments table in which the amount values is less than the average amount value in the Payments table. Sort the results by payment amount from highest to lowest amount. Display only the first 10 rows of results.</p> | <img src='https://o.quizlet.com/5DWkLtdOZs8YyW2tsxwIFg.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT amount FROM Payments
WHERE amount < (SELECT AVG(amount) FROM Payments)
ORDER BY amount DESC LIMIT 10 LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 32 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the amount values for those records in the Payments table in which the amount values is less than the average amount value in the Payments table.</p> | <img src='https://o.quizlet.com/Ck4NbukWGQr7jYtxNIh8Tw.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT amount FROM Payments
WHERE amount > (SELECT AVG(amount) FROM Payments) LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 33 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the customerName, paymentDate, and amount from the Payments and Customers tables. Display only the first 10 rows of results.</p> | <img src='https://o.quizlet.com/HnwSdDqQSM0Y8KEjWMkCBg.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT c.customerName, p.paymentDate, p.amount FROM Customers c
JOIN Payments p ON p.customerNumber = c.customerNumber ORDER BY c.customerName LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 34 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the customerName, phone and latest paymentDate for each customer in the Payments and Customers tables. Label the latest paymentDate column as Last Payment Date. Display only the first 10 rows of results.</p> | <img src='https://o.quizlet.com/W4vipBaaF6RFUzbCINASsA.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT c.customerName, c.phone, MAX(p.paymentDate) AS 'Last Payment Date'
FROM Customers c
JOIN Payments p ON p.customerNumber = c.customerNumber
GROUP BY c.customerName LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 35 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display a list of country values in the Customers table along with the number of customers in each country. The list should be in alphabetical order. Display only the first 10 rows of results.</p> | <img src='https://o.quizlet.com/B10JG13zKEFBysOzNao7bw.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT country, COUNT(*) FROM Customers
GROUP BY country
ORDER BY country LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 36 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display a list of country values in the Customers table along with the number of payments for each country. Label the number of payments column 'Payments'. The list should be in alphabetical order. Display only the first 10 rows of results.</p> | <img src='https://o.quizlet.com/GgX38NsY35FfIktEvy-P9w.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT c.country, COUNT(p.checkNumber) AS 'Payments'
FROM Customers c
JOIN Payments p ON p.customerNumber = c.customerNumber
GROUP BY c.country
ORDER BY c.country LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 37 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display a list of orderNumber and orderDate values from the Orders table. Display only the first 10 rows of results.</p> | <img src='https://o.quizlet.com/7L6-kqw3IxcfxfHwP.yQXg.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT orderNumber, orderDate FROM Orders LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 38 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the customerName, orderNumber, and orderDate values from the Customers and Orders tables. Display only the first 10 rows of results.</p> | <img src='https://o.quizlet.com/Yupt4zHi2qDcscAwZHwPNQ.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT c.customerName, o.orderNumber, o.orderDate FROM Customers c
JOIN Orders o ON o.customerNumber = c.customerNumber LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 39 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the orderNumber, orderDate, and value of each order from the Orders and OrderDetails tables. The value of each order is calculated by multiplying quantityOrdered by priceEach. Label the calculated column "Order Value". Format the order value column so that only two digits are displayed after the decimal point. Display only the first ten results.</p> | <img src='https://o.quizlet.com/dMujZr6rV6PsGluxPZgsTw.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT o.orderNumber, o.orderDate, FORMAT(SUM(od.quantityOrdered*od.priceEach),2) AS 'Order Value' FROM Orders o
JOIN OrderDetails od ON od.orderNumber = o.orderNumber
GROUP BY o.orderNumber LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 40 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the customerName, orderNumber, and value of each order from the Orders and OrderDetails tables. The value of each order is calculated by multiplying quantityOrdered by priceEach. Label the calculated column "Order Value". Format the order value column so that only two digits are displayed after the decimal point. Display only the first ten results.</p> | <img src='https://o.quizlet.com/m5sTr4KmhbbbsnE57h0tww.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT c.customerName, o.orderNumber, FORMAT(SUM(od.quantityOrdered*od.priceEach),2) AS 'Order Value' FROM Customers c
JOIN Orders o ON o.customerNumber = c.customerNumber JOIN OrderDetails od ON od.orderNumber = o.orderNumber
GROUP BY o.orderNumber LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 41 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the customerName, and value of all orders made by that customer. The value of each order is calculated by multiplying quantityOrdered by priceEach. Label the calculated column "Value of All Orders". Format the order value column so that only two digits are displayed after the decimal point. Display only the first ten results.</p> | <img src='https://o.quizlet.com/Uzj3WcJaFY-GsFt7m3PT8A.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT c.customerName, FORMAT(SUM(od.quantityOrdered*od.priceEach),2) AS 'Value of All Orders'
FROM Customers c
JOIN Orders o ON o.customerNumber = c.customerNumber
JOIN OrderDetails od ON od.orderNumber = o.orderNumber
GROUP BY c.customerNumber LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 42 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the customerNumber, orderNumber, and productName values for each order using the Orders, OrderDetails, and Products tables. Display only the first ten results.</p> | <img src='https://o.quizlet.com/b.oHVecKN8tuPLmoGzuxzA.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT o.customerNumber, od.orderNumber, pr.productName
FROM OrderDetails od
JOIN Products pr ON pr.productCode = od.productCode
JOIN Orders o ON o.orderNumber = od.orderNumber LIMIT 10;
  ```
</details>

<br>
  
| EXERCISE 43 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the lastName of each Employee followed by the lastName of the Employee they report to. Display only the first ten results.</p> | <img src='https://o.quizlet.com/WPhr2nvxHjwWkMkeNLekxg.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT e.lastName, b.lastName FROM Employees e
JOIN Employees b ON e.reportsTo = b.employeeNumber;
  ```
</details>

<br>
  
| EXERCISE 44 |  |
| :--- | :---: |
| <p style='font-size:16px;font-weight:bold;'>Display the firstName and lastName of each manager followed by the firstName and lastName of each employee they supervise. Sort the results by the lastName of each manager. Display only the first ten results.</p> | <img src='https://o.quizlet.com/dgEr6APvgECz8u6xWIPvbg.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'> |

<details>
  <summary>Click here to see the answer</summary>
  
  ```sql
    SELECT b.firstName, b.lastName, e.firstName, e.lastName
FROM Employees e
JOIN Employees b ON e.reportsTo = b.employeeNumber
ORDER BY b.lastName LIMIT 10;
  ```
</details>

<br>
  