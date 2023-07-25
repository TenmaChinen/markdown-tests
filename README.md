
<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 1</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>List all the records in the <strong>payments</strong> table.<br><br>Display only the first 10 rows of results.</td>
    <td><img src='images/sample_01.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT * FROM payments
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 2</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display only the 10 first values for <strong>check_number</strong> in the <strong>payments</strong> table.</td>
    <td><img src='images/sample_02.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT check_number FROM payments
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 3</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display only the 10 first values for <strong>payment_date</strong> in the <strong>payments</strong></td>
    <td><img src='images/sample_03.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT payment_date FROM payments
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 4</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display only the 10 first values for <strong>amount</strong> in the <strong>payments</strong> table.</td>
    <td><img src='images/sample_04.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT amount FROM payments
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 5</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display only the 10 first values for <strong>customer_number</strong> in the <strong>payments</strong> table.</td>
    <td><img src='images/sample_05.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT customer_number FROM payments
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 6</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display only the 10 first values for <strong>check_number</strong> in the <strong>payments</strong> table.<br><br>Sort the results by <strong>check_number</strong>.</td>
    <td><img src='images/sample_06.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT check_number FROM payments
ORDER BY check_number
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 7</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display only the 10 first values for <strong>check_number</strong> in the <strong>payments</strong> table.<br><br>Sort the results by <strong>check_number</strong> in descending order.</td>
    <td><img src='images/sample_07.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT check_number FROM payments
ORDER BY check_number DESC
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 8</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display only the 10 first values for <strong>payment_date</strong> in the <strong>payments</strong> table.<br><br>Sort the results by <strong>payment_date</strong>.</td>
    <td><img src='images/sample_08.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT payment_date FROM payments
ORDER BY payment_date
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 9</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display only the 10 first values for <strong>payment_date</strong> in the <strong>payments</strong> table.<br><br>Sort the results by <strong>payment_date</strong> in descending order.</td>
    <td><img src='images/sample_09.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT payment_date FROM payments
ORDER BY payment_date DESC
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 10</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display only the 10 first values for <strong>customer_number</strong> in the <strong>payments</strong> table.<br><br>Sort the results by <strong>customer_number</strong>.</td>
    <td><img src='images/sample_10.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT customer_number FROM payments
ORDER BY customer_number
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 11</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display only the 10 first values for <strong>customer_number</strong> in the <strong>payments</strong> table.<br><br>Sort the results by <strong>customer_number</strong> in descending order.</td>
    <td><img src='images/sample_11.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT customer_number FROM payments
ORDER BY customer_number DESC
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 12</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display the values for <strong>check_number</strong> and <strong>payment_date</strong> in the <strong>payments</strong> table.</td>
    <td><img src='images/sample_12.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT check_number, payment_date FROM payments
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 13</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display the values for <strong>check_number</strong> and <strong>amount</strong> in the <strong>payments</strong> table.<br><br>Display only the first</td>
    <td><img src='images/sample_13.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT check_number, amount FROM payments
LIMIT 1;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 14</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display the values for <strong>check_number</strong> and <strong>customer_number</strong> in the <strong>payments</strong> table.</td>
    <td><img src='images/sample_14.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT check_number, customer_number FROM payments
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 15</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display a list of unique <strong>customer_number</strong> values in the <strong>payments</strong> table.</td>
    <td><img src='images/sample_15.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT DISTINCT(customer_number) FROM payments
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 16</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display the smallest <strong>amount</strong> value in the <strong>payments</strong> table.<br><br>Label the result 'Smallest Payment'.</td>
    <td><img src='images/sample_16.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT MIN(amount) AS "smallest payment" FROM payments;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 17</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display the largest <strong>amount</strong> value in the <strong>payments</strong> table.<br><br>Label the result "Largest Payment"</td>
    <td><img src='images/sample_17.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT MAX(amount) AS "largest payment" FROM payments;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 18</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display the average <strong>amount</strong> value in the <strong>payments</strong> table.</td>
    <td><img src='images/sample_18.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT AVG(amount) FROM payments;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 19</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display the earliest <strong>payment_date</strong> value in the <strong>payments</strong> table.</td>
    <td><img src='images/sample_19.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT MIN(payment_date) FROM payments;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 20</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display the latest <strong>payment_date</strong> value in the <strong>payments</strong> table.</td>
    <td><img src='images/sample_20.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT MAX(payment_date) FROM payments;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 21</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display the <strong>customer_number</strong> and the total payment <strong>amount</strong> assigned to that <strong>customer_number</strong> in the <strong>payments</strong> table.<br><br>Display only the first 10 rows of results.</td>
    <td><img src='images/sample_21.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT customer_number, SUM(amount) FROM payments
GROUP BY customer_number
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 22</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display the <strong>customer_number</strong> and the average payment <strong>amount</strong> assigned to that <strong>customer_number</strong> in the <strong>payments</strong> table.</td>
    <td><img src='images/sample_22.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT customer_number, AVG(amount) FROM payments
GROUP BY customer_number
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 23</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Calculate the number of rows in the <strong>payments</strong> table.</td>
    <td><img src='images/sample_23.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT COUNT(*) FROM payments
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 24</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Count the number of unique <strong>customer_number</strong> values in the <strong>payments</strong> table.</td>
    <td><img src='images/sample_24.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT COUNT(DISTINCT(customer_number)) FROM payments
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 25</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display the <strong>customer_number</strong> values for those <strong>customer_number</strong>s in the <strong>payments</strong> table that have values less than 200.</td>
    <td><img src='images/sample_25.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT customer_number FROM payments
WHERE customer_number < 200
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 26</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display the <strong>customer_number</strong> values for those <strong>customer_number</strong>s in the <strong>payments</strong> table that have values between 200 and 400.</td>
    <td><img src='images/sample_26.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT customer_number FROM payments
WHERE customer_number BETWEEN 200 AND 400
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 27</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display the <strong>customer_number</strong> values for those <strong>customer_number</strong>s in the <strong>payments</strong> table that have values greater than 400.</td>
    <td><img src='images/sample_27.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT customer_number FROM payments
WHERE customer_number > 400
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 28</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display the <strong>payment_date</strong> values for those records in the <strong>payments</strong> table in which the payment date is earlier than 12/31/2003.</td>
    <td><img src='images/sample_28.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT payment_date FROM payments
WHERE payment_date < '2003-12-31'
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 29</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display the <strong>payment_date</strong> values for those records in the <strong>payments</strong> table in which the payment date is between 12/31/2003 and 12/31/2004.</td>
    <td><img src='images/sample_29.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT payment_date FROM payments
WHERE payment_date BETWEEN '2003-12-31' AND '2004-12-31'
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 30</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display the <strong>payment_date</strong> values for those records in the <strong>payments</strong> table in which the payment date is 02/02/2005.</td>
    <td><img src='images/sample_30.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT payment_date FROM payments
WHERE payment_date = '2005-02-02';
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 31</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display the <strong>amount</strong> values for those records in the <strong>payments</strong> table in which the <strong>amount</strong> values is less than the average <strong>amount</strong> value in the <strong>payments</strong> table.<br><br>Sort the results by payment <strong>amount</strong> from highest to lowest <strong>amount</strong>.<br><br>Display only the first 10 rows of results.</td>
    <td><img src='images/sample_31.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT amount FROM payments
WHERE amount < (SELECT AVG(amount) FROM payments)
ORDER BY amount DESC
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 32</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display the <strong>amount</strong> values for those records in the <strong>payments</strong> table in which the <strong>amount</strong> values is less than the average <strong>amount</strong> value in the <strong>payments</strong> table.</td>
    <td><img src='images/sample_32.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT amount FROM payments
WHERE amount > (SELECT AVG(amount) FROM payments)
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 33</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display the <strong>customer_name</strong>, <strong>payment_date</strong>, and <strong>amount</strong> from the <strong>payments</strong> and <strong>customers</strong> tables.<br><br>Display only the first 10 rows of results.</td>
    <td><img src='images/sample_33.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT c.customer_name, p.payment_date, p.amount
FROM customers c
JOIN payments p ON p.customer_number = c.customer_number
ORDER BY c.customer_name
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 34</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display the <strong>customer_name</strong>, <strong>phone</strong> and latest <strong>payment_date</strong> for each customer in the <strong>payments</strong> and <strong>customers</strong> tables.<br><br>Label the latest <strong>payment_date</strong> column as Last Payment Date.<br><br>Display only the first 10 rows of results.</td>
    <td><img src='images/sample_34.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT c.customer_name, MAX(c.phone), MAX(p.payment_date)
AS "last payment date"FROM customers c
JOIN payments p ON p.customer_number = c.customer_number
GROUP BY c.customer_name
ORDER BY c.customer_name
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 35</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display a list of <strong>country</strong> values in the <strong>customers</strong> table along with the number of <strong>customers</strong> in each <strong>country</strong>.<br><br>The list should be in alphabetical order.<br><br>Display only the first 10 rows of results.</td>
    <td><img src='images/sample_35.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT country, COUNT(*) FROM customers
GROUP BY country
ORDER BY country
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 36</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display a list of <strong>country</strong> values in the <strong>customers</strong> table along with the number of <strong>payments</strong> for each <strong>country</strong>.<br><br>Label the number of <strong>payments</strong> column '<strong>payments</strong>'.<br><br>The list should be in alphabetical order.<br><br>Display only the first 10 rows of results.</td>
    <td><img src='images/sample_36.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT c.country, COUNT(p.check_number) AS "payments"
FROM customers c
JOIN payments p ON p.customer_number = c.customer_number
GROUP BY c.country
ORDER BY c.country
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 37</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display a list of <strong>order_number</strong> and <strong>order_date</strong> values from the <strong>orders</strong> table.<br><br>Display only the first 10 rows of results.</td>
    <td><img src='images/sample_37.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT order_number, order_date FROM orders
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 38</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display the <strong>customer_name</strong>, <strong>order_number</strong>, and <strong>order_date</strong> values from the <strong>customers</strong> and <strong>orders</strong> tables.<br><br>Display only the first 10 rows of results.</td>
    <td><img src='images/sample_38.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT c.customer_name, o.order_number, o.order_date
FROM customers c
JOIN orders o ON o.customer_number = c.customer_number
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 39</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display the <strong>order_number</strong>, <strong>order_date</strong>, and value of each order from the <strong>orders</strong> and <strong>order_details</strong> tables.<br><br>The value of each order is calculated by multiplying <strong>quantity_ordered</strong> by <strong>price_each</strong>.<br><br>Label the calculated column "Order Value". Format the order value column so that only two digits are displayed after the decimal point. Display only the first 10 results.</td>
    <td><img src='images/sample_39.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT o.order_number, o.order_date,
TO_CHAR(SUM(od.quantity_ordered*od.price_each),'999,999,999.00')
AS "order value"
FROM orders o
JOIN order_details od ON od.order_number = o.order_number
GROUP BY o.order_number
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 40</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display the <strong>customer_name</strong>, <strong>order_number</strong>, and value of each order from the <strong>orders</strong> and <strong>order_details</strong> tables.<br><br>The value of each order is calculated by multiplying <strong>quantity_ordered</strong> by <strong>price_each</strong>.<br><br>Label the calculated column "Order Value". Format the order value column so that only two digits are displayed after the decimal point.<br><br>Display only the first 10 results.</td>
    <td><img src='images/sample_40.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT MAX(c.customer_name), o.order_number,
TO_CHAR(SUM(od.quantity_ordered*od.price_each),'999,999,999.00')
AS "order value" FROM customers c
JOIN orders o ON o.customer_number = c.customer_number
JOIN order_details od ON od.order_number = o.order_number
GROUP BY o.order_number
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 41</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display the <strong>customer_name</strong>, and value of all <strong>orders</strong> made by that customer.<br><br>The value of each order is calculated by multiplying <strong>quantity_ordered</strong> by <strong>price_each</strong>.<br><br>Label the calculated column "Value of All <strong>orders</strong>". Format the order value column so that only two digits are displayed after the decimal point.<br><br>Display only the first 10 results.</td>
    <td><img src='images/sample_41.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT c.customer_name,
TO_CHAR(SUM(od.quantity_ordered*od.price_each),'999,999,999,00')
AS "value of all orders"
FROM customers c
JOIN orders o ON o.customer_number = c.customer_number
JOIN order_details od ON od.order_number = o.order_number
GROUP BY c.customer_number
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 42</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display the <strong>customer_number</strong>, <strong>order_number</strong>, and <strong>product_name</strong> values for each order using the <strong>orders</strong>, <strong>order_details</strong>, and <strong>products</strong> tables.<br><br>Display only the first 10 results.</td>
    <td><img src='images/sample_42.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT o.customer_number, od.order_number, pr.product_name
FROM order_details od
JOIN products pr ON pr.product_code = od.product_code
JOIN orders o ON o.order_number = od.order_number
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 43</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display the <strong>last_name</strong> of each Employee followed by the <strong>last_name</strong> of the Employee they report to.<br><br>Display only the first 10 results.</td>
    <td><img src='images/sample_43.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT e.last_name, b.last_name FROM employees e
JOIN employees b ON e.reports_to = b.employee_number
LIMIT 10;
```

</details>
</td>
</tr>
</table>

<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE 44</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>Display the <strong>first_name</strong> and <strong>last_name</strong> of each manager followed by the <strong>first_name</strong> and <strong>last_name</strong> of each employee they supervise. Sort the results by the <strong>last_name</strong> of each manager.<br><br>Display only the first 10 results.</td>
    <td><img src='images/sample_44.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
SELECT b.first_name, b.last_name, e.first_name, e.last_name
FROM employees e
JOIN employees b ON e.reports_to = b.employee_number
ORDER BY b.last_name
LIMIT 10;
```

</details>
</td>
</tr>
</table>
