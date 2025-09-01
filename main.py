import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# OpenCV webcam
cap = cv2.VideoCapture(0)

# Gesture classifier function
def classify_gesture(landmarks):
    """
    Simple rules-based gesture classification using finger positions.
    landmarks: list of 21 hand landmark points (x, y normalized)
    Returns: str (gesture name)
    """
    # Get y-coordinates of fingertips & relevant joints
    finger_tips = [8, 12, 16, 20]  # Index, Middle, Ring, Pinky
    thumb_tip = 4

    fingers = []

    # Thumb: check x-coordinates (different rule from other fingers)
    if landmarks[thumb_tip].x < landmarks[3].x:  # left of thumb joint
        fingers.append(1)  # open
    else:
        fingers.append(0)  # closed

    # Other four fingers
    for tip in finger_tips:
        if landmarks[tip].y < landmarks[tip - 2].y:  # tip above pip joint
            fingers.append(1)  # open
        else:
            fingers.append(0)  # closed

    # Classify gestures
    if fingers == [1,1,1,1,1]:
        return "Open Palm"
    elif fingers == [0,0,0,0,0]:
        return "Fist"
    elif fingers == [0,1,1,0,0]:
        return "Peace Sign"
    elif fingers == [1,0,0,0,0]:
        return "Thumbs Up"
    else:
        return "Unknown"

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Flip image for natural interaction
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        gesture_name = "No Hand"

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                gesture_name = classify_gesture(hand_landmarks.landmark)

        # Show recognized gesture on screen
        cv2.putText(frame, f"Gesture: {gesture_name}", (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Hand Gesture Recognition", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
