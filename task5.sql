-- Task 5(a)
SELECT name, marks
FROM students
ORDER BY marks DESC
LIMIT 1 OFFSET 1;

-- Task 5(b)
SELECT name, marks
FROM (
SELECT name, marks,
ROW_NUMBER() OVER (ORDER BY marks DESC, name ASC) AS rnk
FROM students
) t
WHERE rnk = 2;

-- Task 5(c)
SELECT name, marks
FROM (
SELECT name, marks,
DENSE_RANK() OVER (ORDER BY marks DESC) AS rnk
FROM students
) t
WHERE rnk = 2;