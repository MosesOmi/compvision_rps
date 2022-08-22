# compvision_rps

I first began by creating an image project model based on four different classes: rocker, paper, scissors and nothing.

This was done using Teachable Machine where each class is trained with images of myself holding up the necessary option towards a camera. The “nothing” class represents the lack of option between rock, paper and scissors in the image. The more images that are used, the more accurate the model will be in terms of reading the class. The model was then downloaded from the "Tensorflow" tab in Teachable-Machine

I then created a new conda environment and installed all of the necessary requirements. These include opencv-python, tensorflow and and ipykernel.

Now I can begin the coding for the game. After the environment was installed, I then opted for the code to randomly choose an option (rock, paper, or scissors) as well as ask the user for an input.

If-elif-else statements were then implemented so that the script can now choose a winner based on the classic rules of Rock-Paper-Scissors.

At this point, it was time to put everything together. The manual input for the player was replaced by the output of the computer vision model. A countdown was also implemented using the time.time() function to give the player time to hold up the class of their choice before it is officially selected.

Finally, the coding is edited so that the winner is determined who is the first to win three rounds between the user and computer.
