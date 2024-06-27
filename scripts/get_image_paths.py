import os

# Prompt the user for the directory path
image_directory = input("Enter the path to the directory containing images: ")

# Ensure the provided path exists and is a directory
if not os.path.isdir(image_directory):
    print("Error: The provided path is not a directory or does not exist.")
    exit(1)

# Get a list of all files in the directory
image_files = os.listdir(image_directory)

# Filter out only the image files (common formats)
image_files = [f for f in image_files if f.lower().endswith(
    ('.png', '.jpg', '.jpeg', '.gif', '.svg'))]

# Generate the list in manifest format
image_list = ',\n    '.join(
    [f"'{image_directory}/{file}'" for file in image_files])

# Print the formatted list
print(image_list)
