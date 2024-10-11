import csv
import cv2

# Load Dataset

coverages = {}

with open("dataset.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for line in reader:
        char_name, char_coverage = line
        char_coverage = float(char_coverage)

        coverages[char_name] = char_coverage

# Translation
translation = {
    "Ampersand": "&",
    "At": "@",
    "Carat": "^",
    "CloseBrace": "}",
    "CloseBracket": "]",
    "CloseParanthesis": ")",
    "Dollar": "$",
    "Exclamation": "!",
    "LeftArrow": "<",
    "LowerA": "a",
    "LowerB": "b",
    "LowerC": "c",
    "LowerD": "d",
    "LowerE": "e",
    "LowerF": "f",
    "LowerG": "g",
    "LowerH": "h",
    "LowerI": "i",
    "LowerJ": "j",
    "LowerK": "k",
    "LowerL": "l",
    "LowerM": "m",
    "LowerN": "n",
    "LowerO": "o",
    "LowerP": "p",
    "LowerQ": "q",
    "LowerR": "r",
    "LowerS": "s",
    "LowerT": "t",
    "LowerU": "u",
    "LowerV": "v",
    "LowerW": "w",
    "LowerX": "x",
    "LowerY": "y",
    "LowerZ": "z",
    "OpenBrace": "{",
    "OpenParanthesis": "(",
    "OpenBracket": "[",
    "Percent": "%",
    "RightArrow": ">",
    "Sharp": "#",
    "Slash": "/",
    "Space": " ",
    "Star": "*",
    "Tilde": "~",
    "Won": "\\"
}

for k, v in translation.items():
    coverages[v] = coverages[k]
    del coverages[k]

# The coverages variable that used to be dict is now a list    
coverages = [(k, v) for k, v in sorted(coverages.items(), key = lambda x: x[1])] # This ambiguous typing...

# Main Program
images = cv2.VideoCapture("video.mp4")

with open("result.txt", "w") as file:
    while True:
        ret, image = images.read()
        
        if not ret:
            break
        
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.resize(image, (300, 60))

        for line in image:
            for col in line:
                coverage_index = int((255 - col) / 255 * (len(coverages) - 1))
                file.write(coverages[coverage_index][0])
            file.write("\n")
        file.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

images.release()
cv2.destroyAllWindows()