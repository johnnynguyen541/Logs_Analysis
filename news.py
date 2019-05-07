#!/usr/bin/env python
#
# Assignment #1: Logs Analysis
# News CLI service to connect to forum

from newsdb import get_posts

# Query String #1: What are the most popular three articles of all time?
query_1 = """SELECT articles.title, COUNT(*) AS views
        FROM log JOIN articles
        ON log.path LIKE CONCAT('%', articles.slug)
        GROUP BY articles.title
        ORDER by views DESC
        LIMIT 3;"""

# Query String #2: Who are the most popular article authors of all time?
query_2 = """SELECT authors.name, subqa.views
            FROM authors,
                (SELECT articles.author, COUNT(*) AS views
                FROM log JOIN articles
                ON log.path LIKE CONCAT('%', articles.slug)
                GROUP BY articles.author
                ORDER by views DESC) AS subqa
            WHERE authors.id = subqa.author;"""

# Query String #3 On which days did more than 1% of requests lead to errors?
query_3 = """SELECT subqa.date, CAST(subqb.fail AS FLOAT) / subqa.total * 100
                AS error_rate
            FROM (SELECT date_trunc('day', time) AS date, count(*) AS total
                FROM log
                GROUP BY date) AS subqa,
                (SELECT date_trunc('day', time) AS date, count(*) AS fail
                FROM log
                WHERE status = '404 NOT FOUND'
                GROUP BY date) AS subqb
            WHERE subqa.date = subqb.date
                AND CAST(subqb.fail AS FLOAT) / subqa.total * 100 >= 1.0
            ORDER BY error_rate DESC;"""


# Troubleshooting Main Menu
def MainMenu():
    """Menu CLI.  User can enter 1-3 for appropriate query, 'q' to exit"""

    # Print Version number
    print("Udacity Log Analysis Project #1\n")

    # Runs Loop to see what option needs to be run
    exit = False
    while exit is False:

        # Print Main Menu
        menu = """
        ************************************
          News Database/Log Analysis CLI
        ************************************
        1) What are the most popular three articles of all time?
        2) Who are the most popular article authors of all time?
        3) On which days did more than 1 percent of requests lead to errors?
        q) Quit Program
        """
        print(menu)

        # Read Command Line Input
        selection = raw_input('Enter your selection: ')

        # Menu Selection
        if selection == '1':
            # Run Query 1 and output to terminal
            results = get_posts(query_1)
            print('{:33s} {:1s} {:6s}'.format('Title', '|', 'Views'))
            print("----------------------------------+--------")
            for x in results:
                print('{:33s} {:1s} {:6d}'.format(x[0], '|', x[1]))
        elif selection == '2':
            # Run Query 2 and output to terminal
            results = get_posts(query_2)
            print('{:33s} {:1s} {:6s}'.format('Name', '|', 'Views'))
            print("----------------------------------+--------")
            for x in results:
                print('{:33s} {:1s} {:6d}'.format(x[0], '|', x[1]))
        elif selection == '3':
            # Run Query 3 and output to terminal
            results = get_posts(query_3)
            print('{:13s} {:1s} {:16s}'.format('Date', '|', 'Error_Rate'))
            print("--------------+------------------")
            for x in results:
                date = str(x[0])[0:10]
                print('{:13s} {:1s} {:16.14f}'.format(date, '|', x[1]))
        elif selection == 'q' or selection == 'Q':
            # Exit CLI
            exit = True
        else:
            # Prompt user that they selected an invalid selection
            print("Invalid Selection!\n")

# -------------------------------------------------------------------
#  Run Main Menu
# -------------------------------------------------------------------


MainMenu()
