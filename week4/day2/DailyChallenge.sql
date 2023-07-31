-- Database: DailyChallenge

-- Q1. What will be the OUTPUT of the following statement?

--     SELECT COUNT(*) 
--     FROM firstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM secondtab WHERE id IS NULL )
-- 	the ouput is 0

-- Q2. What will be the OUTPUT of the following statement?

--     SELECT COUNT(*) 
--     FROM firstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM secondTab WHERE id = 5 )

-- the output is 3

-- Q3. What will be the OUTPUT of the following statement?

--     SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )

-- the output is 2

-- Q4. What will be the OUTPUT of the following statement?

--     SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )
	
-- the output is 3