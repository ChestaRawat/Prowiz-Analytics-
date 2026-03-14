-- Task 5: SQL Topper in Class
-- Database Used: SQLite3

-- Create table
CREATE TABLE students(
    name TEXT,
    marks INTEGER
);

-- Insert sample data
INSERT INTO students VALUES
('Sahil',95),
('Kaushik',90),
('John',89),
('Kara',87),
('Simpson',97);

------------------------------------------------
-- (a) Find the second topper in class
------------------------------------------------

SELECT name, marks
FROM students
ORDER BY marks DESC
LIMIT 1 OFFSET 1;

------------------------------------------------
-- (b) Second topper with alphabetical ranking
------------------------------------------------

SELECT name, marks
FROM students
ORDER BY marks DESC, name ASC
LIMIT 1 OFFSET 1;

------------------------------------------------
-- (c) Second rank with ties
------------------------------------------------

SELECT name, marks
FROM (
    SELECT name, marks,
           DENSE_RANK() OVER (ORDER BY marks DESC) AS rnk
    FROM students
)
WHERE rnk = 2;
