import json

DATA_FILE = r'youtube.txt'

def load_data():
    try:
        with open(DATA_FILE,'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open(DATA_FILE,'w') as file:
        json.dump(videos, file)


def list_all_videos(videos):
    print("\n")
    print("*" * 70, "\n")
    print("Vid_ID || Name || Time")
    for index, video in enumerate(videos, start=1):
        print(f"{index} || {video['name']} || {video['time']}")

def add_video(videos):
    name = input("Enter video name : ")
    time = input("Enter video time : ")
    videos.append({'name':name, 'time':time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    while True:
        flag = 0
        vid_id = int(input("Enter vid_id for the video to be updated : "))
        if vid_id not in range(1,len(videos) + 1):
            print("Invalid vid_id!")
            exit_status = input("Do you want to exit? (Y/N)").strip().lower()
            if exit_status == 'y':
                break
            continue
        choice1 = input("Do you want to update the name? (Y/N)").strip().lower()
        if choice1 == 'y':
            videos[vid_id - 1]['name'] = input("Enter new name : ")
            flag = 1
        elif choice1 not in ['y','n']:
            print("Invalid response")
        choice2 = input("Do you want to update the time? (Y/N)").strip().lower()
        if choice2 == 'y':
            videos[vid_id - 1]['time'] = input("Enter new time : ")
            flag = 1
        elif choice2 not in ['y','n']:
            print("Invalid response")
        if flag == 1:
            save_data_helper(videos)
            break
        else:
            exit_status = input("Do you want to exit? (Y/N)").strip().lower()
            if exit_status == 'y':
                break

        


def delete_video(videos):
    list_all_videos(videos)
    vid_id = int(input("Enter the video number to be deleted : "))
    try:
        videos.pop(vid_id - 1)
    except:
        print("Invalid vid_id")
    else:
        save_data_helper(videos)
        print("Successfully Deleted video")

def main():
    videos = load_data()

    while True:
        print("\nYoutube Manager ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = int(input("Enter your choice : "))
        # print(videos)

        if choice == 1:
            list_all_videos(videos)
        elif choice == 2:
            add_video(videos)
        elif choice == 3:
            update_video(videos)
        elif choice == 4:
            delete_video(videos)
        elif choice == 5:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()