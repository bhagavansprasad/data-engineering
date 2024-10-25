import requests
import os

def download_files(url):
    response = requests.get(url)
    if response.status_code == 200:
        folder_name = "downloaded_files"  # Fixed folder name typo
        os.makedirs(folder_name, exist_ok=True)
        print(f"Folder '{folder_name}' is created or already exists.")
        
        url_part = url.split("/")[-1].split("?")[0]
        file_name = f"{url_part}.pdf"
        file_path = os.path.join(folder_name, file_name)

        if os.path.exists(file_path):
            print(f"'{file_name}' already exists in the folder")
        else:
            with open(file_path, "wb") as file:  
                file.write(response.content)  
            print(f"PDF '{file_name}' downloaded successfully!")
    else:
        print(f"Failed to download from {url}, status code: {response.status_code}")
    print("test_line")
