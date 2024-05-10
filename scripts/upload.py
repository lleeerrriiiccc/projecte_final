from googleapiclient.http import MediaFileUpload
from  Google import Create_Service

def upload_file(name):
    CLIENT_SECRET_FILE = "C:/Users/el160/Documents/GitHub/projecte_final/scripts/credentials/creds.json"
    API_NAME = "drive"
    API_VERSION = "v3"
    SCOPES = ["https://www.googleapis.com/auth/drive"]

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    folder_id = "12kretDoyNNJ6nih-H3JnzUHmvJ75R-Jn"
    file_names = [f"{name}.mp4"]
    mime_types = ["video/mp4"]

    for file_name, mime_type in zip(file_names, mime_types):
        file_metadata = {
            "name" : file_name,
            "parents" : [folder_id]
        }

        media = MediaFileUpload("videos/{0}".format(file_name), mimetype=mime_type)

        service.files().create(
            body=file_metadata,
            media_body = media,
            fields = "id"
        ).execute()
    return True
