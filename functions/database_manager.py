

def delete_collection(db, collection):
    docs = db.collection(collection).stream()
    counter = 0
    for doc in docs:
        counter += 1
        doc.reference.delete()
    if(counter > 0):
        return f"Deleted {counter} documents", 200
    else:
        return f"Wasn't able to delete documents. Either the collection does not exist or it is empty", 400
    