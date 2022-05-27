


def bye_http(request, db):
    collection = db.collection(u'my_first_collection')
    docs = collection.stream()
    for doc in docs:
        print(doc._data["name"])
    return "Bye"