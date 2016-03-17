import sqlite3 as lite
from datetime import datetime, date

con = lite.connect('fluxCapacitor.db',detect_types=lite.PARSE_DECLTYPES)
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM logs")
    rows = cur.fetchall()

    # get all different ID

    #for each ID
     # get all exits
     # find erliest entry time
     
    
    

