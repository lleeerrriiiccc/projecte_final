from pytube import YouTube
import os


# Function to download YouTube video
def download_video(url, output_path, video_name):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Select the highest resolution stream
        stream = yt.streams.get_highest_resolution()

        # Set the output file path
        output_file = os.path.join(output_path, video_name)

        # Download the video
        stream.download(output_path=output_path, filename=video_name)
        print("Video downloaded successfully!")
    except Exception as e:
        print("Error:", str(e))

# Example usage
video_url = str(input("Enter the YouTube video URL: "))
output_folder = "videos/"
video_name = str(input("Enter the video name: "))
video_name1 = video_name + ".mp4"
download_video(video_url, output_folder, video_name1)

