#!/usr/bin/python3
""""""
import MySQLdb
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    user1 = os.getenv('CV_MYSQL_USER')
    host1 = os.getenv('CV_MYSQL_HOST')
    pwd1 = os.getenv('CV_MYSQL_PWD')

    db = MySQLdb.connect(
            host= host1,
            user = user1,
            passwd = pwd1
            )

    cursor = db.cursor()

    cursor.execute("CREATE DATABASE cv_db")

    print("All done!")
