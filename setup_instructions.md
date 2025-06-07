# Setup Instructions

## 1. Install Python

- Use Python 3.7 to 3.11 (MediaPipe may not support 3.12+ yet).
- Download from https://www.python.org/downloads/

## 2. Create a Virtual Environment

Open a terminal in your project folder and run:

### Windows
python -m venv venv
venv\Scripts\activate

### macOS/Linux
python3 -m venv venv
source venv/bin/activate

## 3. Install Dependencies
pip install -r requirements.txt

## 4. Run the Code

python src/FaceDepthMeasurement.py
or 
python src/DynamicTextReader.py

## 5. Camera Index

If your camera doesn't work, try changing the index in the code:
- `cv2.VideoCapture(0)` for laptop camera
- `cv2.VideoCapture(1)` or `cv2.VideoCapture(2)` for external cameras

