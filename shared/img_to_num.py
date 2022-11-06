import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\\tesseract.exe"

def from_img(img, name="", show_debug=False, should_invert=True):
    formatted_img = cv2.adaptiveThreshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 2)
    if should_invert:
        formatted_img = cv2.bitwise_not(formatted_img)
    
    if show_debug:
        cv2.imshow(name, formatted_img)
        cv2.waitKey(0)

    result = pytesseract.image_to_string(formatted_img, config="--psm 6")
    num = ""
    for char in result:
        if char in "0123456789":
            num += char

    try:
        num = int(num)
        return num
    except:
        return None