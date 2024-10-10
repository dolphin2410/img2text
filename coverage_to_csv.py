import os
import cv2
import numpy as np
import csv

with open("dataset.csv", "w", newline="\n") as file:
    writer = csv.writer(file)
    
    writer.writerow(["name", "coverage"])

    for image_file_name in os.listdir("dataset"):
        image_name, extension = image_file_name.split(".")

        if extension != "png":
            continue  # skip files that doesn't end wiht a .png
        
        relative_path = f"./dataset/{image_file_name}"

        image = cv2.imread(relative_path, cv2.IMREAD_UNCHANGED)[:, :, 3]

        n_black_pixels = np.count_nonzero(image)

        x, y = image.shape
        
        coverage = n_black_pixels / (x * y)
        print(image_name, coverage)
        
        writer.writerow([image_name, coverage])




