SELECT * FROM MealsInfo.table_info;

-- To select a row from table

SELECT * FROM MealsInfo.table_info limit 1;

-- To select limited rows from table

SELECT * FROM table_info limit 5;

-- Delete

DELETE from table_info WHERE meal_id = 1438;
SELECT * FROM table_info;

-- Update

UPDATE table_info SET category = "Salad" WHERE meal_id = 2307;
SELECT * FROM table_info;

-- Insert

INSERT into table_info values(1755, "Beverages", "Thai");
SELECT * FROM table_info;

-- Drop a table

DROP table table_info;
SELECT * FROM table_info;

-- Sort in order
SELECT * FROM table_info ORDER BY Pizza ASC;
