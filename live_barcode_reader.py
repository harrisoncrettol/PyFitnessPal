from pyzbar import pyzbar
import cv2


def draw_barcode(decoded, image):
    # n_points = len(decoded.polygon)
    # for i in range(n_points):
    #     image = cv2.line(image, decoded.polygon[i], decoded.polygon[(i+1) % n_points], color=(0, 255, 0), thickness=5)
    image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top), 
                            (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                            color=(0, 255, 0),
                            thickness=5)
    return image

# returns [frame, barcode]
def decode(image):
    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        # draw the barcode
        image = draw_barcode(obj, image)
        # print barcode type & data
        #print("Type:", obj.type)
        #print("Data:", obj.data)
        #print()
        if obj.type == "EAN13":
            return [image, obj.data]

    return [image, -1]

# uses webcam to scan a barcode
# returns a barcode (None if barcode was not found)
def scan_barcode():
    window_name = "WindowFrame"
    cap = cv2.VideoCapture(0)
    while True:
        # read the frame from the camera
        _, frame = cap.read()
        # decode detected barcodes & get the image
        # that is drawn
        frame, barcode = decode(frame)
        # show the image in the window
        cv2.imshow(window_name, frame)
        if (cv2.waitKey(1) == ord("q")) or (cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1) or (barcode != -1):
            break
    
    cv2.destroyAllWindows()
    return barcode
    

if __name__ == '__main__':
    barcode = scan_barcode()
    print(barcode)