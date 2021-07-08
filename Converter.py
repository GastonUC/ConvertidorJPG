#https://thequickblog.com/convert-any-image-to-jpg-format-using-python/
#https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
# from PIL import Image
#Recordar que cualquier modificación luego de la creación del '.exe' no será ejecutada en tal.

# import os
# import sys
# #check whether the user passed the input image or not
# if len(sys.argv) > 1:
#     file =sys.argv[1]
#     if os.path.exists(file):
#         filename=file.split(".")
#         img = Image.open(file)
#         target_name = filename[0] + ".jpg"
#         rgb_image = img.convert('RGB')
#         rgb_image.save(target_name)
#         print("Converted image saved as " + target_name)
#     else:
#         print(file + " not found in given location")
# else:
#     print("please execute the script with input image as : python Converter.py <file>")

#La real solution

from PIL import Image

import os
import ctypes

dir = "./RawImages/"

with os.scandir(dir) as i:
    for entry in i:
        if entry.is_file():
            file = entry.name
            filename = file.split(".")
            img = Image.open(str(dir)+file)
            target_name = filename[0] + ".jpg"
            rgb_image = img.convert('RGB')
            rgb_image.save(target_name)
            print("Converted image saved as " + target_name)
            os.remove(entry.path)
        else:
            print(file + " not found in given location")
            ctypes.windll.user32.MessageBoxW(0, file + "No se ha encontrado en la dirección indicada", "Erro al Convertir", 0)
    ctypes.windll.user32.MessageBoxW(0, "La conversión ha finalizado.", "Conversión a JPG", 0)