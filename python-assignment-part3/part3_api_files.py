# part3_api_files.py
# File I/O, APIs & Exception Handling

import requests
from datetime import datetime

# -------------------- LOGGER FUNCTION --------------------

def log_error(function_name, error_type, message):
    """Logs error with timestamp into file"""
    with open("error_log.txt", "a", encoding="utf-8") as f:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{time}] ERROR in {function_name}: {error_type} — {message}\n")


# -------------------- TASK 1: FILE I/O --------------------

# Write file
with open("python_notes1.txt", "w", encoding="utf-8") as f:
  f.write("Topic 1: Variables store data. Python is dynamically typed.\n")
  f.write("Topic 2: Lists are ordered and mutable.\n")
  f.write("Topic 3: Dictionaries store key-value pairs.\n")
  f.write("Topic 4: Loops automate repetitive tasks.\n")
  f.write("Topic 5: Exception handling prevents crashes.\n")
  print("File written successfully.")

# Append
with open("python_notes1.txt", "a", encoding="utf-8") as f:
  f.write("Topic 6: Functions help reuse code.\n")
  f.write("Topic 7: APIs allow communication between systems.\n")
  print("Lines appended.")

# Read file
with open("python_notes1.txt", "r", encoding="utf-8") as f:
  lines = f.readlines()


print("\n--- FILE CONTENT ---")
for i, line in enumerate(lines, 1):
  print(f"{i}. {line.strip()}")

print("\n Total lines:", len(lines))

# Keyword search
keyword = input("\n Enter keyword to search: ").lower()
found = False

for line in lines:
  if keyword in line.lower():
    print(line.strip())
    found = True
    
    if not found:
      print("No matching lines found for the given keyword.")


# -------------------- TASK 2: API --------------------

import requests

BASE_URL = "https://dummyjson.com/products"

def fetch_products():
    try:
        response = requests.get(f"{BASE_URL}?limit=20", timeout=5)
        data = response.json()

        print("\n--- PRODUCTS ---")
        for p in data["products"]:
            print(f"{p['id']} | {p['title'][:25]:25} | {p['category']} | ${p['price']} | {p['rating']}")

        return data["products"]

    except requests.exceptions.ConnectionError:
        print("Connection failed.")
        log_error("fetch_products", "ConnectionError", "No connection")
        return []

    except requests.exceptions.Timeout:
        print("Request timed out.")
        log_error("fetch_products", "Timeout", "Server slow")
        return []

    except Exception as e:
        print(e)
        log_error("fetch_products", "Exception", str(e))
        return []


products = fetch_products()

# Filter & sort
if products:
    filtered = [p for p in products if p["rating"] >= 4.5]
    filtered.sort(key=lambda x: x["price"], reverse=True)

    print("\n--- FILTERED PRODUCTS ---")
    for p in filtered:
        print(p["title"], p["price"])


# Category search
try:
    res = requests.get(f"{BASE_URL}/category/laptops", timeout=5)
    data = res.json()

    print("\n--- LAPTOPS ---")
    for p in data["products"]:
        print(p["title"], "-", p["price"])

except requests.exceptions.ConnectionError:
    print("Connection failed.")
    log_error("category_search", "ConnectionError", "No connection")

except requests.exceptions.Timeout:
    print("Request timed out.")
    log_error("category_search", "Timeout", "Server slow")

except Exception as e:
    print(e)
    log_error("category_search", "Exception", str(e))


# POST request
try:
    new_product = {
        "title": "My Custom Product",
        "price": 999,
        "category": "electronics",
        "description": "Created via API"
    }

    res = requests.post(f"{BASE_URL}/add", json=new_product, timeout=5)
    print("\nPOST Response:", res.json())

except requests.exceptions.ConnectionError:
    print("Connection failed.")
    log_error("post_request", "ConnectionError", "No connection")

except requests.exceptions.Timeout:
    print("Request timed out.")
    log_error("post_request", "Timeout", "Server slow")

except Exception as e:
    print(e)
    log_error("post_request", "Exception", str(e))


# -------------------- TASK 3: Exception Handling  --------------------

# Safe divide
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"


print("\n--------Part A: Guarded Calculator----------")
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("ten", 2))


# Safe file read
# Part B: Guarded File Reader

def read_file_safe(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    finally:
        print("File operation attempt complete.")

print("\n----- Part B: Guarded File Reader -----")
print("\nReading python_notes.txt:")
content1 = read_file_safe("python_notes.txt")
if content1 is not None:
    print(content1)

print("\nReading ghost_file.txt:")
content2 = read_file_safe("ghost_file.txt")
if content2 is not None:
    print(content2)

# Part C: Robust API

def fetch_products():
    try:
        response = requests.get(f"{BASE_URL}?limit=20", timeout=5)
        data = response.json()

        print("\n--- PRODUCTS ---")
        for p in data["products"]:
            print(f"{p['id']} | {p['title'][:25]:25} | {p['category']} | ${p['price']} | {p['rating']}")

        return data["products"]

    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except Exception as e:
        print(e)


print("\n----- Part C: Robust API Calls -----")
products = fetch_products()

if products:
    filtered = [p for p in products if p["rating"] >= 4.5]
    filtered.sort(key=lambda x: x["price"], reverse=True)

    print("\n--- FILTERED PRODUCTS ---")
    for p in filtered:
        print(p["title"], p["price"])


try:
    res = requests.get(f"{BASE_URL}/category/laptops", timeout=5)
    data = res.json()

    print("\n--- LAPTOPS ---")
    for p in data["products"]:
        print(p["title"], "-", p["price"])

except requests.exceptions.ConnectionError:
    print("Connection failed. Please check your internet.")
except requests.exceptions.Timeout:
    print("Request timed out. Try again later.")
except Exception as e:
    print(e)


try:
    new_product = {
        "title": "My Custom Product",
        "price": 999,
        "category": "electronics",
        "description": "Created via API"
    }

    res = requests.post(f"{BASE_URL}/add", json=new_product, timeout=5)
    print("\nPOST Response:")
    print(res.json())

except requests.exceptions.ConnectionError:
    print("Connection failed. Please check your internet.")
except requests.exceptions.Timeout:
    print("Request timed out. Try again later.")
except Exception as e:
    print(e)



# Part D: Input Validation tool

while True:
    user = input("\nEnter product ID (1–100) or 'quit': ")

    if user.lower() == "quit":
        break

    if not user.isdigit():
        print("Invalid input")
        continue

    pid = int(user)

    if pid < 1 or pid > 100:
        print("Warning: Product Id should be between 1 to 100")
        continue

    try:
        res = requests.get(f"{BASE_URL}/{pid}", timeout=5)

        if res.status_code == 404:
            print("Product not found.")
        elif res.status_code == 200:
            data = res.json()
            print(f"Title: {data['title']}")
            print(f"Price: ${data['price']}")
        else:
            print("Failed to fetch product details.")

    except requests.exceptions.RequestException as e:
        print(f"Connection failed. Please check your internet: {e}")
    except requests.exceptions.Timeout:
        print(f"Request timed out. Try again later")
    except Exception as e:
        print(e)

# -------------------- TASK 4: Logging to File  --------------------

import requests
from datetime import datetime

def log_error(function_name, error_type, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("error_log.txt", "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] ERROR in {function_name}: {error_type} — {message}\n")


# 1. Trigger and log a ConnectionError
try:
    requests.get("https://this-host-does-not-exist-xyz.com/api", timeout=5)
except requests.exceptions.ConnectionError:
    print("Connection failed.")
    log_error("fetch_products", "ConnectionError", "No connection could be made")
except requests.exceptions.Timeout:
    print("Request timed out.")
    log_error("fetch_products", "Timeout", "Request took too long")
except Exception as e:
    print(e)
    log_error("fetch_products", "Exception", str(e))


# 2. Trigger and log an HTTP error manually
try:
    product_id = 999
    response = requests.get(f"https://dummyjson.com/products/{product_id}", timeout=5)

    if response.status_code != 200:
        print("Unexpected response received.")
        log_error(
            "lookup_product",
            "HTTPError",
            f"{response.status_code} Not Found for product ID {product_id}"
        )
    else:
        product = response.json()
        print("Product found:", product["title"])

except requests.exceptions.ConnectionError:
    print("Connection failed.")
    log_error("lookup_product", "ConnectionError", "No connection could be made")
except requests.exceptions.Timeout:
    print("Request timed out.")
    log_error("lookup_product", "Timeout", "Request took too long")
except Exception as e:
    print(e)
    log_error("lookup_product", "Exception", str(e))


# 3. Read and print the full log file
print("\n----- Contents of error_log.txt -----")
with open("error_log.txt", "r", encoding="utf-8") as file:
    print(file.read())
