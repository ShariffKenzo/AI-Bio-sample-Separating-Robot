import cv2

def SampleDetector(x,y):
    
#cap = cv2.VideoCapture(0)  # use cv2.CAP_DSHOW for quicker response
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
    ## new line below
    cap.set(cv2.CAP_PROP_AUTOFOCUS, 28)  

#while True:

    _, frame = cap.read() 
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

   # cx = int(width/2)
   # cy = int(height/2)

    cx = int(x)
    cy = int(y)
    #select pixel center = hsv_frame[cy,cx]

    pixel_center = hsv_frame[cy,cx]
    #pixel_center = frame[cy,cx]
    hue_value = pixel_center[1]

    print(pixel_center)
    color = "Undefined"

    if hue_value < 30:
        color = "WHITE"
        return 0
    
    else:
        color = "Not White"
        return 1
    
   # pixel_center_bgr = frame[cy, cx]
   # b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

   # cv2.rectangle(frame, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)
   # cv2.putText(frame, color, (cx - 200, 100), 0, 3, (b, g, r), 5)
   # cv2.circle(frame, (cx, cy), 5, (255, 25, 25), 3)


   # cv2.imshow("ColourDetector", frame)
   # key  = cv2.waitKey(100)

   # if key ==27:
   #     break

#cap.release()
#cv2.destroyAllWindows()

    
    
