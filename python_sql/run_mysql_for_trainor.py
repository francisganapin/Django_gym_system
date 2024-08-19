import mysql.connector

# Establishing the connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

# Creating a cursor object to interact with the database
cursor = conn.cursor()

# Selecting the database
cursor.execute('USE memberdb')

# Creating the gym_trainor table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS gym_trainor(
        id INT AUTO_INCREMENT PRIMARY KEY,
        trainor_id VARCHAR(10),
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        specialty VARCHAR(255),
        phone_number VARCHAR(255)
    );
''')


# Inserting 5 trainers into the gym_trainor table
trainors = [
    ('T001', 'Juan', 'Dela Cruz', 'Weight Training', '09171234567'),
    ('T002', 'Maria', 'Santos', 'Yoga', '09181234567'),
    ('T003', 'Jose', 'Reyes', 'Cardio', '09191234567'),
    ('T004', 'Ana', 'Gonzalez', 'Pilates', '09201234567'),
    ('T005', 'Carlos', 'Torres', 'Boxing', '09211234567')
]

cursor.executemany('''
    INSERT INTO gym_trainor (trainor_id, first_name, last_name, specialty, phone_number)
    VALUES (%s, %s, %s, %s, %s)
''', trainors)

# Committing the transaction
conn.commit()

# Closing the connection
conn.close()
