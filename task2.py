# Sample HTML text that we will parse
html_text = """
<html><head><title>The Dormouse's story</title></head><body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their
names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# Import BeautifulSoup library for HTML parsing
from bs4 import BeautifulSoup

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(html_text, "html.parser")

# i. Extract all links (href values) from <a> tags
print("All href links:")
for link in soup.find_all("a"):
    print(link.get("href"))

# ii. Extract class attribute values from all <a> tags
print("\nClass values of <a> tags:")
for link in soup.find_all("a"):
    print(link.get("class"))

# Import regex library for manual HTML parsing
import re

# Lists to store extracted values
href_links = []
class_values = []

# Function to recursively parse HTML and extract information
def parse_html(html):
    
    # Find the first <a ...> tag in the HTML
    match = re.search(r'<a\s+([^>]+)>', html)
    
    # Stop recursion if no <a> tag is found
    if not match:
        return
    
    # Extract the attributes part of the tag
    tag_content = match.group(1)

    # Extract the href value using regex
    href_match = re.search(r'href="([^"]+)"', tag_content)
    if href_match:
        href_links.append(href_match.group(1))

    # Extract the class value using regex
    class_match = re.search(r'class="([^"]+)"', tag_content)
    if class_match:
        class_values.append(class_match.group(1))

    # Continue searching in the remaining part of the HTML
    remaining_html = html[match.end():]
    parse_html(remaining_html)


# Call the function to start parsing
parse_html(html_text)

# Print extracted href links
print("Href Links:", href_links)

# Print extracted class values
print("Class Values:", class_values)