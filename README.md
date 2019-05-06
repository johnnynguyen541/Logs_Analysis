# Project Title: Log Analysis

This is for the first project for Udacities course.  Per Udacity Curriculum:
Your task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

## Getting Started

You will need to have vagrant installed on your system.
You will need to download the newsdata.sql database, and place in your Vagrant directory, shared with your virtual machine.  In that same directory, place "news.py" and "newsdb.py" files into those directories.
Then, you will need to bring the virtual machine up using the following command `vagrant up`.  Then log into it with `vagrant ssh`.

### Prerequisites

You will need to have "psycopg2" installed in your Vagrant environment.  Run the following command:
```
sudo apt-get install python-psycopg2
```

### Running the tests

To run, run the news.py file with python:

```
python news.py
```

You should see a command line interface:

```
        ************************************
          News Database/Log Analysis CLI
        ************************************
        1) What are the most popular three articles of all time?
        2) Who are the most popular article authors of all time?
        3) On which days did more than 1 percent of requests lead to errors?
        q) Quit Program
```

Enter into the CLI  numbers 1, 2, or 3 to run the appropriate query as seen below:

```
Enter your selection: 1
Title                             | Views
----------------------------------+--------
Candidate is jerk, alleges rival  | 342102
Bears love berries, alleges bear  | 256365
Bad things gone, say good people  | 171762
```

To Exit CLI, enter 'q' or 'Q':