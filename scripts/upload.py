import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.service_account import Credentials

def upload_video_to_drive(video_path, folder_id):
    # Load the credentials from the credentials.json file
    credentials = Credentials.from_service_account_file('credentials/credentials.json')

    # Set up the Drive API client with the loaded credentials
    drive_service = build('drive', 'v3', credentials=credentials)

    # Create a media file upload object
    media = MediaFileUpload(video_path, mimetype='video/mp4')

    # Set the metadata for the file
    file_metadata = {
        'name': os.path.basename(video_path),
        'parents': [folder_id]
    }

    # Upload the file to the Drive folder
    file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    print(f"Video uploaded successfully. File ID: {file.get('id')}")

# Specify the path to the video file and the ID of the Drive folder
video_path = '/path/to/video.mp4'
folder_id = 'your_folder_id'

# Call the function to upload the video
upload_video_to_drive(video_path, folder_id)
