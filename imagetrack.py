import cv2
import mediapipe as mp

def hand_tracker(queue):
    """
    A simple hand tracking example using MediaPipe.
    This function returns the y-coordinate of the index finger tip (landmark 8).
    It places the coordinate into the provided queue.
    """
    mp_hands = mp.solutions.hands 
    mp_drawing = mp.solutions.drawing_utils

    # Start webcam
    cap = cv2.VideoCapture(0)

    with mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.5
    ) as hands:

        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                break

            # Flip for mirror effect and convert BGR to RGB
            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process the frame
            results = hands.process(rgb)

            # Draw hand landmarks and send index tip y to queue
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    index_tip = hand_landmarks.landmark[8]
                    queue.put(index_tip.y)

                    mp_drawing.draw_landmarks(
                        frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
                    )

            cv2.imshow('Hand Tracking', frame)

            if cv2.waitKey(5) & 0xFF == 27:  # ESC key
                break

    cap.release()
    cv2.destroyAllWindows()
