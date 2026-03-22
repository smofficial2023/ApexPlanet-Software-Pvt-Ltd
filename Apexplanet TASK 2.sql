USE customer_database;
SELECT * FROM zepto_customer_table;

SELECT 
    P_ID,
    PName,
    Brand,
    SUM(Qty * Price) AS Total_Revenue
FROM zepto_customer_table
WHERE Order_Date >=(
    SELECT MAX(Order_Date) - INTERVAL 6 MONTH 
    FROM zepto_customer_table
)
GROUP BY P_ID, PName, Brand
ORDER BY Total_Revenue
LIMIT 5;

SELECT 
    DATE_FORMAT(created_date, '%m') AS New_Signup_Month,
    COUNT(DISTINCT C_ID) AS New_Users
FROM zepto_customer_table
GROUP BY New_Signup_Month
ORDER BY New_Signup_Month;

SELECT State, City, AVG(Price) AS Average_Order_Value FROM zepto_customer_table
GROUP BY State, City
HAVING Average_Order_Value>470
ORDER BY Average_Order_Value DESC;

SELECT 
    ROUND(
        100.0 * SUM(CASE WHEN order_count > 1 THEN 1 ELSE 0 END) 
        / COUNT(*), 2
    ) AS repeat_customer_percentage
FROM (
    SELECT 
        C_ID,
        COUNT(C_ID) AS order_count
    FROM zepto_customer_table
    GROUP BY C_ID
) AS user_orders;

SELECT 
    Category,
    COUNT(P_ID) AS Order_Frequency,
    SUM(Qty * Price) AS Total_Revenue
FROM zepto_customer_table
GROUP BY Category
ORDER BY Order_Frequency DESC, Total_Revenue ASC;

SELECT 
    DISTINCT City,
    AVG(Prod_Rating) AS Average_Product_Rating
FROM zepto_customer_table
GROUP BY City
ORDER BY Average_Product_Rating;

SELECT 
    C_ID,
    CName,
    email,
    total_revenue
FROM (
    SELECT 
        C_ID,
        CName,
        email,
        total_revenue,
        SUM(total_revenue) OVER (ORDER BY total_revenue DESC) AS cumulative_revenue,
        SUM(total_revenue) OVER () AS total_revenue_all
    FROM (
        SELECT 
            C_ID,
            CName,
            email,
            SUM(Qty * Price) AS total_revenue
        FROM zepto_customer_table
        GROUP BY C_ID, CName, email
    ) t1
) t2
WHERE cumulative_revenue <= 0.2 * total_revenue_all;