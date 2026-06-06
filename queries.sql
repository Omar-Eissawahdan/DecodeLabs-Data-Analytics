-- Query 1: Filtering and Sorting (Key Requirement)
SELECT 
    Product, 
    Quantity, 
    UnitPrice, 
    TotalPrice
FROM Sales
WHERE TotalPrice > 1000
ORDER BY TotalPrice DESC;


-- Query 2: Aggregation and Grouping (Key Requirement)
SELECT 
    Product, 
    COUNT(*) AS Number_Of_Orders,
    SUM(Quantity) AS Total_Items_Sold, 
    SUM(TotalPrice) AS Total_Revenue
FROM Sales
GROUP BY Product
ORDER BY Total_Revenue DESC;


-- Query 3: Advanced Filtering with HAVING (Bonus Recommendation)
SELECT 
    Product, 
    AVG(UnitPrice) AS Average_Price
FROM Sales
GROUP BY Product
HAVING AVG(UnitPrice) > 150
ORDER BY Average_Price DESC;


-- Query 4: Percentage Contribution (Bonus Recommendation)
SELECT 
    Product, 
    SUM(TotalPrice) AS Category_Revenue,
    (SUM(TotalPrice) * 100.0 / (SELECT SUM(TotalPrice) FROM Sales)) AS Percentage_Contribution
FROM Sales
GROUP BY Product
ORDER BY Percentage_Contribution DESC;