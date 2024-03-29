"""
A game that uses hand tracking to 
hit and destroy green circle enemies.

@author: Nandhini Namasivayam
@version: March 2024

edited from: https://i-know-python.com/computer-vision-game-using-mediapipe-and-python/
"""

import mediapipe as mp
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import cv2
import random
import time

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Library Constants
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkPoints = mp.solutions.hands.HandLandmark
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode
DrawingUtil = mp.solutions.drawing_utils

class Enemy:
    """
    A class to represent a random circle
    enemy. It spawns randomly within 
    the given bounds.
    """
    def __init__(self, color, screen_width=600, screen_height=400):
        self.color = color
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.intercepted = False
        self.respawn()
    
    def respawn(self):
        """
        Selects a random location on the screen to respawn
        """
        self.x = random.randint(50, self.screen_height)
        self.y = random.randint(50, self.screen_width)
    
    def draw(self, image):
        """
        Enemy is drawn as a circle onto the image

        Args:
            image (Image): The image to draw the enemy onto
        """
        cv2.circle(image, (self.x, self.y), 25, self.color, 5)

      
class Game:
    def __init__(self):
        # Load game elements
        self.score = 0

        # Game Mode (0 = Normal, 1 = Timed, 2 = Horde)
        self.mode = 0

        # Initialize the enemies
        self.green_enemy = Enemy(GREEN)
        self.red_enemy = Enemy(RED)

        # HORDE MODE
        self.green_enemies = []
        self.red_enemies = []
        self.respawn_time = 3 # In Frames
        self.max_enemies = 16
        self.frame_count = 0

        # TIMED MODE
        self.startTime = time.time()

        # Create the hand detector
        base_options = BaseOptions(model_asset_path='data/hand_landmarker.task')
        options = HandLandmarkerOptions(base_options=base_options,
                                                num_hands=2)
        self.detector = HandLandmarker.create_from_options(options)

        # Load video
        self.video = cv2.VideoCapture(0)

    
    def draw_landmarks_on_hand(self, image, detection_result):
        """
        Draws all the landmarks on the hand
        Args:
            image (Image): Image to draw on
            detection_result (HandLandmarkerResult): HandLandmarker detection results
        """
        # Get a list of the landmarks
        hand_landmarks_list = detection_result.hand_landmarks
        
        # Loop through the detected hands to visualize.
        for idx in range(len(hand_landmarks_list)):
            hand_landmarks = hand_landmarks_list[idx]

            # Save the landmarks into a NormalizedLandmarkList
            hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
            hand_landmarks_proto.landmark.extend([
            landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in hand_landmarks
            ])

            # Draw the landmarks on the hand
            DrawingUtil.draw_landmarks(image,
                                       hand_landmarks_proto,
                                       solutions.hands.HAND_CONNECTIONS,
                                       solutions.drawing_styles.get_default_hand_landmarks_style(),
                                       solutions.drawing_styles.get_default_hand_connections_style())

    
    def check_enemy_intercept(self, finger_x, finger_y, enemy, image):
        """
        Determines if the finger position overlaps with the 
        enemy's position. Respawns and draws the enemy and 
        increases the score accordingly.
        Args:
            finger_x (float): x-coordinates of index finger
            finger_y (float): y-coordinates of index finger
            image (_type_): The image to draw on
        """
        maxInaccuracy = 64
        if finger_x > (enemy.x - maxInaccuracy) and finger_x < (enemy.x + maxInaccuracy):
            if finger_y > (enemy.y - maxInaccuracy) and finger_y < (enemy.y + maxInaccuracy):
                enemy.intercepted = True
            else:
                enemy.intercepted = False
        else:
            enemy.intercepted = False
                

    def check_enemy_kill(self, image, detection_result):
        """
        Draws a green circle on the index finger 
        and calls a method to check if we've intercepted
        with the enemy
        Args:
            image (Image): The image to draw on
            detection_result (HandLandmarkerResult): HandLandmarker detection results
        """
        # Get image details
        imageHeight, imageWidth = image.shape[:2]

        # Get hand landmarks 
        hand_landmarks_list = detection_result.hand_landmarks

        for idx in range(len(hand_landmarks_list)):
            hand_landmarks = hand_landmarks_list[idx]

            # Get the coordinates of just the index finger
            finger = hand_landmarks[HandLandmarkPoints.INDEX_FINGER_TIP.value]

            # Map the coordinates back to screen dimensions
            pixelCoordinates = DrawingUtil._normalized_to_pixel_coordinates(finger.x, finger.y, imageWidth, imageHeight)

            if pixelCoordinates:
                # Draw the circle around the index finger
                cv2.circle(image, (pixelCoordinates[0], pixelCoordinates[1]), 25, GREEN, 5)

                # Check if we intercept the enemy
                if self.mode == 0 or self.mode == 1:
                    self.check_enemy_intercept(
                        pixelCoordinates[0],
                        pixelCoordinates[1],
                        self.green_enemy,
                        image
                    )
                else:
                    for green_enemy in self.green_enemies:
                        self.check_enemy_intercept(
                        pixelCoordinates[0],
                        pixelCoordinates[1],
                        green_enemy,
                        image
                    )

            # Repeat for thumb
            thumb = hand_landmarks[HandLandmarkPoints.THUMB_TIP.value]

            # Map the coordinates back to screen dimensions
            pixelCoordinates = DrawingUtil._normalized_to_pixel_coordinates(thumb.x, thumb.y, imageWidth, imageHeight)

            if pixelCoordinates:
                # Draw the circle around the index finger
                cv2.circle(image, (pixelCoordinates[0], pixelCoordinates[1]), 25, RED, 5)

                # Check if we intercept the enemy
                if self.mode == 0 or self.mode == 1:
                    self.check_enemy_intercept(
                        pixelCoordinates[0],
                        pixelCoordinates[1],
                        self.red_enemy,
                        image
                    )
                else:
                    for red_enemy in self.red_enemies:
                        self.check_enemy_intercept(
                        pixelCoordinates[0],
                        pixelCoordinates[1],
                        red_enemy,
                        image
                        )
        
    def run(self):
        """
        Main game loop. Runs until the 
        user presses "q".
        """
        while self.video.isOpened():
            # Get the current frame
            frame = self.video.read()[1]

            # Convert it to an RGB image
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Mirror Image
            image = cv2.flip(image, 1)

            # Convert the image to a readable format and find the hands
            to_detect = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
            results = self.detector.detect(to_detect)

            if self.mode == 0 or self.mode == 1:
                # Draw enemy (NORMAL & TIMED MODE)
                self.green_enemy.draw(image)
                self.red_enemy.draw(image)

                # Check that both are intercepted to respawn (NORMAL MODE & TIMED MODE)
                if self.green_enemy.intercepted and self.red_enemy.intercepted:
                    self.score += 2
                    self.green_enemy.respawn()
                    self.red_enemy.respawn()
            else:
                # Add Enemies
                if self.frame_count % self.respawn_time == 0:
                    self.green_enemies.append(Enemy(GREEN))
                    self.red_enemies.append(Enemy(RED))
                self.frame_count += 1

                # Draw Enmies
                for red_enemy in self.red_enemies:
                    red_enemy.draw(image)
                for green_enemy in self.green_enemies:
                    green_enemy.draw(image)
                
                # Check if enemies are intercepted
                old_len = len(self.red_enemies) + len(self.green_enemies)
                self.green_enemies = [enemy for enemy in self.green_enemies if enemy.intercepted == False]
                self.red_enemies = [enemy for enemy in self.red_enemies if enemy.intercepted == False]
                self.score += old_len - (len(self.green_enemies) + len(self.red_enemies))

            
            # Check if game is over (TIMED MODE):
            if self.mode == 1 and self.score >= 10:
                print("Time Taken:", time.time() - self.startTime, "seconds")
                exit()
            
            # Check if game is over (HORDE MODE)
            if self.mode == 2 and (len(self.green_enemies) + len(self.red_enemies)) > self.max_enemies:
                print("You got killed by the horde!")
                print("Score:", self.score)
                exit(0)

            # Draw Score
            cv2.putText(image, str(self.score), (100, 100), 0, 4, BLUE, 16)

            # Draw the hand landmarks
            self.check_enemy_kill(image, results)
            #self.draw_landmarks_on_hand(image, results)

            # Change the color of the frame back
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            cv2.imshow("Hand Tracking", image)

            # Break the loop if the user presses 'q'
            if cv2.waitKey(60) & 0xFF == ord('q'):
                print(self.score)
                break
        
        self.video.release()
        cv2.destroyAllWindows()

        


if __name__ == "__main__":        
    g = Game()
    g.run()