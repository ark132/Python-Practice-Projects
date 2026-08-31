import sqlite3
import os
conn = sqlite3.connect(r"C:\Engineering softcopies.PDF\Multidisplinary\Engineering_Workspace\NPTEL_DataScience\Python Practice Projects\CLI Manager\cli.db")

cursor=conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS files(
                name TEXT NOT NULL,
                path TEXT NOT NULL,
                type TEXT NOT NULL
                )
''')

def list_Files():
    cursor.execute("SELECT * FROM files")
    rows=cursor.fetchall()
    if not rows:
        print("No Files found")
    for row in rows:
        print(row)
def create_Files(File_name):
    name=os.path.basename(File_name)
    path=os.path.abspath(File_name)
    file_type=os.path.splitext(File_name)[1]
    cursor.execute('''INSERT INTO files(name,path,type) VALUES(?,?,?)''',
                   (name,path,file_type))
    conn.commit()
def read_Files(File_name):
    name=os.path.basename(File_name)
    path=os.path.abspath(File_name)
    file_type=os.path.splitext(File_name)[1]
    cursor.execute('''SELECT * FROM files WHERE name=? AND path=? AND type=?''',
                   (name,path,file_type))
    row=cursor.fetchone()
    if row:
        print("File found: ",row)
    else:
        print("File Not found")
    conn.commit()
def update_Files(old_name,new_name):
    old_base=os.path.basename(old_name)
    old_path=os.path.abspath(old_name)
    old_type=os.path.splitext(old_name)[1]

    new_base=os.path.basename(new_name)
    new_path=os.path.abspath(new_name)
    new_type=os.path.splitext(new_name)[1]
    cursor.execute('''
           UPDATE files
           SET name= ?,path= ?,type= ?
           WHERE name= ? AND path= ? AND type=? 
''',(new_base,new_path,new_type,old_base,old_path,old_type))
    conn.commit()
def delete_Files(File_name):
    name=os.path.basename(File_name)
    path=os.path.abspath(File_name)
    cursor.execute("DELETE FROM files WHERE name= ? AND path=?",(name,path))
    conn.commit()
def main():
    while True:
        print("---Welcome To CLI MANAGER v.01---")
        print("Please Perform CRUD Operations")
        File_Name=input("Enter a File Name with Extension: ")
        choice=input('''Enter Your Choice:
                    1 for Create a File
                    2 for Read a File 
                    3 Update a File
                    4 Delete a File
                    5List File: 
                    6Exit App''')
        match choice:
            case '1':
                with open(File_Name,'w')as File:
                    File.write("Hello")
                create_Files(File_Name)
            case '2':
                try:
                    with open(File_Name,'r')as File:
                        print(File.read())
                    print("File Name:",File_Name)
                    read_Files(File_Name)
                except FileNotFoundError:
                    print("File does not exist")

            case '3':
                New_File_Name=input("Enter the New_name of file: ")
                try:
                  os.rename(File_Name,New_File_Name)
                  update_Files(File_Name,New_File_Name)
                  print("File Renamed and Database updated")
                except FileNotFoundError:
                    print("Old file does not exist")
                except OSError:
                    print("Rename Failed.Check if the new file name is valid")
            case '4':
                Name=input("Enter File Name that is to be Deleted: ")
                try:
                    os.remove(Name)
                    delete_Files(Name)
                    print("File deleted from disk and database")
                except FileNotFoundError:
                    print("File does not exist")
            case '5':
                list_Files()
            case '6':
                break
            case _:
                print("INVALID SELECTION")
if __name__=="__main__":
    main()
