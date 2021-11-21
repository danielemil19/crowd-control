import cv2
import numpy as np
import pandas as pd
from pyzbar.pyzbar import decode


def scan():
    def decoder(image):
        gray_img = cv2.cvtColor(image,0)
        code = decode(gray_img)
    
        for obj in code:
            points = obj.polygon
            (x,y,w,h) = obj.rect
            pts = np.array(points, np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(image, [pts], True, (0, 255, 0), 3)
    
            codeData = obj.data.decode("utf-8")
            codeType = obj.type
            string = "Data " + str(codeData) + " | Type " + str(codeType)
            
            cv2.putText(frame, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0), 2)
            print("Code: "+codeData +" | Type: "+codeType)
    
        return code

    saved_data = ''

    reqnum = 10
    tries = 0

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        code = decoder(frame)
        
        cv2.imshow('Image', frame)
            
        if code and saved_data == code[0].data.decode("utf-8"):
            print("Confirming Barcode...")
            tries += 1
        elif code:
            tries = 0
            saved_data = code[0].data.decode("utf-8")
            print('Replace with: ', saved_data)

        key = cv2.waitKey(10)
        if key == ord('q') or tries == reqnum:
            print("[+] Code Info:", saved_data)
            break

    codeData = code[0].data.decode("utf-8")
    codeType = code[0].type
    valid = False
        
    if codeType == 'CODE39':
        print("Checking validity...")
        df = pd.read_csv('check.csv')

        print(df)
        query = df.query(f'ID == {int(saved_data)} and vaccinated == "T"')
        
        if query.empty:
            print("Invalid Barcode")
        else:
            print("Valid Barcode")
            valid = True
    elif codeType == 'QRCODE':
        print(len(codeData))
        if len(codeData) > 1000:
            print('Probably a VacuID')
            valid = True
    else:
        print('Unsupported Type:', codeType)

    return valid

scan()
