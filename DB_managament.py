import sqlite3 as lite 


#    functionality of db
class DatabaseManage(object):

    def __init__(self):
        global   con
        try:
            con=lite.connect("course.db")
            with con:
                cur=con.cursor()
                cur.execute('CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCREMENT,Name TEXT,description TEXT,price TEXT,is_private Boolean NOT NULL Default 1)')
        except  Exception:
            print("unable to create a database")
    # create a data
    def insertion_data(self,data):
        try:
            with con:
                cur=con.cursor()
                cur.execute("INSERT INTO course(name,description,price,is_private) VALUES(?,?,?,?)",data)
                return True
        except  Exception:
            return False
    # retrieve the data from table
    def fetch_data(self):
        try:
            with con:
                cur=con.cursor()
                cur.execute("SELECT * FROM course")
                return cur.fetchall()
        except  Exception:
            return False
    # delete th data using the primary key like a ID
    def delete_data(self,id):
        try:
            with con:
                cur=con.cursor()
                cur.execute("DELETE FROM course where id=?",id)
                return True
        except  Exception:
            return False


# interference for the user
def main():
    print("*"*40)
    print("\n::COURSE MANAGEMENT :: \n")
    print("*"*40)
    print("\n")


    db=DatabaseManage()

    print("*"*40)
    print("\n::User Manual:: \n")
    print("*"*40)
    
    print("\n press 1 Insertion")
    print("press 2, Show all course")
    print("press 3 Delete Course ")
    print("*"*40)
    print("\n")

    choice=input("Enter a choice")
    if choice=='1':
        name = input('\n Enter The Name of the Course : ')
        description=input('\n Enter the description of the Course :')
        price=input("\n Enter the price of the Course")
        private=input("\n Enter the private status (1/0 )")
        if(db.insertion_data([name, description, price,private])):
            print("\n Data inserted successfully!")
        else:
            print("\n Data not inserted successfully!")
    elif choice=='2':
        print("\n course of list")

        for index,item in enumerate(db.fetch_data()):
            print("\n  ID : ", str(item[0]))
            print('Name : ', str(item[1]))
            print('description '+str(item[2]))
            print('price:'+str(item[3]))
            private="YES" if item[4] else "NO"
            print("private" + private)
            print("\n")
    elif choice == "3":
        id=input("Enter a  iD for Deletion")

        if(db.delete_data(id)):
            print("Deleted")
        else:
            print("Failed to delete")
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()






        

            







           
           




