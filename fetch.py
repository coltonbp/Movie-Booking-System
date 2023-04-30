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
    elif fetch == "titles":
        fetchValue = 0
    elif fetch == "desc":
        fetchValue = 1
    elif fetch == "times":
        fetchValue = 2
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
    try:
        with open(f'{db}.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                for col in row:
                    if searchTerm in col:
                        results.append(row)
                        break
    except FileNotFoundError:
        pass
    return results

def writeTo(db, rowsToAdd, mode='a'):
    with open(f'{db}.csv', mode, newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in rowsToAdd:
            print(row)
            writer.writerow(row)

def deleteFrom(db, idToDelete):
    contents = []
    newContents = []
    with open(f'{db}.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            contents.append(row)
    for row in contents:
        if row[0] != idToDelete:
            newContents.append(row)
    print("contents: " + str(contents))
    with open(f'{db}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in newContents:
            writer.writerow(row)
    
