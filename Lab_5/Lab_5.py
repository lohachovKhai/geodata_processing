import sqlite3 as sl

import datetime

con = sl.connect('db/orders.db')
cur = con.cursor()
def printFormatter(records, header):
    dictMaxRow = dict()
    for i in range(len(records)):
        for j in range(len(header)):
            value = str(records[i][j])
            if j not in dictMaxRow:
                dictMaxRow[j] = max(len(value) + 1, len(header[j]) + 1)
            else:
                dictMaxRow[j] = max(dictMaxRow[j], len(value) + 1)
    autoForm = ""
    for i in dictMaxRow.keys():
        if autoForm != "":
            autoForm = autoForm + "| "
        autoForm = autoForm + "{0[" + str(i) + "]:<" + str(dictMaxRow[i]) + "}"
    print(autoForm.format(header))
    for i in records:
        print(autoForm.format(i))
    print('')

def createDB():
    with con:
        # Create Clients table
        con.execute("""
        CREATE TABLE IF NOT EXISTS Clients (
           client_id INTEGER PRIMARY KEY AUTOINCREMENT,
           client_name TEXT NOT NULL UNIQUE,
           sex TEXT NOT NULL ,
           contact_phone TEXT NOT NULL UNIQUE
           ); """)

        # Create Equipment table
        con.execute("""
               CREATE TABLE IF NOT EXISTS Equipment (
                  item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                  item_type TEXT NOT NULL,
                  item_price INTEGER NOT NULL,
                  status TEXT NOT NULL
                  ); """)

        # Create RentalInfo table
        con.execute("""
               CREATE TABLE IF NOT EXISTS RentalInfo (
                  rental_id INTEGER PRIMARY KEY AUTOINCREMENT,
                  client_id INTEGER,
                  item_id INTEGER,
                  assigned_worker_id INTEGER,
                  start_date DATE,
                  expiration_date DATE,
                  total_price INTEGER,
                  status TEXT NOT NULL,
                  FOREIGN KEY (client_id) REFERENCES Clients(client_id),
                  FOREIGN KEY (item_id) REFERENCES Equipment(item_id),
                  FOREIGN KEY (assigned_worker_id) REFERENCES Staff(worker_id)
                  ); """)

        # Create Staff table
        con.execute("""
        CREATE TABLE IF NOT EXISTS Staff (
           worker_id INTEGER PRIMARY KEY AUTOINCREMENT,
           worker_name TEXT NOT NULL,
           department TEXT ,
           job_title TEXT 
           ); """)


def setData():
    clients = [
        ('Jermaine Zemlak', 'female', '+38(054)2440514 '),
        ('Elmo Gorczany', 'male', '+38(085)3675405 '),
        ('Edna Boyer', 'female', '+38(044)9572727 '),
        ('Jasper Prosacco', 'male', '+38(087)2117873 '),
        ('Olga Emard', 'female', '+38(083)2895195 '),
        ('Evans Hintz', 'male', '+38(099)5634691'),
        ('Darien Mills', 'male', '+38(083)2028072 '),
        ('Shanon Goldner', 'female', '+38(055)5233631 '),
        ('Mona Kulas', 'female', '+38(089)0541127 '),
        ('Viola Spencer', 'female', '+38(075)9703008 '),
        ('Otto Watsica Jr.', 'male', '+38(059)0016417 '),
        ('Humberto Heidenreich', 'male', '+38(086)9559338 '),
        ('Carroll Wisozk', 'male', '+38(099)1704527 '),
        ('Santiago Morar', 'male', '+38(082)4120540 '),
        ('Gunner Renner', 'female', '+38(093)6751003 ')
    ]

    staf = [
        ('Jasper Maxwell', 'A', 'L1'),
        ('Anton Schaefer', 'B', 'L3'),
        ('Samia Powers', 'A', 'L5'),
        ('Macauley Park', 'C', 'L2'),
        ('Celine Zimmerman', 'C', 'L3'),
        ('Alec Farmer', 'A', 'L2'),
        ('Freddie Nelson', 'B', 'L1'),
        ('Larissa Suarez', 'A', 'L1'),
        ('Isobella Santos', 'C', 'L3'),
        ('Austin Reyes', 'B', 'L4'),
        ('Ronan Wilkinson', 'B', 'L4'),
        ('Leah Berger', 'B', 'L2'),
        ('Olly Finley', 'B', 'L3'),
        ('Diane Sloan', 'C', 'L2'),
        ('Eden Stokes', 'A', 'L4'),
    ]

    equipment = [
        ('SKI: K2 Disruption 78C', 30, 'available'),
        ('SNOW TUBE: ARCV22', 25, 'reserved'),
        ('SKI: Nordica Dobermann Spitfire 76 Pro', 50, 'available'),
        ('SNOWBOARD: GNU RC C3', 32, 'reserved'),
        ('SKI: Nordica Enforcer 80', 41, 'available'),
        ('SKI: Nordica Belle 73', 38, 'reserved'),
        ('HELMET: GIRO ARIA SPHERICAL MAT WHT', 10, 'reserved'),
        ('GLOVES: VOLCOM TARO GORE-TEX MITT', 8, 'reserved'),
        ('HELMET: GIRO JACKSON MIPS MAT BLK', 11, 'available'),
        ('SKI: Elan Ripstick 86 T', 45, 'available'),
        ('SNOWBOARD: LIB TECH TRAVIS RICE PRO C2', 55, 'available'),
        ('SNOWBOARD: GNU RIDERS CHOICE C2X', 45, 'available'),
        ('SNOWBOARD: SKUNK APE HP', 42, 'available'),
        ('SNOWBOARD: T-RICE CLIMAX C2X', 40, 'available'),
        ('GLOVES: THIRTYTWO TM MITT', 7, 'available')
    ]

    cur.executemany("INSERT INTO Clients VALUES(null, ?, ?, ?);", clients)
    cur.executemany("INSERT INTO Equipment VALUES(null, ?, ?, ?);", equipment)
    con.commit()

    def totalPriceCounter(item_id, start_date, expiration_date):
        start = start_date.split('-')
        expiration = expiration_date.split('-')
        duration = (datetime.date(int(expiration[0]), int(expiration[1]), int(expiration[2])) - datetime.date(
            int(start[0]), int(start[1]), int(start[2])))

        cur.execute(
            f"SELECT  Equipment.item_price FROM Equipment where Equipment.item_id = {item_id} ;")

        return cur.fetchone()[0] * int(duration.days)



    rentalInfos =[
        [13, 2, 12, '2023-02-02', '2023-02-15', 'ACTIVE'],
        [10, 9, 2, '2023-01-03', '2023-01-06', 'CANCELED'],
        [3, 3, 15, '2023-02-08', '2023-02-15', 'ACTIVE'],
        [8, 6, 1, '2023-01-08', '2023-02-22', 'ACTIVE'],
        [1, 7, 12, '2023-02-07', '2023-02-12', 'ACTIVE'],
        [12, 4, 2, '2023-02-06', '2023-05-08', 'CANCELED'],
        [5, 2, 15, '2023-02-08', '2023-02-15', 'ACTIVE'],
        [3, 11, 1, '2023-02-08', '2023-02-14', 'ACTIVE'],
        [14, 14, 12, '2023-02-07', '2023-02-13', 'ACTIVE'],
        [9, 1, 2, '2022-12-31', '2023-01-07', 'CANCELED'],
        [3, 7, 15, '2023-01-29', '2023-02-19', 'ACTIVE'],
        [15, 13, 1, '2023-02-08', '2023-02-22', 'ACTIVE'],
        [10, 14, 12, '2023-02-07', '2023-02-22', 'ACTIVE'],
        [12, 6, 2, '2023-01-08', '2023-02-12', 'CANCELED'],
        [4, 14, 15, '2023-02-08', '2023-02-15', 'ACTIVE'],
    ]

    for i in range(len(rentalInfos)):
         rentalInfos[i].insert(5, (totalPriceCounter(rentalInfos[i][1], rentalInfos[i][3], rentalInfos[i][4])))

    cur.executemany("INSERT INTO RentalInfo VALUES(null, ?, ?, ?, ?, ?, ?, ?);", rentalInfos)
    cur.executemany("INSERT INTO Staff VALUES(null, ?, ?, ?);", staf)
    con.commit()

# NOTE: Should be executed once
# createDB()

# NOTE: Should be executed once
# setData()


# Stages


# 1.	Отримаємо перелік обладнання, вартість оренди на добу котрого, становить більше 40 грошових єдиниць.

cur.execute(
        """ SELECT Equipment.item_id, Equipment.item_type, Equipment.item_price FROM Equipment
            WHERE Equipment.item_price >=40;""")

printFormatter(cur.fetchall(), ("Item Id", "Item type", "Item price"))


# 2.	Виконаємо операцію UPDATE для користувача Mona Kulas, змінивши йому номер телефону.

cur.execute(
        """ SELECT client_id, client_name, contact_phone FROM Clients
            WHERE client_name == "Mona Kulas";""")

print("BEFORE UPDATE EXECUTION")
printFormatter(cur.fetchall(), ("Id", "Client Name", "Contact Phone"))

cur.execute(
        """ UPDATE Clients SET contact_phone = "+38(099)7777777"
            WHERE client_name == 'Mona Kulas';""")

print("AFTER UPDATE EXECUTION")


cur.execute(
        """ SELECT client_id, client_name, contact_phone FROM Clients
            WHERE client_name == "Mona Kulas";""")

printFormatter(cur.fetchall(), ("Id", "Client Name", "Contact Phone"))



# 3.	Виконаємо операцію DELETE для таблиці зі співробітниками.

cur.execute(
        """ SELECT * FROM Staff ;""")
# NOTE: Should be executed once

# cur.execute(
#         """ INSERT INTO Staff (worker_name, department, job_title)
#             VALUES ('Jackson Astraia', 'Temporary', 'TMP')
#         ;""")

cur.execute(
        """ DELETE FROM Staff WHERE worker_name = "Jackson Astraia"
        ;""")

cur.execute(
        """ SELECT * FROM Staff ;""")


printFormatter(cur.fetchall(), ("Id", "Worcker Name", "Department", "Job Title"))



# 4.	Запит на детальне відображення інформації щодо орендованого обладнання

cur.execute("""
                SELECT RentalInfo.rental_id, Clients.client_name, Clients.contact_phone, Equipment.item_type, 
                RentalInfo.status, RentalInfo.start_date, RentalInfo.expiration_date, Staff.worker_name 
                FROM RentalInfo 
                INNER JOIN Equipment ON Equipment.item_id = RentalInfo.item_id
                LEFT JOIN Clients ON Clients.client_id = RentalInfo.client_id
                RIGHT JOIN Staff ON Staff.worker_id = RentalInfo.assigned_worker_id 
                ;""")

printFormatter(cur.fetchall(), ("Id", "Client Name", "Phone number", "Item Type", "Status", "Start",
                                "Expiration", "Assigned staff"))



# 5.	Запит по користувачах у кого завтра спливає строк оренди

cur.execute("""
                SELECT Clients.client_name,Clients.contact_phone, Equipment.item_type, RentalInfo.status,
                RentalInfo.start_date, RentalInfo.expiration_date, Staff.worker_name 
                FROM RentalInfo 
                INNER JOIN Equipment ON Equipment.item_id = RentalInfo.rental_id
                LEFT JOIN Clients ON Clients.client_id = RentalInfo.rental_id
                RIGHT JOIN Staff ON Staff.worker_id = RentalInfo.rental_id
                WHERE 
                        julianday(RentalInfo.expiration_date) - julianday('now') ==
                               ( SELECT MIN(res) FROM (
                                    SELECT julianday(RentalInfo.expiration_date) - julianday('now') as res
                                            FROM RentalInfo
                                                WHERE res > 0))     
                        AND   RentalInfo.status like "ACTIVE"        
                ;""")

printFormatter(cur.fetchall(), ("Client Name", "Phone Number", "Item Type", "Status", "Start Date", "Expiration", "Assigned staff"))



# 6 Запит на пошук найпопулярнішого товару (тобто товару, який найчастіше здавався в оренду)
cur.execute("""
                SELECT Equipment.item_type, COUNT(RentalInfo.item_id) AS count
                FROM RentalInfo
                JOIN Equipment ON Equipment.item_id = RentalInfo.item_id
                GROUP BY RentalInfo.item_id
                ORDER BY count DESC
                LIMIT 1
                ;""")

printFormatter(cur.fetchall(), ("Item Type", "Times"))
