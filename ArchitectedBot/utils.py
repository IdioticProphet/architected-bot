import pytesseract, os, cv2
import numpy as np
from difflib import SequenceMatcher
from PIL import Image


def was_killed_by_architects(img_name) -> bool:
    img = cv2.imread(img_name)
    original = img
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray, img_bin = cv2.threshold(gray,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    gray = cv2.bitwise_not(img_bin)
    kernel = np.ones((2, 1), np.uint8)
    img = cv2.erode(gray, kernel, iterations=1)
    img = cv2.dilate(img, kernel, iterations=1)
    #cv2.imshow("img", img)
    for im in [img, original, Image.open(img_name)]:
        string = pytesseract.image_to_string(im, timeout=3)
        for st in string.splitlines():
            split_str = st.split(" ")
            for index in range(0, len(split_str)//4+1):
                match_string = " ".join(split_str[index:index+4])
                matcher = SequenceMatcher(lambda x: x==" ", "Killed by the archetects".lower(), match_string.lower()) 
                #print(matcher.ratio())
                #print(match_string)
                if matcher.ratio() > .8:
                    return True
    


if __name__ == "__main__":
    directory = "C:\\Users\\joshu\\Desktop\\Architected\\"
    #was_killed_by_archetects(cv2.imread(directory+"difficult.png"))
    
    for file in os.listdir(directory):
        print(was_killed_by_archetects(directory+file))
