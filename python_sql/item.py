import mysql.connector

def insert_item_gym():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )

    cursor = conn.cursor()

# it will use our memberdb database
    cursor.execute('USE memberdb')

    # this will create table if not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gym_item(
            id INT AUTO_INCREMENT PRIMARY KEY,
            item_name VARCHAR(255),
            stock INT,
            description VARCHAR(255),
            supplier VARCHAR(255),
            phone_number VARCHAR(255)
        );
    ''')


    try:
        item_name = input('Name of item: ')
        
        while True:
            try: 
                stock = int(input('stock Quantity: '))
                break #break if the input was integer
            except ValueError:
                print('please put valid number')

        description = input('Description: ')
        supplier =   input('Who our supplier?: ')
        
        while True:
            phone_number = input('Phone number: ')
            if phone_number.isdigit():
                break  # Break if the input is a valid number
            else:
                print('Please enter a valid phone number (digits only).')

        cursor.execute('''
            INSERT INTO gym_item (item_name, stock, description, supplier, phone_number) 
            VALUES (%s, %s, %s, %s, %s)
        ''', (item_name, stock, description, supplier, phone_number))
        
        conn.commit()
        print(f'Recorded done insert of {item_name}, {stock} ,{description} ,{supplier} ,{phone_number}')
        conn.close()

    except ValueError:
        print('error changes')

# Close the connection



insert_item_gym()