from pyzbar import pyzbar
import cv2
import pandas as pd

def draw_barcode(decoded, image):
    image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top), 
                            (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                            color=(0, 255, 0),
                            thickness=5)
    return image

def decode(image):
    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        # draw the barcode
        image = draw_barcode(obj, image)

    return image, decoded_objects

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    input("Press enter to start.")
    
    saved_decode = b'none'

    reqnum = 10
    tries = 0

    while True:
        # read the frame from the camera
        _, frame = cap.read()
        # decode detected barcodes & get the image that is drawn
        frame, decoded_objects = decode(frame) 
        # show the image in the window
        cv2.imshow("frame", frame)

        if decoded_objects and saved_decode == decoded_objects[0].data:
            print("Confirming Barcode...")
            tries += 1
        elif decoded_objects:
            tries = 0
            saved_decode = decoded_objects[0].data
            print('Replace with: ', saved_decode)

        if cv2.waitKey(1) == ord("q") or tries == reqnum:
            print("[+] Barcode Info:", saved_decode)
            break
    
    print("Checking validity...")
    df = pd.read_csv('check.csv')
    
    print(df)
    query = df.query(f'ID == {int(saved_decode)} and vaccinated == "T"')

    print("Invalid Barcode" if query.empty else "Valid Barcode")

    
    

