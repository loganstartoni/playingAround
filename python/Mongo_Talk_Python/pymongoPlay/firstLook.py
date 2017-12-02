import pymongo

conn_str = "mongodb://192.168.1.201:27017"
client = pymongo.MongoClient(conn_str)

db = client.small_bookstore

# Insert Stuff

# Previously Inserted
if db.books.count() == 0:
    print("Inserting 6 Books.")
    resp = db.books.insert({'title': 'The First Book', 'ISBN': '1234567654323456'})
    resp = db.books .insert({'title': 'The Second Book', 'ISBN': '6543456787654345'})
    resp = db.books .insert({'title': 'The Third Book', 'ISBN': '23454345654345434565434'})
    resp = db.books .insert({'title': 'The Fourth Book', 'ISBN': '54565456765456765456765'})
    resp = db.books .insert_one({'title': 'The fifth Book', 'ISBN': '876898767876789876567876'})
    resp = db.books .insert_one({'title': 'The sixth Book', 'ISBN': '3454345434565434565455'})
else:
    print("Books are already Inserted.")


# Find One object and update it
# book = db.books.find_one({'ISBN': '1234567654323456'})
# print(book, type(book))
# book['favorited_by'] = []
# print("already contains favorited by")
# book['favorited_by'].append(100)
# db.books.update({'_id': book.get('_id')}, book)
# book = db.books.find_one({'ISBN': '1234567654323456'})
# print(book)

book = db.books.find_one({'ISBN': '876898767876789876567876'})
print(book)
book = db.books.update({'ISBN': '876898767876789876567876'}, {'$addToSet': {'favorited_by': 101}})
book = db.books.find_one({'ISBN': '876898767876789876567876'})
print(book)
