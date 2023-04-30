import csv

def readFrom(db, username='', fetch='', alwaysReturnList=False):
    #fetch values
    fetchValue = 0
    fetch = fetch.lower()
    results = []
    if fetch == "admin":
        fetchValue = 1
    elif fetch == "password":
        fetchValue = 1
    elif fetch == "name":
        fetchValue = 2
    elif fetch == "address":
        fetchValue = 3
    elif fetch == "phone":
        fetchValue = 4
    try:
        with open(f'{db}.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if username == row[0] or username == '':
                    if fetch == '':
                        results.append(row)
                    else:
                        results.append(row[fetchValue])
    except FileNotFoundError:
        pass
    if len(results) == 1 and not alwaysReturnList:
        results = results[0]
    elif len(results) == 0 and not alwaysReturnList:
        results = None
    return results

def searchFor(db, searchTerm):
    results = []
    with open(f'{db}.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            for col in row:
                if searchTerm in col:
                    results.append(row)
                    break
    return results

def writeTo(db, rowsToAdd, mode='a'):
    for row in rowsToAdd:
        with open(f'{db}.csv', mode, newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(row)

    
