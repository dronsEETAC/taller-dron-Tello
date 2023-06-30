import cv2
import mediapipe as mp


def initialize ():
    global pose
    global mp_drawing
    global mp_drawing_styles
    global mp_pose

    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(
            static_image_mode=True,
            model_complexity=2,
            enable_segmentation=True,
            min_detection_confidence=0.5)


def prepareBody(image):
    global pose
    global mp_drawing
    global mp_drawing_styles
    global mp_pose


    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image)
    image.flags.writeable = True

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(
        image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    bodyLandmarks = []
    if results.pose_landmarks:
        for landmark in results.pose_landmarks.landmark:
            bodyLandmarks.append([landmark.x, landmark.y])
    return bodyLandmarks, image

def detectPose (bodyLandmarks):
    # pose 1
    if  bodyLandmarks[14][0] < bodyLandmarks[12][0] and \
        bodyLandmarks[16][0] < bodyLandmarks[14][0] and \
        bodyLandmarks[16][1] < bodyLandmarks[14][1] and \
        bodyLandmarks[14][1] < bodyLandmarks[12][1] and \
        bodyLandmarks[13][0] > bodyLandmarks[11][0] and \
        bodyLandmarks[15][0] > bodyLandmarks[13][0] and \
        bodyLandmarks[15][1] < bodyLandmarks[13][1] and \
        bodyLandmarks[13][1] < bodyLandmarks[11][1]:
        return 1
    # pose 2
    elif  bodyLandmarks[14][0] < bodyLandmarks[12][0] and \
        bodyLandmarks[16][0] > bodyLandmarks[14][0] and \
        bodyLandmarks[16][1] < bodyLandmarks[14][1] and \
        bodyLandmarks[14][1] < bodyLandmarks[12][1] and \
        bodyLandmarks[13][0] > bodyLandmarks[11][0] and \
        bodyLandmarks[15][0] > bodyLandmarks[13][0] and \
        bodyLandmarks[15][1] < bodyLandmarks[13][1] and \
        bodyLandmarks[13][1] < bodyLandmarks[11][1]:
        return 2
    # pose 3
    elif bodyLandmarks[14][0] < bodyLandmarks[12][0] and \
            bodyLandmarks[16][0] > bodyLandmarks[14][0] and \
            bodyLandmarks[16][1] < bodyLandmarks[14][1] and \
            bodyLandmarks[14][1] < bodyLandmarks[12][1] and \
            bodyLandmarks[13][0] > bodyLandmarks[11][0] and \
            bodyLandmarks[15][0] < bodyLandmarks[13][0] and \
            bodyLandmarks[15][1] < bodyLandmarks[13][1] and \
            bodyLandmarks[13][1] < bodyLandmarks[11][1]:
        return 3
    else:
        return 0

cap = cv2.VideoCapture(0)
initialize()



while True:
    result, computerFrame = cap.read()
    if result:
        computerFrame = cv2.resize(computerFrame, (720, 480))
        bodyLandmarks, frameWithLandmarks = prepareBody(computerFrame)
        frameWithLandmarks = cv2.flip(frameWithLandmarks, 1)
        if len (bodyLandmarks) > 0:
            miPose = detectPose(bodyLandmarks)

            print ('***** ', miPose)
            cv2.putText(frameWithLandmarks, "pose " +str(miPose), (100, 100),
                       cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 255, 255), 5)

        cv2.imshow("computer", frameWithLandmarks)
        cv2.waitKey(1)
