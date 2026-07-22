#CH-3-Display
#1number of products
#2highest price
@#lowest price
#inasinglequery.

USE data_science_journey;

SELECT 
    COUNT(*) as TotalProducts,  
    MAX(Price) as HighestPrice, 
    MIN(Price) as LowestPrice

FROM sales;