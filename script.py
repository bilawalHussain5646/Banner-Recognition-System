# # adds image processing capabilities
from PIL import Image
# # will convert the image to text string
# import pytesseract

# pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# # assigning an image from the source path
# img = Image.open('test2.jpg')
# # converts the image to result and saves it into result variable
# result = pytesseract.image_to_string(img)

# print(result)

# from PIL import Image


# result = pytesseract.pytesseract.image_to_data(Image.open('test2.jpg'))

# import matplotlib.pyplot as plt 

# im = plt.imread('test2.jpg')
# print(im.shape)

# fig = plt.figure(figsize=(15,15))

# plt.imshow(im)

# for i in range(len(result)):
#     row = result.iloc[i]
#     if row['conf'] > 0:
#         x = [row['left'], row['left']+row['width'], row['left']+row['width'], row['left'], row['left']]
#         y = [row['top'], row['top'], row['top']+row['height'], row['top']+row['height'], row['top']]
#         plt.fill(x,y, facecolor='none', edgecolor='red')
#         plt.text(x[0],y[0], row['text'], color='red', fontsize=15)

# plt.axis('off')
# plt.savefig('output.png')
# plt.show()

# import easyocr
# reader = easyocr.Reader(['en'],gpu=True)
# result = reader.readtext('https://media.extra.com/i/aurora/Discount_LargeAppliance_HS_E_4.webp', detail = 0)
# print(result)

import easyocr
import requests
from io import BytesIO
# Set the URL of the image
import requests
from html2image import Html2Image




# Details:
#--------------------------------------------------------------
# From the html 
    # Save html url as image 
    # Once saved pass that image to the AI and get the text
    # If the text has LG then count the banner 
# -------------------------------------------------------------

def Calculate_Images(image_url):
    hti = Html2Image()
    hti.screenshot(url=image_url, save_as='output.png')
    # url = "https://media.extra.com/i/aurora/Discount_LargeAppliance_HS_E_4.webp"

    reader = easyocr.Reader(['en'], gpu=True)
    # Process the image using easyocr
    result = reader.readtext("output.png", detail=0)
    # Print the result
    print(result)

    count = 0
    for res in result:
        if "LG" in res:
            count+=1
            break
    print(count)
    return count 

Calculate_Images('https://media.extra.com/i/aurora/Buy1_Get1_TVs_HS_E_1?fmt=webp,%20//media.extra.com/i/aurora/Buy1_Get1_TVs_HS_E_1?fmt=jpg,%20//media.extra.com/i/aurora/Buy1_Get1_TVs_HS_E_1?fmt=jp2')