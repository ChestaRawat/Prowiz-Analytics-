# Import required libraries
import requests          # To fetch data
import pandas as pd      # For data manipulation and analysis
import numpy as np       # For numerical operations (not strictly needed here but imported)

# API endpoint from where we will fetch the posts data
url = "https://jsonplaceholder.typicode.com/posts"

# Send a GET request to the API
response = requests.get(url)

# Convert the API response (JSON format) into Python list/dictionary
data = response.json()

# Print each post individually
# This loop iterates through all posts returned by the API
for post in data:
    print(post)

# Convert the JSON data into a Pandas DataFrame
# This makes it easier to analyze the data
df = pd.DataFrame(data)

# Print the DataFrame to view the structured data
print(df)

# Count the number of distinct users who created posts
# nunique() returns the count of unique values in the column
distinct_users = df['userId'].nunique()

print("Distinct Users:", distinct_users)

# Count how many posts each user has created
# value_counts() counts occurrences of each userId
post_counts = df['userId'].value_counts()

print(post_counts)

# Identify the user with the highest number of posts
# idxmax() returns the userId with maximum posts
highest_user = post_counts.idxmax()

# max() returns the highest number of posts
highest_posts = post_counts.max()

print("User with highest posts:", highest_user)
print("Number of posts:", highest_posts)

# Create a new column that counts number of words in each title
# split() divides the title into words and len() counts them
df['title_word_count'] = df['title'].apply(lambda x: len(x.split()))

# Calculate the average word count across all titles
average_word_length = df['title_word_count'].mean()

print("Average word length of title:", average_word_length)