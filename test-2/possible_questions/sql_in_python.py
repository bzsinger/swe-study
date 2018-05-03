# select
def select(table, func):
    for row in table:
        if func(row):
            yield row

def select(table, func):
    return (row for row in table if func(row))

# project
def project(table, *cols):
    for row in table:
        yield {col: row[col] for col in cols if col in row}

def project(table, *cols):
    return ({col: row[col] for col in cols if col in row} for row in table)

# cross_join
def cross_join(table1, table2):
    for row1 in table1:
        for row2 in table2:
            yield {**row1, **row2}

def cross_join(table1, table2):
    return ({**row1, **row2} for row1 in table1 for row2 in table2)

def cross_join(table1, table2):
    return theta_join(table1, table2, lambda row1, row2: True)

# theta_join
def theta_join(table1, table2, func):
    for row1 in table1:
        for row2 in table2:
            if func(row1, row2):
                yield {**row1, **row2}

def theta_join(table1, table2, func):
    return ({**row1, **row2} for row1 in table1 for row2 in table2 if func(row1, row2))


# natural_join
def natural_join(table1, table2):
    for row1 in table1:
        for row2 in table2:
            if all([row1[col] == row2[col] for col in row1 if col in row2]):
                yield {**row1, **row2}

def natural_join(table1, table2):
    return ({**row1, **row2} for row1 in table1 for row2 in table2 if all([row1[col] == row2[col] for col in row1 if col in row2]))

def natural_join(table1, table2):
    return theta_join(table1, table2, lambda row1, row2: all([row1[col] == row2[col] for col in row1 if col in row2]))
