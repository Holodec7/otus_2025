import json
import os
from csv import DictReader


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "books.csv"), "r") as f:
    books = list(DictReader(f))

with open(os.path.join(BASE_DIR, "users.json"), "r") as f1:
    users = json.load(f1)

filtered_books = [
    {
        "title": book["Title"],
        "author": book["Author"],
        "pages": book["Pages"],
        "genre": book["Genre"]
    } for book in books
]

books_iter = iter(filtered_books)

num_users = len(users)
num_books = len(filtered_books)
books_one_user = [num_books // num_users] * num_users
for i in range(num_books % num_users):
    books_one_user[i] += 1

for user, count in zip(users, books_one_user):
    user["books"] = [next(books_iter) for _ in range(count)]

with open("result.json", "w") as f:
    json.dump(users, f, indent=4)

