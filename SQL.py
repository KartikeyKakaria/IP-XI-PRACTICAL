# EXECUTING SQL FILES USING PYTHON
import mysql.connector

try:
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="Ip_Practical" # A DEMO DATABASE IS ALREADY CREATED , SO IT WONT GIVE ANY ERROR, MAKE SURE TO CREATE THIS DB IF IT DOESNT EXIST
    )

    mycursor = mydb.cursor();
    print("CONNECTED TO DB!")
    print("What do you want to do Today? "
    "\n 1. Create a new Database" 
    "\n 2. Create a new Table" 
    "\n 3. Create a new Record in table"
    "\n 4. Search for Records in tables"
    "\n 5. Update Records in Tables"
    "\n 6. Delete A Record in Table"
    "\n 7. Alter A Table");
    choice = int(input("Enter your choice: "))
    
    try:
        match choice:
            case 1:
                file = open('./sql/CREATE.sql');
                content = file.read();
                mycursor.execute(content);
                print("SQL QUERY EXECUTED: " + content);
                file.close();
            case 2:
                file = open('./sql/TABLE.sql');
                content = file.read();
                mycursor.execute(content);
                print("SQL QUERY EXECUTED: " + content);
                file.close();
            case 3:
                file = open('./sql/INSERT.sql');
                content = file.read();
                mycursor.execute(content);
                print("SQL QUERY EXECUTED: " + content);
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
                file.close();
            case 4:
                file = open('./sql/SEARCH.sql');
                content = file.read();
                mycursor.execute(content);
                myresult = mycursor.fetchall()
                #print all the results
                for x in myresult:
                    print(x)
                print("SQL QUERY EXECUTED: " + content);
                file.close();
            case 5:
                file = open('./sql/UPDATE.sql');
                content = file.read();
                mycursor.execute(content);
                mydb.commit()
                print(mycursor.rowcount, "record(s) affected") 
                print("SQL QUERY EXECUTED: " + content);
                file.close();
            case 6:
                file = open('./sql/DELETE.sql');
                content = file.read();
                mycursor.execute(content);
                mydb.commit()

                print(mycursor.rowcount, "record(s) affected") 
                print("SQL QUERY EXECUTED: " + content);
                file.close();
            case 7:
                file = open('./sql/ALTER.sql');
                content = file.read();
                mycursor.execute(content);
                mydb.commit();
                print("SQL QUERY EXECUTED: " + content);
                file.close();
            case _:
                print("Invalid choice!")
    
    except Exception as error:
        print("Failed to execute SQL query.");
        print(str(error))

except Exception:
    print("Failed to connect to the database.")