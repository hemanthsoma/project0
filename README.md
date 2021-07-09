# Meals info project using MongoDB

**Use MongoDB for NoSQL**

> Meals info Database contains collection of foods with different countries.
> Python is a programming language linked with MongoDB which helps to access and retrive databases.

**Use Required Modules**

> pymongo is the standard MongoDB library and MongoClient method used to establish a connection to a MongoDB objects.
```
import warnings
from pymongo import MongoClient
warnings.filterwarnings('ignore')
```
> Client Collection with MongoDB
```
MongoClient(localhost,PortNumber)
```

## List of MongoDB Commands

**find_one()**

*find_one() method is used to return single document from the database collection*
```
db.collection.find_one()
```

**find()**

*find() method is used to select documents in a collection and return a cursor to the selected documents*
```
db.collection.find()
```

**limit()**

*limit() method to specify a maximum number of documents for a cursor to return*
```
db.collection.find().limit(number)
```

**insert_one()**

*insert_one() method is used to insert a record, or document*
```
db.collection.insert_one(record)
```

**insert_many()**

*insert_many() method is used to insert multiple documents into a collection*
```
db.collection.insert_many([{record1},{record2} ... {recordn}])
```

**update_one()**

*update_one() method is used to update single document into a collection*
```
db.collection.update_one(myquery,newvalues)
```

**update_many()**

*update_many() method is used to update multiple documents into a collection*
```
db.collection.update_many(filter,update,options)
```

**delete_one()**

*delete_one() method is used to delete one document or record from collection*
```
db.collection.delete_one(record)
```

**delete_many()**

*delete_many() method is used to delete multiple documents or records from collection*
```
db.collection.delete_many(records)
```

**count()**

*count() method is used to count number od documents from collection*
```
db.collection.find().count()
```

**sort()**
*sort() method is used to sort the collection of fields either ascending or descending order*
```
db.collection.find().sort([("name",1)])
```

**drop()**

*drop() method is used to delete entire documents in the database*
```
db.collection.drop()
```
