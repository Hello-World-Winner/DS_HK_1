-- What customers are from the UK
SELECT * FROM Customers WHERE Country = "UK"

-- What is the name of the customer who has the most orders?
SELECT Customers.CustomerName FROM orders
JOIN Orders on (Orders.CustomerID = Customers.CustomerID)
GROUP BY Customers.CustomerID) DESC
LIMIT 1

-- What supplier has the highest average product price?
SELECT Supplier.*

-- What category has the most orders?
SELECT 

-- What employee made the most sales (by number of sales)?
SELECT 

-- What employee made the most sales (by value of sales)?
SELECT 

-- What employees have BS degrees? (Hint: Look at LIKE operator)
SELECT 

-- What supplier has the highest average product price assuming they have at least 2 products (Hint: Look at the HAVING operator)
SELECT 
