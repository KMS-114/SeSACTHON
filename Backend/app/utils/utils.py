import shutil

from fastapi import UploadFile
import os


async def save_upload_file(username: str, file: UploadFile, type: str):
    save_path = f"../../data/{type}/{username}"
    os.makedirs(save_path, exist_ok=True)

    file_path = os.path.join(save_path, file.filename)
    with open(file_path, "wb") as file_object:
        shutil.copyfileobj(file.file, file_object)
    return file_path


async def delete_upload_file(file_path: str):
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
            if not os.listdir(file_path):
                os.rmdir(file_path)
            return True
        else:
            print(f"File not found: {file_path}")
            return False
    except Exception as e:
        print(f"An error occured while deleting the file: {e}")
        return False
