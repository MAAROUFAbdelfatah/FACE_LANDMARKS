import cv2
import mediapipe as mp
import time

from mediapipe.python.solutions.face_mesh import FaceMesh

cap = cv2.VideoCapture(0)
pTime = 0


mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces = 5)
drawSpec = mpDraw.DrawingSpec(thickness = 1, circle_radius = 1)

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    resultes = faceMesh.process(imgRGB)
    if resultes.multi_face_landmarks:
        for faceLms in resultes.multi_face_landmarks:
            mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACEMESH_CONTOURS, drawSpec, drawSpec)
        #print(faceLms)
    cTime = time.time()
    fps = 1 / ( cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS:{int(fps)}', (28, 78), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    key = cv2.waitKey(1)
    if key == 27:
        break
