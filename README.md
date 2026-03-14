# Prowiz Analytics Assessment

This repository contains solutions for the Python and SQL technical assessment.
The tasks involve working with APIs, HTML parsing, FastAPI development, data analysis, and SQL queries using SQLite3.

---

# Technologies Used

* Python
* Requests
* Pandas
* BeautifulSoup
* FastAPI
* SQLite3
* SQL

---

# Project Structure

```
Prowiz-Analytics
│
├── task1.py        # Python API data extraction and analysis
├── task2.py        # HTML parsing using BeautifulSoup
├── task3.py        # FastAPI application
├── task4.py        # Data analysis using Python
├── task5.sql       # SQL queries using SQLite3
└── README.md       # Documentation
```

---

# Task 1 – Python API Requests

API Used:
https://jsonplaceholder.typicode.com/posts

Objectives:

* Fetch all posts using the Python **requests** library.
* Convert the response data into a structured format.
* Count the number of distinct users.
* Identify the user with the highest number of posts.
* Calculate the average word length of post titles.

Tools used:

* requests
* pandas

File: `task1.py`

---

# Task 2 – HTML Parsing

Objective:
Parse HTML content and extract specific elements.

Tasks performed:

* Extract all **href links** from `<a>` tags.
* Extract **class attributes** of `<a>` tags.
* Demonstrate parsing using **BeautifulSoup**.
* Implement an alternative solution without BeautifulSoup using **regex/string parsing**.

File: `task2.py`

Libraries used:

* BeautifulSoup
* re

---

# Task 3 – FastAPI Application

A simple FastAPI application was created with two endpoints.

API Endpoints:

1. **Sum API**

   * Accepts two numbers as input.
   * Returns their sum.
   * Handles invalid inputs with error handling.

2. **Uppercase API**

   * Accepts a lowercase string.
   * Returns the string converted to uppercase.

Framework used:

* FastAPI

File: `task3.py`

---

# Task 4 – Data Analysis

Dataset Used:
Global Electronics Retailer Dataset

Analysis performed:

* Data loading and preprocessing
* Revenue analysis
* Product performance analysis
* Country-wise sales insights
* Basic exploratory data analysis

Libraries used:

* pandas
* numpy

File: `task4.py`

---

# Task 5 – SQL Queries (Using SQLite3)

Database Used: **SQLite3**

Objective:
Identify the **second topper in class** under different ranking conditions.

Tasks performed:

### (a) Second Topper in Class

Find the second highest marks using sorting and limit.

### (b) Second Topper with Alphabetical Tie Break

If multiple students have the same marks, ranking is determined alphabetically.

### (c) Second Rank with Ties

If multiple students share the same marks, they receive the same rank using **DENSE_RANK()**.

File: `task5.sql`

Example SQL logic used:

```
SELECT name, marks
FROM (
    SELECT name, marks,
           DENSE_RANK() OVER (ORDER BY marks DESC) AS rnk
    FROM students
)
WHERE rnk = 2;
```

---

# How to Run

Clone the repository:

```
git clone https://github.com/<your-username>/Prowiz-Analytics.git
```

Navigate to the project folder:

```
cd Prowiz-Analytics
```

Run Python scripts:

```
python task1.py
python task2.py
python task3.py
python task4.py
```

Run SQL queries using SQLite:

```
sqlite3 database.db
.read task5.sql
```

---

# Author

Chesta Rawat
