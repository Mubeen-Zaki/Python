# import pymongo
from pymongo import MongoClient
from bson import ObjectId

try:
    client = MongoClient("mongodb+srv://<username>:<password>@cluster0.wpj8w6s.mongodb.net/", tlsAllowInvalidCertificates = True)
    print(client)
    db = client["ytmanager"]
    print(db)
    video_collection = db["videos"]
    print(video_collection)

except Exception as e:
    print(str(e))


def add_video(name, time):
    doc = {'title' : name, 'time' : time}
    video_collection.insert_one(doc)
    print("Video details added successfully")

def delete_video(vid_id):
    video_collection.delete_one({'_id' : vid_id})
    print("Video details DELETED!")

def update_video(vid_id):
    choice = input("Do you want to update name? (Y/N)").strip().lower()
    if choice == 'y':
        name = input("Enter name : ")
        video_collection.update_one(
            {'_id' : vid_id},
            {"$set" : {'title': name}}
        )
    choice = input("Do you want to update time? (Y/N)").strip().lower()
    if choice == 'y':
        time = input("Enter time : ")
        video_collection.update_one(
            {'_id' : vid_id},
            {"$set" : {'time': time}}
        )
    print("Details updated successfully!")

def list_videos():
    print("Video ID || Video Title || Video Time")
    for video in video_collection.find():
        print(f"{video['_id']} || {video['title']} || {video['time']}")

def main():
    while True:
        print("*" * 100)
        print("Welcome to Youtube Manager App")
        print("*" * 100)
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ") 
        choice = int(input("Enter your choice : "))
        if choice == 1:
            list_videos()
        elif choice == 2:
            name = input("Enter name : ").strip()
            time = input("Enter time : ").strip()
            add_video(name, time)
        elif choice == 3:
            list_videos()
            vid_id = ObjectId(input("Enter video id to update : "))
            update_video(vid_id)
        elif choice == 4:
            list_videos()
            vid_id = ObjectId(input("Enter video id to delete : "))
            delete_video(vid_id)
        elif choice == 5:
            break
        else:
            print("! Invalid Response. Select choice from the given options!")
        
        

if __name__ == "__main__":
    main()