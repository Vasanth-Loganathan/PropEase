import mysql.connector
import openpyxl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

conn = mysql.connector.connect(host='yourhost', user='username', passwd='yourpassword', database='real_estate_management')
cur = conn.cursor()
cur.execute("""
    CREATE TABLE estate02(
        property_id INT PRIMARY KEY,
        property_type VARCHAR(15),
        location VARCHAR(20),
        listing_price INT,
        rent_price INT,
        owner_name VARCHAR(30),
        owner_contact VARCHAR(15),
        status VARCHAR(15),
        listing_date VARCHAR(25),
        last_updated VARCHAR(25),
        additional_comments VARCHAR(45)
    )
""")
loc = r"your excel file path"
wb = openpyxl.load_workbook(loc)
sheet = wb.active
header = [cell.value.strip() for cell in sheet[1]] 
print("Header:", header)  
l = []
for row in sheet.iter_rows(min_row=2, values_only=True): 
    row_data = tuple(row)
    l.append(row_data)
q = '''
    INSERT INTO estate02
    (
        property_id, property_type, location, listing_price, rent_price, owner_name, 
        owner_contact, status, listing_date, last_updated, additional_comments
    ) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
'''
cur.executemany(q, l)
conn.commit()
conn.close()

def  delete():
    conn=mysql.connector.connect(host='yourhost',user='username',passwd='yourpassword',database='real_estate_management')
    cur=conn.cursor()
    property_to_delete=int(input('Enter the property ID to delete:'))
    q='delete from estate02 where property_id=%s'
    cur.execute(q,(property_to_delete,))
    print('Property Removed')
    conn.commit()
    conn.close()

def add():
    conn = mysql.connector.connect(host='yourhost',user='username',passwd='yourpassword',database='real_estate_management')
    cur = conn.cursor()
    property_id = int(input('Enter the property ID:'))
    property_type = input('Enter the property type:')
    location = input('Enter the location:')
    listing_price = int(input('Enter the Listing Price:'))
    rent_price = int(input('Enter the rent price:'))
    owner_name = input('Enter the owner name:')
    owner_contact = input('Enter the owner contact:')
    status = input('Enter the property status:')
    listing_date = input('Enter the listing date:')
    last_updated = input('Enter the Last updated date:')
    additional_comments = input('Enter the additional comments:')
    new_property = (
        property_id, property_type, location, listing_price, rent_price,
        owner_name, owner_contact, status, listing_date, last_updated,
        additional_comments
    )
    q = '''
        INSERT INTO estate02(
            property_id, property_type, location, listing_price, rent_price,
            owner_name, owner_contact, status, listing_date, last_updated,
            additional_comments
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''
    cur.execute(q, new_property)
    conn.commit()
    conn.close()
    print('Property Added')

def display():
    conn=mysql.connector.connect(host='yourhost',user='username',passwd='yourpassword',database='real_estate_management')
    cur = conn.cursor()
    q='select * from estate02'
    cur.execute(q)
    rows=cur.fetchall()
    for i in rows:
        print(i,end='\n')
    conn.commit()
    conn.close()

def search():
    conn=mysql.connector.connect(host='yourhost',user='username',passwd='yourpassword',database='real_estate_management')
    cur = conn.cursor()
    property_id=int(input('Enter the property Id:'))
    query='SELECT * FROM estate02  WHERE property_id = %s'
    cur.execute(query, (property_id,))
    rows = cur.fetchall()
    if not rows:
        print("No property found with property ID:", property_id)
    else:
        for row in rows:
            print("Property details:")
            print("Property ID:", row[0])
            print("Property Type:", row[1])
            print("Location:", row[2])
            print("Listing Price:", row[3])
            print("Rent Price:", row[4])
            print("Owner Name:", row[5])
            print("Owner Contact:", row[6])
            print("Status:", row[7])
            print("Listing Date:", row[8])
            print("Last Updated:", row[9])
            print("Additional Comments:", row[10])
    cur.close()
    conn.close()

def grouping():
    conn = mysql.connector.connect(host='yourhost',user='username',passwd='yourpassword',database='real_estate_management')        
    cur = conn.cursor()
    max_rent_price = int(input("Enter the maximum rent price: "))
    group_by = input("Group by Property Type (P) or Location (L): ").strip().upper()
    if group_by not in ['P', 'L']:
        print("Invalid choice. Please enter 'P' for Property Type or 'L' for Location.")
        return
    if group_by == 'P':
        property_type = input("Enter the property type: ").strip()
        query = 'SELECT * FROM demo001 WHERE rent_price <= %s AND property_type = %s'
        params = (max_rent_price, property_type)
    else:
        location = input("Enter the location: ").strip()
        query = 'SELECT * FROM demo001 WHERE rent_price <= %s AND location = %s'
        params = (max_rent_price, location)
    cur.execute(query, params)
    rows = cur.fetchall()
    if not rows:
        print(f"No properties found with rent price <= {max_rent_price}.")
    else:
        print(f"Properties with Rent Price <= {max_rent_price}:")
        for row in rows:
            print(f"Property ID: {row[0]}, Property Type: {row[1]}, Location: {row[2]}, Rent Price: {row[4]}, Owner Name: {row[5]}, Status: {row[7]}, Listing Date: {row[8]}")
        cur.close()
        conn.close()

def visualize_rent_price():
    conn = mysql.connector.connect(host='yourhost',user='username',passwd='yourpassword',database='real_estate_management')
    cur = conn.cursor()
    query = "SELECT rent_price FROM estate02"
    cur.execute(query)
    rows = cur.fetchall()
    rent_prices = [row[0] for row in rows]
    cur.close()
    conn.close()
    plt.figure(figsize=(10, 6))
    x_indices = range(1, len(rent_prices) + 1)
    plt.bar(x_indices, rent_prices, align='center', alpha=0.8)
    plt.xlabel('Properties')
    plt.ylabel('Rent Price')
    plt.title('Rent Prices of Properties')
    plt.xticks(x_indices)  
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def rent_price_statistics():
    conn=mysql.connector.connect(host='yourhost',user='username',passwd='yourpassword',database='real_estate_management')
    cur=conn.cursor() 
    query = "SELECT rent_price FROM estate02"
    cur.execute(query)

    rows = cur.fetchall()
    rent_prices = [row[0] for row in rows]
    cur.close()
    conn.close()
    rent_prices_array = np.array(rent_prices)
    mean_rent_price = np.mean(rent_prices_array)
    median_rent_price = np.median(rent_prices_array)
    mode_rent_price = float(pd.Series(rent_prices).mode()[0])
    std_dev_rent_price = np.std(rent_prices_array)
    max_rent_price = np.max(rent_prices_array)
    min_rent_price = np.min(rent_prices_array)
    print("\nRent Price Statistics (from NumPy and Pandas):")
    print(f"Mean Rent Price: {mean_rent_price}")
    print(f"Median Rent Price: {median_rent_price}")
    print(f"Mode Rent Price: {mode_rent_price}")
    print(f"Standard Deviation of Rent Price: {std_dev_rent_price}")
    print(f"Maximum Rent Price: {max_rent_price}")
    print(f"Minimum Rent Price: {min_rent_price}")
while True:
        print("\n**** Real Estate Management System ****")
        print("1. Add a new property")
        print("2. Delete a property")
        print("3. Display all properties")
        print("4. Search for a property by ID")
        print("5. Group properties based on criteria")
        print("6. Visualize rent price distribution")
        print("7. Calculate rent price statistics")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == '1':
            add()
        elif choice == '2':
            delete()
        elif choice == '3':
            display()
        elif choice == '4':
            search()
        elif choice == '5':
            grouping()
        elif choice == '6':
            visualize_rent_price()
        elif choice == '7':
            rent_price_statistics()
        elif choice == '8':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")
