import cv2

#### note set to 720 by 1080
def PlasmaCount(x,index):

   #cap = cv2.VideoCapture(0)
    cap =cv2.VideoCapture(0, cv2.CAP_DSHOW)
    #cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
    #cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
    cap.set(3, 1280) # set the resolution
    cap.set(4, 720)
    cap.set(28,90)
    
    _, frame = cap.read() 
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    #  cx = int(width/2)
    #  cy = int(height/2)

    cx= int(x)
    cy= int(675) #can't read at height need to offset by n ,

        #select pixel center = hsv_frame[cy,cx]

    pixel_center = hsv_frame[cy,cx]
        #pixel_center = frame[cy,cx]
    hue_value = pixel_center[0]

    print(pixel_center)
    color = "Undefined"

    if hue_value < 5:
        color = "RED"
    elif hue_value < 22:
        color = "ORANGE"
    elif hue_value < 33:
        color = "YELLOW"
    elif hue_value < 78:
        color = "GREEN"
    elif hue_value < 131:
        color = "BLUE"
    elif hue_value < 170:
        color = "VIOLET"
    else:
        color = "RED"
        
    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

#    cv2.rectangle(frame, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)
#    cv2.putText(frame, color, (cx - 200, 100), 0, 3, (b, g, r), 5)
#    cv2.circle(frame, (cx, cy), 5, (255, 25, 25), 3)


   # cv2.imshow("ColourDetector", frame)
   # key  = cv2.waitKey(100)

    counter  = 0

    while True:
          #  colorOld = color
            cx= int(x)
            cy= cy -1
            pixel_center = hsv_frame[cy,cx]
            hue_value = pixel_center[0]

            if hue_value < 5:
             color = "RED"
            elif hue_value < 14:
             color = "ORANGE"
            elif hue_value < 33:
             color = "YELLOW"
            elif hue_value < 78:
             color = "GREEN"
            elif hue_value < 131:
             color = "BLUE"
            elif hue_value < 170:
             color = "VIOLET"
            else:
             color = "RED"
            
            if color == "YELLOW":
                counter= counter+1
        #    else:
         #       break
            if cy == 0:
                break
            print(counter)
    
    ####### calibration portion in comment for now
    ####### length = (counter/480) * length
        

    print(counter)
    if index == 1:
        suction = (counter/590) *9.5
    #Zdist = counter/480 *100
    if index ==2 :
        suction  = (counter/588) * 9.5
    if index ==3:
        suction  = (counter/586) * 9.5
    if index == 4:
        suction = (counter/585) * 9.5
    if index == 5:
        suction =(counter/ 580) * 9.5

    return suction
    #cap.release()
    #cv2.destroyAllWindows()

        
        
