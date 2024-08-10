from instagrapi import Client
import cropfile as cp
import os

username = "your_user_name"
password = "your_password"

client = Client()
client.login(username, password)


def crop():
    #input_file = input("Enter the path to the video file: ")
    input_file = "source/test.mp4"
    num_pieces = int(input("Enter the number of pieces to split the video into: "))
    output_dir = "target"
    cp.split_video(input_file, num_pieces, output_dir)

def num_of_file():
    folder_path = "target"
    # List all files and directories in the folder
    all_files = os.listdir(folder_path)
    return sum(1 for file in all_files if os.path.isfile(os.path.join(folder_path, file)))

crop()


# Count only files
file_count = num_of_file()
print(f"number of videos: {file_count}")


for i in range(file_count):
    video_path = (f"target/output_{i+1}.mp4")
    caption = (f"demo part{i+1}")
    client.video_upload(video_path, caption)

