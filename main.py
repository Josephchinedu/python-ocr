import os


def ocr_helper(image):
    import pytesseract
    from pdf2image import convert_from_path

    text = ""

    # print("Reading image")
    # print(image)

    try:
        text = pytesseract.image_to_string(image)
    except Exception as e:
        print(
            f"""
        Image: {image}
        Error in reading image
        {e}
        """
        )


    

    return text


# Function to read files in a directory
def read_files_in_directory():
    directory_path = "screenshots"
    # List all files and directories in the given directory
    files_in_folder = os.listdir(directory_path)

    return files_in_folder


if __name__ == "__main__":
    files = read_files_in_directory()
    for file in files:
        # print(file)
        text = ocr_helper(os.path.join("screenshots", file))
        with open("output.txt", "a") as f:
            f.write(text)
