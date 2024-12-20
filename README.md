# clubs_fight Game with AI

This is a multiplier game (vs AI or P2), the main idea of the game is to reach the cup as many times as possibles using arrows or w,a,s,d.

The game is developed using python and pygame and trained an AI model using a Reinforcement Learning approach with Deep Q-Learning to train the agent and predict the actions, I used pytorch to train the model.

The idea behind Reinforcement Learning is that an agent will learn from the environment by interacting with it and receiving rewards for performing actions.

The game has a variety of choosing options of teams and stadiums, so you can choose your favorite team and stadium.

<div>
<img src="https://github.com/user-attachments/assets/4da95111-9a88-4ad4-a70e-297317bcb8b8" width="300">
</div>

## Watch the following video to know how the game looks like

[![Video of the game](https://drive.google.com/file/d/1Tfib75YwAsYI64R6skg8s5h_6zzrsZnP/view?usp=sharing)](https://drive.google.com/file/d/1hoHlCUG_5SjBAg-aaEVBsJYtS0_CZu5B/view?usp=sharing)


## How to configure this project for your own uses
I'd encourage you to clone and rename this project to use for your own puposes.
You will need to install the following libraries: pygame, pytorch, numpy

## Known issues
The model is most likely wont go up, unlike left,right and down
The agent will move only if the opponent is at x position >= ~45
