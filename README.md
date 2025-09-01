# Static-Hand-Gesture-Recognition-Public
Overview of Project

This project demonstrates real-time static hand gesture recognition using MediaPipe and OpenCV. It detects and classifies four predefined gestures from a live webcam feed:

🖐 Open Palm

✊ Fist

✌ Peace Sign (V-sign)

👍 Thumbs Up

The system processes webcam frames, performs hand landmark detection with MediaPipe, applies simple rule-based classification logic, and displays the recognized gesture directly on the video stream.

Technology Justification
MediaPipe Hands

Provides 21 high-precision landmark points per hand.

Lightweight and optimized for real-time applications.

Handles detection and tracking seamlessly with built-in models.

OpenCV

Handles video capture, preprocessing, and visualization.

Provides utilities for drawing, displaying text, and window management.

Why this choice?

MediaPipe offers direct landmark detection, which allows us to design custom gesture logic without needing external wrappers. OpenCV complements it by efficiently handling webcam streaming and visualization. This combination ensures flexibility, speed, and simplicity.

Gesture Logic Explanation

Using mediapipe.solutions.hands, we extract landmark points (x, y, z coordinates). Based on these, we define rules for finger states (open or closed):

Thumb Rule: Compare x-coordinates of tip (4) and joint (3).

Other Fingers: Compare y-coordinates of tip vs. proximal joint (tip-2).

Gesture Classification Rules

🖐 Open Palm

Condition: [1, 1, 1, 1, 1] (all fingers open).

Visual feedback: label “Open Palm” displayed.

✊ Fist

Condition: [0, 0, 0, 0, 0] (all fingers closed).

Visual feedback: “Fist” displayed.

✌ Peace Sign (V-sign)

Condition: [0, 1, 1, 0, 0] (index and middle open).

Visual feedback: “Peace Sign”.

👍 Thumbs Up

Condition: [1, 0, 0, 0, 0] (thumb open only).

Visual feedback: “Thumbs Up”.

Any other finger combination → “Unknown”.


Algorithm

Initialize OpenCV webcam capture.

Load MediaPipe Hands with detection confidence = 0.7.

Capture video frames in loop.

Preprocess frames (flip, RGB conversion).

Detect hands → extract 21 landmarks.

Apply custom classify_gesture() rules.

Overlay gesture name + hand skeleton on frame.

Display results in real time until user quits.
