import cv2
from cvzone.FaceMeshModule import FaceMeshDetector
from dynamic_font import get_font_scale_for_height

cap = cv2.VideoCapture(0)  # Use your working camera index
detector = FaceMeshDetector(maxFaces=1)

while True:
    success, img = cap.read()
    if not success or img is None:
        print("Failed to grab frame from camera.")
        break

    img, faces = detector.findFaceMesh(img, draw=False)
    if faces:
        face = faces[0]
        # Example: Use points 145 and 374 for left/right eye, 1 and 152 for top/bottom
        left_eye = face[145]
        right_eye = face[374]
        top = face[10]
        bottom = face[152]

        # Calculate face "depth" (distance between eyes, or top-bottom)
        face_width = ((left_eye[0] - right_eye[0])**2 + (left_eye[1] - right_eye[1])**2) ** 0.5
        face_height = ((top[0] - bottom[0])**2 + (top[1] - bottom[1])**2) ** 0.5

        # Map face_width or face_height to a desired text height in pixels (arbitrary mapping)
        # For example: closer face = bigger text
        min_height, max_height = 20, 80
        min_face, max_face = 60, 200  # Tune these for your camera/setup
        desired_height = int(max(min_height, min(max_height, (max_face - face_width) + min_height)))

        # Calculate dynamic font scale
        text = "Dynamic Text"
        font_face = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = get_font_scale_for_height(text, font_face, desired_height)
        thickness = 2

        # Draw text
        cv2.putText(img, text, (50, 100), font_face, font_scale, (0, 255, 0), thickness, cv2.LINE_AA)

    cv2.imshow("Dynamic Text Size", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
