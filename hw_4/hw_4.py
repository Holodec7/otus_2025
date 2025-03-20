
import json
from csv import DictReader

with open ("/Users/gromkott/Desktop/otus_2025/hw_4/books.csv", "r") as f:
    books = list(DictReader(f))

with open("/Users/gromkott/Desktop/otus_2025/hw_4/users.json", "r") as f1:
    users = json.load(f1)

books_iter = iter(books)
num_users = len(users)
num_books = len(books)
books_one_user = [num_books//num_users]*num_books
for i in range(num_books%num_users):
    books_one_user[i] +=1

print(books_one_user)

for user, count in zip(users, books_one_user):
    user["books"] = [next(books_iter) for _ in range(count)]

with open("result.json", "w") as f:
    json.dump(users, f, indent=4)







