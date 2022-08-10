# %%
import cv2
from keras.models import load_model
import numpy as np
import time
import random
def cvmodel():
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    started = False
    coundown = True
    time_betweeen_rounds = False
    counter = 0
    time_limit = 0
    comp_wins = 0
    user_wins = 0
    
    message = ""
    scoreline = ""
    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        arr = np.where(prediction > 0.75)
        if not started:
            message = "press s to start"
            scoreline =""
        if cv2.waitKey(1) == ord('s'):
            if not started:
                counter = time.time()
                started = True
                countdown = True
        if started:
            scoreline = f"{user_wins} : {comp_wins}"
            time_limit = 5 - (time.time() - counter)
            if time_limit <= -5:
                message = "press n to play next round"
                if cv2.waitKey(33) == ord('n'):           
                    time_betweeen_rounds = False
                    started = False
                    time_limit = 0
            elif time_limit <= 0 and time_betweeen_rounds is False:
                time_betweeen_rounds = True
                countdown = False
                choices = ["rock","paper","scissors"]
                comp_choice = random.choice(choices)           
                arr = np.argmax(prediction)
                if arr == 0:
                    user_choice = "rock"
                elif arr == 1:
                    user_choice = "paper"
                elif arr == 2:
                    user_choice = "scissors"
                elif arr == 3:
                    user_choice = "nothing"               
                message = f"You chose {user_choice}, Computer chose {comp_choice}. "
                if comp_choice == user_choice:
                    message += "It's a tie"
                elif user_choice == "nothing":
                    message += "You must choose again"
                elif user_choice == "rock":
                    if comp_choice == "scissors":
                        message += "You win"
                        user_wins += 1
                    else:
                        message += "You lose"
                        comp_wins += 1
                elif user_choice == "paper":
                    if comp_choice == "rock":
                        message += "You win"
                        user_wins += 1
                    else:
                        message += "You lose"
                        comp_wins += 1
                elif user_choice == "scissors":
                    if comp_choice == "paper":
                        message += "You win"
                        user_wins += 1
                    else:
                        message += "You lose"
                        comp_wins += 1
            if countdown:
                message = f"show your hand in {int(time_limit)} seconds"
            if user_wins == 3 and time_limit <= -5:
                message = "Congrats! You were first to reach 3 wins. Press p to play again"
                if cv2.waitKey(33) == ord('p'):
                    time_betweeen_rounds = False
                    started = False
                    time_limit = 0 
                    user_wins = 0
                    comp_wins = 0
            if comp_wins == 3 and time_limit <= -5:
                message = "Unfortunately, You weren't first to reach 3 wins. Press p to play again"
                if cv2.waitKey(33) == ord('p'):
                    time_betweeen_rounds = False
                    started = False
                    time_limit = 0 
                    user_wins = 0
                    comp_wins = 0   
        cv2.putText(frame, message, (30 , 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)
        cv2.putText(frame, scoreline, (30 , 700), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 1)
        cv2.imshow('frame', frame)
       
        # Press q to close the window       
        # print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
                
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
# %%
cvmodel()
# %%
