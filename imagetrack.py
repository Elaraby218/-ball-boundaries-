import cv2
import mediapipe as mp




def hand_tracker(queue):
    """
    A simple hand tracking example using MediaPipe.
    this function returns the coordinates of the index finger tip (index finger).
    return it to a queue
    """

    # Initialize MediaPipe Hands
    mp_hands = mp.solutions.hands # pyright: ignore[reportAttributeAccessIssue]
    hands = mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.5
    )


    # Start webcam
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        # Flip for mirror effect and convert BGR to RGB
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame
        results = hands.process(rgb)

        # Draw hand landmarks
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:

                # Example: Get index finger tip (landmark 8)
                index_tip = hand_landmarks.landmark[8]
                queue.put(index_tip.y )
                

    cap.release()
