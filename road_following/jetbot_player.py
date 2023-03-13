# 202107 brighteyes
# jetbot camera test


import cv2
import numpy as np

def Video(openpath):
    cap = cv2.VideoCapture(openpath)
    if cap.isOpened():
        print("Video Opened")
    else:
        print("Video Not Opened")
        print("Program Abort")
        exit()
    fps = cap.get(cv2.CAP_PROP_FPS)
    print('fps : {}'.format(fps))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
    #fourcc = cv2.VideoWriter_fourcc('m','p','4','v') with *.mp4 save

    cv2.namedWindow("Input", cv2.WINDOW_GUI_EXPANDED)

    try:
        while cap.isOpened():
            # Capture frame-by-frame
            ret, frame = cap.read()
            if ret:

                # Display the resulting frame
                cv2.imshow("Input", frame)

            else:
                break
            # waitKey(int(1000.0/fps)) for matching fps of video
            if cv2.waitKey(int(1000.0/fps)) & 0xFF == ord('q'):
                break
    except KeyboardInterrupt:  
        print("key int")
        cap.release()
        cv2.destroyAllWindows()
        exit()
    # When everything done, release the capture
    cap.release()

    cv2.destroyAllWindows()
    return
   
if __name__=="__main__":
    Video("./output.avi")
