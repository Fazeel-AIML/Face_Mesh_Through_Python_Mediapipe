# Face Mesh Through Python MediaPipe

This repository contains a Python script for facial landmark detection using MediaPipe's FaceMesh. The script leverages MediaPipe's powerful tools to detect and visualize facial landmarks in real-time.

## Requirements

- `mediapipe`
- `opencv-python`
- `numpy`

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Fazeel-AIML/Face_Mesh_Through_Python_Mediapipe.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd Face_Mesh_Through_Python_Mediapipe
    ```

3. **Install the required packages**:
    ```bash
    pip install mediapipe opencv-python numpy
    ```

## Usage

1. **Run the script**:
    ```bash
    python facemesh_script.py
    ```

2. The script will open your webcam, detect faces, and overlay facial landmarks on the video feed in real-time.

## Example

- Upon execution, the script captures video from your webcam and displays facial landmarks on detected faces.
- ![App Demo](Demo.gif)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
