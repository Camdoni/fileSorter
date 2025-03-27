from pathlib import Path

doc_extensions = {'.pdf', '.doc', '.docx'}
image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.jfif', '.heic'}
video_extensions = {'.mp4', '.mov', '.avi', '.mkv', '.flv'}

def file_sort(file_path):
    # create folders
    docs_folder = file_path / 'Documents'
    images_folder = file_path / 'Images'
    videos_folder = file_path / 'Videos'

    if file_path.exists() and file_path.is_dir:
        for file in file_path.iterdir():
            if file.suffix.lower() in doc_extensions:
                docs_folder.mkdir(exist_ok=True)
                file.rename(docs_folder / file.name)

            elif file.suffix.lower() in image_extensions:
                images_folder.mkdir(exist_ok=True)
                file.rename(images_folder / file.name)

            elif file.suffix.lower() in video_extensions:
                videos_folder.mkdir(exist_ok=True)
                file.rename(videos_folder / file.name)
    else:
        print("Not valid directory")

# get file path from user
file_path = input(r"Enter the absolute file path of the folder you want to sort: ").strip().strip('"')

file_path = Path(file_path)

file_sort(file_path)

for file in file_path.rglob("*"):
    print(file)


