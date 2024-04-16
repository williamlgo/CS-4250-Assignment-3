#-------------------------------------------------------------------------
# AUTHOR: William Go
# FILENAME: db_connetion_mongo.py
# SPECIFICATION: Collection of Documents with Terms
# FOR: CS 4250- Assignment #3
# TIME SPENT: 4 Hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with
# standard arrays

#importing some Python libraries
# --> add your Python code here
from pymongo import MongoClient
import datetime

def connectDataBase():

    # Create a database connection object using pymongo
    # --> add your Python code here
    DB_NAME = "CPP"
    DB_HOST = "localhost"
    DB_PORT = 27017
    try:
        client = MongoClient(host=DB_HOST, port=DB_PORT)
        db = client[DB_NAME]
        return db
    except:
        print("Database not connected successfully")


def createDocument(col, docId, docText, docTitle, docDate, docCat):

    # create a dictionary indexed by term to count how many times each term appears in the document.
    # Use space " " as the delimiter character for terms and remember to lowercase them.
    # --> add your Python code here
    #This would use docText to count how many times each term appears and add it into the dictionary

    # create a list of objects to include full term objects. [{"term", count, num_char}]
    # --> add your Python code here
    #This would be added into the list that describes the embedded term 
    terms = []

    # produce a final document as a dictionary including all the required document fields
    # --> add your Python code here

    collection = {
        "_id": docId,
        "text": docText,
        "title": docTitle,
        "num_chars": int(docText.len()),
        "date": docDate,
        "category": docCat,
        "terms": terms
    }

    # insert the document
    # --> add your Python code here
    col.insert_one(collection)

def deleteDocument(col, docId):

    # Delete the document from the database
    # --> add your Python code here
    col.delete_one(docId)


def updateDocument(col, docId, docText, docTitle, docDate, docCat):

    # Delete the document
    # --> add your Python code here
    col.delete_one(docId)

    # Create the document with the same id
    # --> add your Python code here
    createDocument(col, docId, docText, docTitle, docDate, docCat)

def getIndex(col):

    # Query the database to return the documents where each term occurs with their corresponding count. Output example:
    # {'baseball':'Exercise:1','summer':'Exercise:1,California:1,Arizona:1','months':'Exercise:1,Discovery:3'}
    # ...
    # --> add your Python code here
    index = ''