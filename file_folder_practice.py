
from pathlib import Path
import shutil

# =====================================================
# STEP 1: DEFINE YOUR ROOT PATH
# =====================================================

root_path = Path(
    "/Users/geetabhimsenmaharana/Desktop/CurrentProjects/"
    "3_project_python_mini_programs/createfilefolder/"
)

# Keep all practice items inside this separate folder.
workspace = root_path / "file_folder_practice"

# Create the workspace if it does not exist.
workspace.mkdir(parents=True, exist_ok=True)

print("Workspace:", workspace)
print("Workspace exists:", workspace.exists())


# =====================================================
# STEP 2: CREATE 3 FOLDERS
# =====================================================

folder1 = workspace / "Folder_1"
folder2 = workspace / "Folder_2"
folder3 = workspace / "Folder_3"

for folder in [folder1, folder2, folder3]:
    # Create each folder.
    # exist_ok=True prevents an error if it already exists.
    folder.mkdir(exist_ok=True)
    print("Created/checked:", folder.name)


# =====================================================
# STEP 3: CREATE 3 FILES INSIDE EACH FOLDER
# =====================================================

for folder_number, folder in enumerate(
    [folder1, folder2, folder3], start=1
):
    for file_number in range(1, 4):
        file_path = folder / f"file_{file_number}.txt"

        # Create a file and write some text.
        # write_text() overwrites the contents if the file exists.
        file_path.write_text(
            f"This is file {file_number} in Folder {folder_number}.",
            encoding="utf-8"
        )

        print("Created:", file_path)


# =====================================================
# STEP 4: CHECK FILES AND FOLDERS
# =====================================================

print("\n--- CHECKING ---")

print("Folder_1 exists:", folder1.exists())

sample_file = folder1 / "file_1.txt"

print("file_1.txt exists:", sample_file.exists())
print("Is it a file?:", sample_file.is_file())
print("Is Folder_1 a folder?:", folder1.is_dir())

# List everything directly inside Folder_1.
print("Contents of Folder_1:")
for item in folder1.iterdir():
    print(" ", item.name)


# =====================================================
# STEP 5: RENAME ONE FILE IN EACH FOLDER
# =====================================================

print("\n--- RENAMING FILES ---")

folders = [folder1, folder2, folder3]

for number, folder in enumerate(folders, start=1):
    old_file = folder / "file_1.txt"
    new_file = folder / f"renamed_file_{number}.txt"

    # Check that the source exists and destination is unused.
    if old_file.exists() and not new_file.exists():
        old_file.rename(new_file)
        print(f"Renamed {old_file.name} -> {new_file.name}")
    else:
        print("Skipped rename:", old_file)


# =====================================================
# STEP 6: MOVE ONE FILE FROM EACH FOLDER TO THE NEXT
# =====================================================

print("\n--- MOVING FILES ---")

# file_2.txt moves from Folder_1 to Folder_2.
# file_3.txt moves from Folder_2 to Folder_3.
# renamed_file_3.txt moves from Folder_3 to Folder_1.

moves = [
    (folder1 / "file_2.txt", folder2 / "file_2_from_folder1.txt"),
    (folder2 / "file_3.txt", folder3 / "file_3_from_folder2.txt"),
    (
        folder3 / "renamed_file_3.txt",
        folder1 / "renamed_file_3_from_folder3.txt"
    )
]

for source, destination in moves:
    # Never rename/move if the source is missing
    # or the destination already exists.
    if source.exists() and not destination.exists():
        source.rename(destination)
        print(f"Moved {source} -> {destination}")
    else:
        print("Skipped move:", source)


# =====================================================
# STEP 7: RENAME A FOLDER
# =====================================================

print("\n--- RENAMING FOLDER ---")

renamed_folder3 = workspace / "Folder_3_Renamed"

if folder3.exists() and not renamed_folder3.exists():
    folder3.rename(renamed_folder3)
    print("Folder_3 renamed to Folder_3_Renamed")


# =====================================================
# STEP 8: MOVE A FOLDER
# =====================================================

print("\n--- MOVING FOLDER ---")

archive_folder = workspace / "Archive"

# Create the destination folder first.
archive_folder.mkdir(exist_ok=True)

# Move the renamed folder into Archive.
folder_destination = archive_folder / "Folder_3_Renamed"

if renamed_folder3.exists() and not folder_destination.exists():
    renamed_folder3.rename(folder_destination)
    print("Moved Folder_3_Renamed into Archive")


# =====================================================
# STEP 9: DELETE A FILE
# =====================================================

print("\n--- DELETING A FILE ---")

# This is a sample file created by this program.
# We delete only this specific file.
file_to_delete = folder1 / "file_3.txt"

if file_to_delete.exists() and file_to_delete.is_file():
    file_to_delete.unlink()
    print("Deleted file:", file_to_delete.name)
else:
    print("File not found:", file_to_delete)


# =====================================================
# STEP 10: DELETE AN EMPTY FOLDER
# =====================================================

print("\n--- DELETING AN EMPTY FOLDER ---")

empty_folder = workspace / "Empty_Folder"

# Create the empty folder for this demonstration.
empty_folder.mkdir(exist_ok=True)

# rmdir() deletes empty folders only.
if empty_folder.exists() and empty_folder.is_dir():
    empty_folder.rmdir()
    print("Deleted empty folder:", empty_folder.name)


# =====================================================
# STEP 11: DISPLAY THE FINAL STRUCTURE
# =====================================================

print("\n--- FINAL FILE STRUCTURE ---")

for item in sorted(workspace.rglob("*")):
    print(item.relative_to(workspace))

print("\nProgram completed!")
