#!/usr/bin/env python
#
# Assignment #1: Logs Analysis
# Contains the Get Posts function to run query on news SQL file.

import psycopg2

DBNAME = "news"


def get_posts(query):
    """Return all posts from the 'database', given the proper query."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    posts = c.fetchall()
    db.close()
    return posts
