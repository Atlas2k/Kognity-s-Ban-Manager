import sqlite3


def addBanNonIssued():
    data = sqlite3.connect('theExcommunicated.db')
    basket = {'Steam ID': 0, 'Staff Member': 0, 'Offender': 0,
              'Offence': 0, 'Server': 0, 'Punishment': 0,
              'Date': 0, 'Notes': 0}
    for key in basket:
        basket[key] = input('Please enter the %s: ' % key)
    data.execute("""INSERT INTO "Non Issued" VALUES ('%s', '%s', '%s', '%s',\
                '%s', '%s', '%s', '%s')"""
                 % (basket['Steam ID'], basket['Staff Member'],
                    basket['Offender'], basket['Offence'],
                    basket['Server'], basket['Punishment'],
                    basket['Date'], basket['Notes']))
    data.commit()
    data.close()


def addBanIssued():
    data = sqlite3.connect('theExcommunicated.db')
    basket = {'Steam ID': 0, 'Staff Member': 0, 'Offender': 0,
              'Offence': 0, 'Server': 0, 'Punishment': 0,
              'Date': 0, 'Notes': 0}
    for key in basket:
        basket[key] = input('Please enter the %s: ' % key)
    data.execute("INSERT INTO issued VALUES ('%s', '%s', '%s', '%s',\
                '%s', '%s', '%s', '%s')"""
                 % (basket['Steam ID'], basket['Staff Member'],
                    basket['Offender'], basket['Offence'],
                    basket['Server'], basket['Punishment'],
                    basket['Date'], basket['Notes']))
    data.commit()
    data.close()


def editNonIssued():
    data = sqlite3.connect('theExcommunicated.db')
    basket = {'Steam ID': 0, 'Column': 0, 'Edit': 0}
    for key in basket:
        basket[key] = input('Please enter the %s: ' % key)
    data.execute("""UPDATE "Non Issued" SET "%s"= '%s' WHERE "Steam ID" = '%s'"""
                 % (basket['Column'], basket['Edit'], basket['Steam ID']))
    data.commit()
    data.close()


def editIssued():
    data = sqlite3.connect('theExcommunicated.db')
    basket = {'Steam ID': 0, 'Column': 0, 'Edit': 0}
    for key in basket:
        basket[key] = input('Please enter the %s: ' % key)
    data.execute("""UPDATE issued SET "%s"= '%s' WHERE "Steam ID" = '%s'"""
                 % (basket['Column'], basket['Edit'], basket['Steam ID']))
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
    cursor.execute("""SELECT * from issued WHERE "Steam ID" = '%s'"""
                   % identifier)
    selection = cursor.fetchall()
    for row in selection:
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
    identifier = input('Please enter the Steam ID: ')
    data.execute("""DELETE FROM "Non Issued" WHERE "Steam ID"='%s'"""
                 % identifier)
    print('Entries with Steaam ID: %s have been deleted.' % identifier)
    data.commit()
    data.close()


def removeIssued():
    data = sqlite3.connect('theExcommunicated.db')
    identifier = input('Please enter the Steam ID: ')
    data.execute("""DELETE FROM "Issued" WHERE "Steam ID"='%s'"""
                 % identifier)
    print('Entries with Steaam ID: %s have been deleted.' % identifier)
    data.commit()
    data.close()
