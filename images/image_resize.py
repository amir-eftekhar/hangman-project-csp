import turtle as t
import os
from PIL import Image

def resize_image(input_path, width, height, suffix):
    try:
        img = Image.open(input_path)

       
        dir_name = os.path.dirname(input_path)
        file_name, file_ext = os.path.splitext(os.path.basename(input_path))
        output_path = os.path.join(dir_name, f"{file_name}_{suffix}{file_ext}")

        img.resize((width, height), Image.LANCZOS).save(output_path)
        return output_path  
    except FileNotFoundError:
        print(f"No file found at {input_path}. Please make sure the file path is correct.")
        return None
    
    


def check_file(file_path):
  if os.path.exists(file_path) and os.path.isfile(file_path):
    print(f"File found: {file_path}")
  else:
    print(f"File NOT found: {file_path}")