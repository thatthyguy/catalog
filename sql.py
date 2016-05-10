import sqlite3 as sql3

# to do
# create the database schemea
# add checking to make sure the schema exists 
# write functions for adding items to the database
# make sure the INSERT function checks for existing/duplicate entries
# write a search function to locate items based upon the schema

# schema - just one big ole' table for now
# table name: pdfs
# id: primary key int
# full_path: char 
# filename: char
# author: char
# title: char
# page length: int
# publisher (maybe): char


# If the database doesn't exist, it will be created. 


def create_table():
    conn = sql3.connect('catalog.db')
    cur = conn.cursor()

    # create the table
    cur.execute(''' CREATE TABLE pdf
        (id INTEGER PRIMARY KEY, full_path text, filename text, author text,
         title text, length integer, publisher text)''')

    conn.commit()
    cur.close()
