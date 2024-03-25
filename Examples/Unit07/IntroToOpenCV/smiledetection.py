"""
A program to detect faces and smiles in 
pictures and videos. 

@author: Nandhini Namasivayam
@version: March 2024

Adopted from GeeksforGeeks
"""
import cv2
from matplotlib import pyplot as plt

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def image_smile_detection(image=None, filepath=None, display=False):
    """
    Detects smiles in still images.
    Can take in an image or a filepath. By default, 
    does not display the image.
    Args:
        image (Image, optional): The image to identify smiles in. Defaults to None.
        filepath (String, optional): The filepath to the image. Defaults to None.
        display (bool, optional): If True, displays the image after detecting smiles. Defaults to False.

    Returns:
        Image: The RGB version of the image
    """
    # Load pre-trained classifiers
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

    if filepath != None:
        image = cv2.imread(filepath)
    
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Find faces in the image
    faces = face_cascade.detectMultiScale(img_gray, scaleFactor=1.1, minSize=(128,128))

    # Loop through each face
    for (start_x, start_y, width, height) in faces:
        end_x = start_x + width
        end_y = start_y + height

        # Draw a red rectangle around each face
        cv2.rectangle(img_rgb, (start_x, start_y), (end_x, end_y), RED, 2)

        # Section out faces and find smiles in them
        section_gray = img_gray[start_y:end_y, start_x:end_x]
        section_rgb = img_rgb[start_y:end_y, start_x:end_x]

        # Detect smiles
        smiles = smile_cascade.detectMultiScale(section_gray, scaleFactor=1.9, minSize=(64,64))

        # Loop through each smile
        for (start_x_smile, start_y_smile, width_smile, height_smile) in smiles:
            end_x_smile = start_x_smile + width_smile
            end_y_smile = start_y_smile + height_smile

            # Draw a blue rectangle around each smile
            cv2.rectangle(section_rgb, (start_x_smile, start_y_smile), (end_x_smile, end_y_smile), BLUE, 2)

    # Display our images
    if display:
        plt.subplot(1, 1, 1)
        plt.imshow(img_rgb)
        plt.show()

    return img_rgb

def video_smile_detection():
    # Open video stream
    video = cv2.VideoCapture(0)

    # Loop until the end of the video
    while video.isOpened():
        # Get a frame
        frame = video.read()[1]

        img = image_smile_detection(frame)

        # Display the image
        cv2.imshow("Smile!", cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        # Use q to exit video
        if cv2.waitKey(60) & 0xFF == ord('q'):
            break
    
    # Shutdown video stream
    video.release()

def draw_box_on_head():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    box_height = 200

    # Capture video from the webcam
    video = cv2.VideoCapture(0)

    while video.isOpened():
        frame = video.read()[1]

        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        faces = face_cascade.detectMultiScale(img_gray, scaleFactor=1.1, minSize=(128,128))

        for (start_x, start_y, width, height) in faces:
            end_x = start_x + width
            end_y = start_y + height

            # Draw rectangle
            cv2.rectangle(img_rgb, (start_x, start_y), (end_x, start_y - box_height), BLUE, 2)
        
        # Display our images
        cv2.imshow("Top Hat!", cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB))

        # Use q to exit video
        if cv2.waitKey(60) & 0xFF == ord('q'):
            break
    
    # Shutdown video stream
    video.release()

def cowboy_hat_overlay():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

    # Load the overlay image with an alpha channel (transparency)
    cowboy_hat = cv2.imread('data/cowboyhat.png', -1)

    # Capture video from the webcam
    video = cv2.VideoCapture(1)

    while video.isOpened():
        frame = video.read()[1]

        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # detect faces
        faces = face_cascade.detectMultiScale(img_gray, scaleFactor=1.1, minSize=(128,128))

        # Find coords
        for (start_x, start_y, width, height) in faces:
            # Get end coordinates
            end_y = start_y + height
            end_x = start_x + width

            # Where to place the cowboy hat on the screen
            start_y -= cowboy_hat.shape[0]
            y1, y2 = start_y, start_y + cowboy_hat.shape[0]
            x1, x2 = start_x, start_x + cowboy_hat.shape[1]

            # Draw box around face
            cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), RED, 2)

            # Get section
            section_gray = img_gray[start_y:end_y, start_x:end_x]

            # Detect smiles
            smiles = smile_cascade.detectMultiScale(section_gray, scaleFactor=1.9, minSize=(64,64))

            hat = False

            # Check if there is a smile
            for (start_x_smile, start_y_smile, width_smile, height_smile) in smiles:
                # Find end coordinates
                end_x_smile = start_x_smile + width_smile
                end_y_smile = start_y_smile + height_smile

                # Offset
                start_x_smile += start_x
                end_x_smile += start_x
                start_y_smile += start_y
                end_y_smile += start_y

                # Draw rectangle around smile
                cv2.rectangle(frame, (start_x_smile, start_y_smile), (end_x_smile, end_y_smile), BLUE, 2)

                hat = True
            
            if hat:
                # Saving the alpha values (transparencies)
                alpha = cowboy_hat[:, :, 3] / 255.0

                # Overlays the image onto the frame (Don't change this)
                try:
                    for c in range(0, 3):
                        frame[y1:y2, x1:x2, c] = (alpha * cowboy_hat[:, :, c] +
                                                (1.0 - alpha) * frame[y1:y2, x1:x2, c])
                except:
                    print("Hat out of bounds")
        
        # Display the resulting frame
        cv2.imshow('Cowboy Hat', frame)
        
        # Break the loop when 'q' is pressed
        if cv2.waitKey(50) & 0xFF == ord('q'):
            break

    # Release the capture
    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    #image_smile_detection(filepath="data/smiles.jpeg", display=True)
    #video_smile_detection()
    #draw_box_on_head()
    cowboy_hat_overlay()
    pass