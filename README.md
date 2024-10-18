# Face Recognition Program

This program performs facial recognition to identify a specific individual in a group photo. It uses Python libraries such as `face_recognition`, `PIL` (Pillow), and `cv2` (OpenCV) to encode facial features, compare them, and highlight matching faces in an image.

## Features

- Load an individual’s image and encode their facial features.
- Load a group image, detect faces, and encode their facial features.
- Compare the individual's face with the group faces to find matches.
- Draw a green box around matching faces and red boxes around non-matching faces.
- Save the output image with the marked faces.
  
## Technologies Used

- **Python**: The programming language used for writing the script.
- **face_recognition**: A powerful library for face recognition that simplifies encoding and face comparison.
- **PIL (Pillow)**: Used for image manipulation, specifically drawing boxes around detected faces.
- **OpenCV (cv2)**: Utilized for image processing.
  
## How to Use

### Prerequisites

1. Install Python (version 3.x).
2. Install the required libraries using pip:

    ```bash
    pip install face_recognition pillow opencv-python
    ```

### Running the Program

1. Place the image of the individual in the project directory (e.g., `individuals_face.jpg`).
2. Place the group image in the same directory (e.g., `group_faces.jpg`).
3. Run the program by executing the following command:

    ```bash
    python face_recognition_program.py
    ```

4. The program will:
    - Load the individual’s face and the group image.
    - Compare the faces from both images.
    - Highlight matching faces with a green box in the output image (`output_group_image.png`).
    - Open the output image for viewing.

### Example

In this section, I will post sample images of the program in action. For example, using a sample picture of Elon Musk, the program identifies him in a group of people and highlights his face with a green box.

#### images:
- **Input Individual Image (Elon Musk)**
  
  ![Elon Musk](https://github.com/user-attachments/assets/aaca44e3-fad8-46e5-8c25-2ada8b145531)

- **Group Image**

  ![Elon Musk Group 2](https://github.com/user-attachments/assets/d6d1a3ea-1fd3-4181-9997-888d7afce1c7)

- **Output Image**

  ![output_group_image](https://github.com/user-attachments/assets/9080211e-3f64-4336-99b5-90cca93c6684)

### Notes

- Ensure that the individual image contains a clear view of the face.
- If no face is found in either the individual or group images, the program will output a message indicating the issue.
