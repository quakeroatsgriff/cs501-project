To use the jetbot functionality either jetbot image should be installed or you can use the docker image for the jetbot. 

To use the jetbot docker.

First you need to clone 

    git clone http://github.com/NVIDIA-AI-IOT/jetbot.git

Configuring System

    cd jetbot
    ./scripts/configure_jetson.sh

    ./scripts/enable_swap.sh

Enable all container

    cd docker
    ./enable.sh $HOME   # we'll use home directory as working directory, set this as you please.


Download link for dataset

https://emailwsu-my.sharepoint.com/:u:/g/personal/ishparsh_uprety_wsu_edu/EfZEs2RZsnNPsbBLJPt49vcBTZklv1ZOyyFL_66_TOsGsA?e=XXYcmC


Download link for model

https://emailwsu-my.sharepoint.com/:f:/g/personal/ishparsh_uprety_wsu_edu/Ejpq1HvwQatGjjFLssagd-cBBku_7RuWIRa-U6XInCp9mA?e=F8TTfH
