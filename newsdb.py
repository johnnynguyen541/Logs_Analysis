#!/usr/bin/env python
#
# Assignment #1: Logs Analysis
# Contains the Get Posts function to run query on news SQL file.

import psycopg2
import sys

DBNAME = "news"


def get_posts(query):
    """Return all posts from the 'database', given the proper query."""
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query)
        posts = c.fetchall()
        db.close()
        return posts
    except psycopg2.Error as e:
        print("Unable to connect to the database")
        print(e.pgerror)
        print(e.diag.message_detail)
        sys.exit(1)
