print("Chai Aur Code")
print("Youtube Manager project for Learning SqlLite3")
#-------------------------------------------------------------------------------------#
import sqlite3
conn=sqlite3.connect('youtube.db')

cursor=conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT  NOT NULL,
               time TEXT NOT NULL
    )                     
''')
def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)
def add_videos(name,time):
    cursor.execute("INSERT INTO videos(name,time) VALUES(?,?)",(name,time))
    conn.commit()
def update_videos(video_id,new_name,new_time):
    cursor.execute("UPDATE videos SET name=?,time=? WHERE id=?",(new_name,new_time,video_id))
    conn.commit()
def delete_videos(video_id):
     cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
     conn.commit()
def main():
    while True:
        print("\n YouTube manager with DB")
        print("1.List videos")
        print("2.Add videos")
        print("3.Update videos")
        print("4.Delete videos")
        print("5.Exit")
        choice=input("Enter your choice: ")

        match choice:
            case '1':
                list_videos()

            case '2':
                name=input("Enter the video Name: ")
                time=input("Enter the video Time: ")
                add_videos(name,time)
                
            case '3':
                video_id=input("Enter the video ID: ")
                name=input("Enter the video Name: ")
                time=input("Enter the video Time: ")
                update_videos(video_id,name,time)
                
            case '4':
                video_id=input("Enter the video ID to Delete: ")
                delete_videos(video_id)
                
            case '5':
                break
            case _:
                print("Invalid Input")

    conn.close()
if __name__=="__main__":
    main()