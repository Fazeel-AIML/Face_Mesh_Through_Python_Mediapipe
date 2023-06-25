import mediapipe as mp
import cv2

webcam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh()
while 1:
    _,frame = webcam.read()
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output = face_mesh.process(gray_frame)
    face_landmarks = output.multi_face_landmarks
    face_h,face_w,_ =  frame.shape
    if face_landmarks:
        landmarks = face_landmarks[0].landmark
        for landmark in landmarks:
            x = int(landmark.x * face_w)
            y = int(landmark.y * face_h)
            cv2.circle(frame,(x,y),3,(0,0,255))
    cv2.imshow("window",frame)
    cv2.waitKey(1)
webcam.release()