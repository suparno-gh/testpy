import json

PATH = "youtube.txt"

def load_data(path=PATH):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []

def save_data(videos, path=PATH):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(videos, f)

def list_all_videos(videos):
    print("\n" + "*"*50)
    for i, vid in enumerate(videos, start=1):
        print(f"{i}. Video Name: {vid['name']}, Duration: {vid['time']}")
    print("\n" + "*"*50)

def add_video(videos):
    name = input("Enter name: ")
    time = input("Enter duration: ")
    videos.append({"name": name, "time": time})
    save_data(videos)

def update_video(videos):
    list_all_videos(videos)
    idx = int(input("Enter index to be updated: "))
    if 1 <= idx <= len(videos):
        name = input("Enter updated name: ")
        time = input("Enter updated duration: ")
        videos[idx-1] = {"name": name, "time": time}
        save_data(videos)
    else:
        print("Invalid response")

def delete_video(videos):
    list_all_videos(videos)
    idx = int(input("Enter index to be deleted: "))
    if 1 <= idx <= len(videos):
        del videos[idx-1]
        save_data(videos)
    else:
        print("Invalid response")

def main():
    videos = load_data()
    while True:
        print("\nYoutube Manager | Choose an option")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ").strip()
        match choice:
            case '1': list_all_videos(videos)
            case '2': add_video(videos)
            case '3': update_video(videos)
            case '4': delete_video(videos)
            case '5': break
            case _: print("Invalid Choice")

if __name__ == "__main__":
    main()
