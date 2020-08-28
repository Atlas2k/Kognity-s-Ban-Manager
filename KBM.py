import sqlite3


def addBanNonIssued():
    data = sqlite3.connect('theExcommunicated.db')
    repNo = 0
    basket = {'Steam ID': 0, 'Staff Member': 0, 'Offender': 0,
              'Offence': 0, 'Server': 0, 'Punishment': 0,
              'Date': 0, 'Notes': 0}
    cursor = data.cursor()
    cursor.execute("""SELECT * FROM "Non Issued" """)
    allRows = cursor.fetchall()
    for n in allRows:
        temp = n[8]
        if temp > repNo:
            repNo = temp
    cursor.execute("""SELECT * FROM "Issued" """)
    allRows = cursor.fetchall()
    for n in allRows:
        temp = n[8]
        if temp > repNo:
            repNo = temp
    repNo += 1
    for key in basket:
        basket[key] = input('Please enter the %s: ' % key)
    data.execute("""INSERT INTO "Non Issued" VALUES ('%s', '%s', '%s', '%s',\
                '%s', '%s', '%s', '%s', '%s')"""
                 % (basket['Steam ID'], basket['Staff Member'],
                    basket['Offender'], basket['Offence'],
                    basket['Server'], basket['Punishment'],
                    basket['Date'], basket['Notes'], repNo))
    data.commit()
    data.close()


def addBanIssued():
    data = sqlite3.connect('theExcommunicated.db')
    basket = {'Steam ID': 0, 'Staff Member': 0, 'Offender': 0,
              'Offence': 0, 'Server': 0, 'Punishment': 0,
              'Date': 0, 'Notes': 0, 'Report No.': 0}
    for key in basket:
        basket[key] = input('Please enter the %s: ' % key)
    data.execute("""INSERT INTO "Issued" VALUES ('%s', '%s', '%s', '%s',\
                '%s', '%s', '%s', '%s', '%s')"""
                 % (basket['Steam ID'], basket['Staff Member'],
                    basket['Offender'], basket['Offence'],
                    basket['Server'], basket['Punishment'],
                    basket['Date'], basket['Notes'], basket['Report No.']))
    data.commit()
    data.close()


def editNonIssued():
    data = sqlite3.connect('theExcommunicated.db')
    basket = {'Report No.': 0, 'Column': 0, 'Edit': 0}
    for key in basket:
        basket[key] = input('Please enter the %s: ' % key)
    basket['Report No.'] = int(basket['Report No.'])
    data.execute("""UPDATE "Non Issued" SET "%s"= '%s' WHERE "Report No." = '%i'"""
                 % (basket['Column'], basket['Edit'], basket['Report No.']))
    data.commit()
    data.close()


def editIssued():
    data = sqlite3.connect('theExcommunicated.db')
    basket = {'Report No.': 0, 'Column': 0, 'Edit': 0}
    for key in basket:
        basket[key] = input('Please enter the %s: ' % key)
    basket['Report No.'] = int(basket['Report No.'])
    data.execute("""UPDATE Issued SET "%s"= '%s' WHERE "Report No." = '%i'"""
                 % (basket['Column'], basket['Edit'], basket['Report No.']))
    data.commit()
    data.close()


def viewNonIssued():
    data = sqlite3.connect('theExcommunicated.db')
    cursor = data.cursor()
    identifier = input('Please enter the Steam ID: ')
    cursor.execute("""SELECT * from "Non Issued" WHERE "Steam ID" = '%s'"""
                   % identifier)
    selection = cursor.fetchall()
    for row in selection:
        print('Report No.:', row[8])
        print('Steam ID:', row[0])
        print('Staff Member:', row[1])
        print('Offender:', row[2])
        print('Offence:', row[3])
        print('Server:', row[4])
        print('Punishment:', row[5])
        print('Date:', row[6])
        print('Notes:', row[7])
    data.commit()
    data.close()


def viewIssued():
    data = sqlite3.connect('theExcommunicated.db')
    cursor = data.cursor()
    identifier = input('Please enter the Steam ID: ')
    cursor.execute("""SELECT * from "Issued" WHERE "Steam ID" = '%s'"""
                   % identifier)
    selection = cursor.fetchall()
    for row in selection:
        print('Report No.:', row[8])
        print('Steam ID:', row[0])
        print('Staff Member:', row[1])
        print('Offender:', row[2])
        print('Offence:', row[3])
        print('Server:', row[4])
        print('Punishment:', row[5])
        print('Date:', row[6])
        print('Notes:', row[7])
    data.commit()
    data.close()


def removeNonIssued():
    data = sqlite3.connect('theExcommunicated.db')
    identifier = int(input('Please enter the Report No.: '))
    data.execute("""DELETE FROM "Non Issued" WHERE "Report No."='%i'"""
                 % identifier)
    print('Entries with Report No.: %i have been deleted.' % identifier)
    data.commit()
    data.close()


def removeIssued():
    data = sqlite3.connect('theExcommunicated.db')
    identifier = int(input('Please enter the Report No.: '))
    data.execute("""DELETE FROM "Issued" WHERE "Report No."='%i'"""
                 % identifier)
    print('Entries with Report No.: %i have been deleted.' % identifier)
    data.commit()
    data.close()
