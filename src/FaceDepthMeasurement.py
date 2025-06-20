import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
import numpy as np

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)

textList = ["Welcome "," This is ram.",
            "A computer vision enthusiast,", " mechanical,", "Robotics and AI.",
            "If you like this", "this is your chance to make one"]

sen = 25  # more is less

while True:
    success, img = cap.read()
    if not success or img is None:
        print("Failed to grab frame from camera.")
        continue  # or break, depending on your loop
    imgText = np.zeros_like(img)
    img, faces = detector.findFaceMesh(img, draw=False)

    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]
        w, _ = detector.findDistance(pointLeft, pointRight)
        W = 6.3

        # Finding distance
        f = 840
        d = (W * f) / w
        print(d)

        cvzone.putTextRect(img, f'Depth: {int(d)}cm',
                           (face[10][0] - 100, face[10][1] - 50),
                           scale=2)

        for i, text in enumerate(textList):
            singleHeight = 20 + int((int(d/sen)*sen)/4)
            scale = 0.4 + (int(d/sen)*sen)/75
            cv2.putText(imgText, text, (50, 50 + (i * singleHeight)),
                        cv2.FONT_ITALIC, scale, (255, 255, 255), 2)

    imgStacked = cvzone.stackImages([img, imgText], 2, 1)
    cv2.imshow("Image", imgStacked)
    cv2.waitKey(1)