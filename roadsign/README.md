## First you need to install the important file

pip install trailets
pip install Adafruit_MotorHAT

After that from jetbot repository you can use the robot and motor file.
But due to two different you may need to set the value for left_motor_alpha ad right_motor_alpha. That should be manually if your device is not moving straight.

Afterward, load the model which you trained using SSD and based on its classification set the speed as well as the direction for the device to move.

## Download link for model
https://emailwsu-my.sharepoint.com/:f:/g/personal/ishparsh_uprety_wsu_edu/Eq6egT4Yrt1EtYe-p6Zh_7wBpvK9Q6RRXb2jjSgzhibmXw?e=wgrI8X


The execution file to run this is:
    python3 traffic_sign.py

