
import mysql.connector as mysql

con =mysql.connect(host="localhost",
    user="root",
    password="123456789",
    database="employee_fp_6")
cur = con.cursor()
cur.execute('''
CREATE TABLE employees (
emp_id INT PRIMARY KEY,
emp_name VARCHAR(100),
department VARCHAR(50),
job_name VARCHAR(50),
manager_id INT NULL,
hire_date DATE,
salary DECIMAL(10,2),
commission DECIMAL(10,2) NULL
)''');


cur.execute('''
CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    sale_date DATE NOT NULL,
    amount DECIMAL(12,2) NOT NULL
)
''')


cur.execute('''
CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY AUTOINCREMENT,
    col1 VARCHAR(50) NOT NULL,
    col2 VARCHAR(50) NOT NULL,
    transaction_date DATE,
    amount DECIMAL(12,2)
)
''')

emp_values = [
    (1, 'Ram', 'Science', 'Developer', 1, '2019-09-22', 60000, None),
    (2, 'Prasad', 'Mathematics', 'Tester', 1, '2023-05-23', 25000, None),
    (3, 'Kiran', 'CSE', 'Chief Executive', 1, '2012-11-12', 30000, None),
    (4, 'Shankar', 'IT', 'Manager', 1, '2017-09-06', 100000, None),
    
]
cur.executemany("""INSERT INTO employees (emp_id, emp_name, department, job_name, manager_id, hire_date, salary, commission)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""", emp_values)

sales_values = [
    (1, '2020-09-08', 5000.00),
    (2, '2019-04-23', 10000.00),
    (3, '2024-09-02', 15000.00),
    (4, '2021-03-31', 20000.00)
]
cur.executemany("INSERT INTO sales(sale_id,sale_date,amount) VALUES (%s, %s, %s)", sales_values)


transactions_values = [
    ('WWE', 'VCX', '2020-09-31', 250.00),
    ('XEC', 'RTF', '2017-09-06', 550.00),
    ('REX', 'YTF', '2023-04-13', 2000.00),
    ('BVC', 'FRC', '2021-03-31', 1000.00),
    ('BVC', 'VCX', '2023-06-05', 3550.00)
]
cur.executemany("INSERT INTO transactions (col1, col2, transaction_date, amount) VALUES (%s, %s, %s, %s)", transactions_values)

con.commit()

#1
cur.execute("""
SELECT salary FROM employees
ORDER BY DESC LIMIT 1 OFFSET 0
""")
print("second highest salary", cur.fetchone()[0])


#2
cur.execute("""
SELECT emp_name, department, salary
FROM employees e
WHERE salary > (
    SELECT AVG(salary) FROM employees WHERE department = e.department
)
""")
print("employees in evey department :\n")
for row in cur.fetchall():
    print(row)

#3
cur.execute("""
SELECT date, amount,
       SUM(amount) OVER (ORDER BY date) AS total
FROM sales
""")
print("\total of sales amounts:")
for row in cur.fetchall():
    print(row)

#4
cur.execute("""
SELECT col1, col2, COUNT(*) AS count
FROM transactions
GROUP BY col1, col2
HAVING COUNT(*) > 1
""")
print("\n dupliacate combinations:")
for row in cur.fetchall():
    print(row)
