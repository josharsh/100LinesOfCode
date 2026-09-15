# Face Detection with OpenCV

A simple real-time face detection project using Python and OpenCV. It uses a Haar Cascade classifier to detect faces from a webcam stream.

## Requirements

- Python 3.x
- OpenCV
- Jupyter Notebook

Install OpenCV with:

`pip install opencv-python`

## How to Run

1. Open `face_detection.ipynb` in Jupyter Notebook or VS Code.
2. Run the cells from top to bottom.
3. Allow access to your webcam when prompted.
4. A window will show the camera feed with detected faces.
5. Press `Esc` to stop the video capture.

## Camera Selection

The notebook uses camera index `1`.

If your webcam does not open, change `cv2.VideoCapture(1)` to `cv2.VideoCapture(0)`.

You can try another camera index if your computer has multiple cameras.

## How It Works

The project uses OpenCV's pre-trained Haar Cascade face detector.

1. Capture a frame from the webcam.
2. Convert the frame to grayscale.
3. Detect faces in the frame.
4. Draw rectangles around detected faces.
5. Display the camera feed.

## Note

Face detection works best when the camera has reasonable lighting and the face is clearly visible.