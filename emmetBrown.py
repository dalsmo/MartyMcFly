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


     entry
     mashine
     mashine
     exit

     entry
     mashine
     mashine

     mashine
     mashine
     exit


     mashine
     mashine

     mashine

     Entry and exit gives full time, for one day
     else just string together mashines????

     4am kicks you out???
     avklingnings time????
     forcelogga alla om lokalen stängs??

     det kommer alltid gå att missanvända sustemet
     logga efter mashines går ej att göra,
         missvisande och problem med före jobbet besökare
     
    
    



