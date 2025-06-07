import cv2

for idx in range(3):
    cap = cv2.VideoCapture(idx)
    if cap.isOpened():
        print(f"Camera index {idx} opened successfully.")
        ret, frame = cap.read()
        if ret:
            cv2.imshow(f'Camera {idx}', frame)
            cv2.waitKey(2000)  # Show for 2 seconds
            cv2.destroyAllWindows()
        cap.release()
    else:
        print(f"Camera index {idx} failed.")
