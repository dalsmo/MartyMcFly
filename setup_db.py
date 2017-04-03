#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Dev script to setup a test database. """

import sqlite3 as lite
import time

con = lite.connect('fluxCapacitor.db')

with con:

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS logs")
    cur.execute(
        "CREATE TABLE logs(id INT, memberName TEXT, action TEXT," +
        "timestamp timestamp)"
    )

    temp_id = 1
    rfId = 2016050010
    nick_temp = 'John Doe'
    cur.execute("INSERT INTO logs VALUES (?,?,?,?);",
                (temp_id, nick_temp, "login",time.time()))
