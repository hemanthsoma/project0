SELECT * FROM MealsInfo;

-- To select a row from table

SELECT * FROM MealsInfo limit 1;

-- To select limited rows from table

SELECT * FROM table limit 5;

-- Delete

DELETE from table
SELECT * FROM table WHERE meal_id = 1438;


-- Update

UPDATE table
SET category = "Salad" WHERE meal_id = 2307;
SELECT * FROM table;

-- Insert

INSERT into table values(1755, "Beverages", "Thai");
SELECT * FROM table;

-- Drop a table

INSERT into table values(2640,"Starters","Thai");
SELECT * FROM table;

-- Sort in order
SELECT * FROM table ORDER BY Pizza DESC;
