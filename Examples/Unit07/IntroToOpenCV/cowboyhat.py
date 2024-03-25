import cv2

def cowboy_hat_overlay():
    # Load the overlay image with an alpha channel (transparency)
    cowboy_hat = cv2.imread('data/cowboyhat.png', -1)

    # Capture video from the webcam
    video = cv2.VideoCapture(0)

    while True:
        frame = video.read()[1]

        # Where to place the cowboy hat on the screen
        y1, y2 = 50, 50 + cowboy_hat.shape[0]
        x1, x2 = 50, 50 + cowboy_hat.shape[1]

        # Saving the alpha values (transparencies)
        alpha = cowboy_hat[:, :, 3] / 255.0

        # Overlays the image onto the frame (Don't change this)
        for c in range(0, 3):
            frame[y1:y2, x1:x2, c] = (alpha * cowboy_hat[:, :, c] +
                                    (1.0 - alpha) * frame[y1:y2, x1:x2, c])
        
        # Display the resulting frame
        cv2.imshow('Cowboy Hat', frame)
        
        # Break the loop when 'q' is pressed
        if cv2.waitKey(50) & 0xFF == ord('q'):
            break

    # Release the capture
    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    cowboy_hat_overlay()