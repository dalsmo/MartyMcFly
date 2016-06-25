import sqlite3 as lite
import datetime
import pdb

# define the data range
print("-------- Defining the processing range --------")
startYear = input("year:")
startMonth = input("month:")
startDate = datetime.date(startYear,startMonth,1)
#endDate = datetime.date.today()-datetime.timedelta(days=1)
endDate = startDate+datetime.timedelta(365/12)
diffDays = endDate-startDate
print 'calculating for %i days' % diffDays.days
print("-------- inputs defined, calculating ----------")

# get the important part from the logs databace
rows = list();
con = lite.connect('fluxCapacitor.db',detect_types=lite.PARSE_DECLTYPES)
with con:          
    cur = con.cursor()
    statement = "SELECT * FROM logs WHERE timestamp>'" + startDate.strftime('%Y-%m-%d')+ "' AND timestamp<'" + endDate.strftime('%Y-%m-%d') + "';"
    #print statement
    cur.execute(statement)
    rows = cur.fetchall()

# figure out who are the active people 
activePeople = list();
for row in rows:
    if row[1] not in activePeople:
        activePeople.append(row[1])

# create the result matrix
resMatrix = [[0 for x in range(diffDays.days)] for y in range(len(activePeople))] # resmatrix[person][day]

# now check each day
for d in range(diffDays.days):
    day = startDate + datetime.timedelta(days=d)
    nextDay = day + datetime.timedelta(days=1)

    # define a boolean matrix to hold all people and every hour that thay where there
    boolMatrix = [[False for x in range(24)] for y in range(len(activePeople))] # boolMatrix[person][hour]

    # define for every person if thay where here. (this code will not get every edge case)
    for personIndex in range(len(activePeople)):
        rows = list();
        with con:          
            cur = con.cursor()
            statement = "SELECT * FROM logs WHERE timestamp>'" + day.strftime('%Y-%m-%d')+ "' AND timestamp<'" + nextDay.strftime('%Y-%m-%d') + "' AND memberName='" + activePeople[personIndex] +"';"
            cur.execute(statement)
            rows = cur.fetchall()
        for rowIndex in range(len(rows)):
            row=rows[rowIndex]
            if row[2]=='login' and rowIndex<(len(rows)-1):
                nextRow = rows[rowIndex+1]
                if nextRow[2]=='logout': # set times to true
                    startHour = row[3].hour
                    endHour = nextRow[3].hour
                    for i in range(startHour,endHour):
                        boolMatrix[personIndex][i] = True
        # Note: this does not register loging in the day before and staying past midnight               
        # quesry for last login yesterday(fix the edge case)
            #query for logout this day (if its befor the first login or by itsef we are fine)
            # set tartign boleans as true
        # query for logout tomorow(fi edge case)


    # now define the times
        # made upp rules:
            # hela timmar som borjar varje timme
            # om det ar fler an tre, ge varje medlam en timmes count
            # fuck the edge cases
            # this gives an aproxmiate logging.
        #loop thrugh every hour and se if it gives a point for people who wherer there
        #return the hours for each person that day, put it in the reult matrix
    for hourIndex in range(24):
        hourSum = 0
        for personIndex in range(len(activePeople)):
            if boolMatrix[personIndex][hourIndex]:
                hourSum+=1
                #print 'ya'
        if hourSum>=3: # iterate that persons day counter
            for k in range(len(activePeople)):
                if boolMatrix[k][hourIndex]:
                    resMatrix[k][d]+=1
                    #print 'something'

            
# remove days when nobody was there?? (do this in output for now)
# remove pople who where not ther enaught (do this in output for now)


# now go for some form of output
#resMatrix = [[0 for x in range(diffDays.days)] for y in range(len(activePeople))] # resmatrix[person][day]
daysToPrint = [False for x in range(diffDays.days)]
for day in range(diffDays.days):
    for person in range(len(activePeople)):
        if resMatrix[person][day]>0:
            daysToPrint[day] = True           

# pritn adiquit blanks and dates
print '------------------------ output ----------------------------\n'
print '               ',# 15 blanks
for day in range(diffDays.days):
    if daysToPrint[day]:
        print str(day).ljust(3),
print ''

for personIndex in range(len(activePeople)):
    print activePeople[personIndex].ljust(15),
    for dayIndex in range(diffDays.days):
        if daysToPrint[dayIndex]:
            print str(resMatrix[personIndex][dayIndex]).ljust(3),
    print('')
            
        
# it something :-|
    

