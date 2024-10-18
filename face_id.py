import face_recognition
from PIL import Image, ImageDraw
import cv2


# Step 1: Load the image of the individual face
def load_image(file_path):
    return face_recognition.load_image_file(file_path)


# Step 2: Encode faces in the image
def encode_faces(image):
    return face_recognition.face_encodings(image)


# Step 3: Compare the face encodings of the individual and group
def compare_faces(individual_encoding, group_encodings):
    matches = face_recognition.compare_faces(group_encodings, individual_encoding)
    return matches


# Step 4: Mark matched faces on the group image
def mark_faces_on_group_image(group_image, face_locations, face_matches):
    pil_image = Image.fromarray(group_image)
    draw = ImageDraw.Draw(pil_image)

    for (top, right, bottom, left), match in zip(face_locations, face_matches):
        if match:
            # Draw a box around the matching face
            draw.rectangle(((left, top), (right, bottom)), outline=(0, 255, 0), width=4)
        else:
            # Draw a box around the non-matching faces
            draw.rectangle(((left, top), (right, bottom)), outline=(255, 0, 0), width=4)

    del draw
    return pil_image


# Step 5: Main function to run facial recognition
def main(individual_image_path, group_image_path):
    # Load the individual face image and group image
    individual_image = load_image(individual_image_path)
    group_image = load_image(group_image_path)

    # Encode the individual face
    individual_face_encodings = encode_faces(individual_image)
    if len(individual_face_encodings) == 0:
        print("No face found in the individual image.")
        return

    individual_face_encoding = individual_face_encodings[0]

    # Encode the group faces
    group_face_encodings = encode_faces(group_image)
    group_face_locations = face_recognition.face_locations(group_image)

    if len(group_face_encodings) == 0:
        print("No faces found in the group image.")
        return

    # Compare faces
    matches = compare_faces(individual_face_encoding, group_face_encodings)

    # Check if there is a match
    if True in matches:
        print("Individual face found in the group!")
    else:
        print("Individual face not found in the group.")

    # Step 6: Mark faces on the group image
    result_image = mark_faces_on_group_image(group_image, group_face_locations, matches)

    # Save and display the result
    result_image.save('output_group_image.png')
    result_image.show()


# Run the program with the paths to the images
if __name__ == "__main__":
    individual_image_path = "individuals_face.jpg"  # Path to the individual's image
    group_image_path = "group_faces.jpg"  # Path to the group's image    # group_image_path = "Elon Musk Group 2.jpg"  # Path to the group's image
    main(individual_image_path, group_image_path)
