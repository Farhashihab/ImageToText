import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('img2.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

imgHeight, imgWidth, __ = img.shape
# roi = img[0:imgHeight, 400:imgWidth]
# cv2.imshow('Roi', roi)

# ##TIME TO DETECT CHARACTER##

# print(imgHeight,imgWidth)
# boxes = pytesseract.image_to_boxes(img)
# for b in boxes.splitlines():
#     b = b.split(" ")
#     # print(b)
#     x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
#     cv2.rectangle(img,(x,imgHeight-y),(w,imgHeight-h),(0,0,255),1)
#     cv2.putText(img,b[0],(x,imgHeight-y+25),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(50,50,255),1)


##TIME TO DETECT DATA##
imgHeight,imgWidth,__ = img.shape
print(imgHeight,imgWidth)
boxes = pytesseract.image_to_data(img)
for x,b in enumerate(boxes.splitlines()):
    if x!=0:
        b = b.split()
        # print(b)
        if len(b)==12:
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),1)
            # cv2.putText(img,b[0],(x,imgHeight-y+25),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(50,50,255),1)
            print(b[11])

##TIME TO DETECT CHARACTER##
# imgHeight,imgWidth,__ = img.shape
# print(imgHeight,imgWidth)
# conf = r'--oem 3 --psm 6 outputbase digits'
# boxes = pytesseract.image_to_boxes(img,config=conf)
# for b in boxes.splitlines():
#     b = b.split(" ")
#     # print(b)
#     x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
#     cv2.rectangle(img,(x,imgHeight-y),(w,imgHeight-h),(0,0,255),1)
#     cv2.putText(img,b[0],(x,imgHeight-y+25),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(50,50,255),1)


cv2.imshow("Image", img)
cv2.waitKey(0)
