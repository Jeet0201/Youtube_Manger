import json

def load_data(): 
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_video(videos):
    if not videos:
        print("No videos found.")
    else:
        for index, video in enumerate(videos, start=1):
            print(f"{index}.{video['name']},Duration:{video['time']}")

def add_video(videos):
    name = input("Enter the video name: ")
    time = input("Enter the video time: ")
    videos.append({'name': name, 'time': time})
    save_data(videos)
    print("Video added successfully!")

def update_video(videos):
    list_all_video(videos)
    index=int(input("Enter the index of the video to update: ")) 
    if 1<= index <= len(videos):
        name=input("Enter the video name: ")
        time = input("Enter the video time: ")
        videos[index-1] ={'name':name,'time':time}
        save_data(videos)
    else:
        print("Invalid index. Please try again.")
        
    
def delete_video(videos):
   list_all_video(videos)
   index = int(input("Enter the index of the video to delete: "))
   
   if 1<= index <= len(videos):
       del videos[index-1]
       save_data(videos)
   else:
       print("Invalid index. Please try again.")
    

def main():
    videos = load_data()
    while True:
        print("\n🎬 Youtube Manager | Choose an Option")
        print("1. List All Youtube Videos")
        print("2. Add a Youtube Video")
        print("3. Update a Youtube Video")
        print("4. Delete a Youtube Video")
        print("5. Exit the App")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_video(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print("Goodbye!")
                break
            case _:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
