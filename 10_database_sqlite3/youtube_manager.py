import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    time TEXT NOT NULL
               )
''')

def list_all_videos():
    cursor.execute('SELECT * FROM videos')
    try:
        table = cursor.fetchall()
        if table:
            print("VID_ID || NAME || TIME")
            for row in table:
                print(f'{row[0]} || {row[1]} || {row[2]}')
    except:
        print("Database is empty")

def add_video(name, time):
    cursor.execute('INSERT INTO videos (name, time) VALUES (?,?)',(name, time))
    conn.commit()

def delete_video(vid_id):
    cursor.execute('DELETE FROM videos WHERE id = ?', (vid_id,))
    conn.commit()

def update_video(vid_id):
    choice = input("Do you want to update name?(Y/N)")
    if choice.strip().lower() == 'y':
        name = input("Enter name : ")
        cursor.execute('UPDATE videos SET name = ? WHERE id = ?', (name, vid_id))
    if choice.strip().lower() not in ['y','n']:
        print("Invalid response")
    choice = input("Do you want to update time?(Y/N)")
    if choice.strip().lower() == 'y':
        time = input("Enter time : ")
        cursor.execute('UPDATE videos SET time = ? WHERE id = ?', (time, vid_id))
    if choice.strip().lower() not in ['y','n']:
        print("Invalid response")
    conn.commit()

def main():
    while True:
        print("\n Youtube Manager App with DB")
        print("1. List all videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            list_all_videos()
        elif choice == 2:
            name = input("Enter name of the video : ").strip()
            time = input("Enter time of the video : ").strip()
            add_video(name, time)
        elif choice == 3:
            list_all_videos()
            vid_id = int(input("Enter video id : ").strip())
            update_video(vid_id)
        elif choice == 4:
            list_all_videos()
            vid_id = int(input("Enter video id : ").strip())
            delete_video(vid_id)
        elif choice == 5:
            break
        else:
            print("Invalid choice")
    conn.close()


if __name__ == "__main__":
    main()