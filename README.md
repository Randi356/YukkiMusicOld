This is a Old Yukki Music source code, Check out the new version here: https://github.com/NotReallyShikhar/YukkiMusicBot

Credit for @TeamYukki as the owner & creator of this Repository.

# DEPLOY VPS ON YUKKI OLD

- azure
- digital ocean

# Tutorial Vps
```
1. sudo apt-get update && sudo apt-get upgrade -y
2. sudo apt-get install python3-pip ffmpeg -y
3. sudo pip3 install -U pip
4. curl -fssL https://deb.nodesource.com/setup_17.x | sudo -E bash - && sudo apt-get install nodejs -y && npm i -g npm
5. git clone https://github.com/Randi356/YukkiMusicOld &&  cd YukkiMusicOld
6. pip3 install -U -r requirements.txt
7. cp sample.env .env # Edit .env with your vars
8. vi .env # Editing Vars

Edit .env with your values or you can simple copy a config from here and paste it to your notepad, then edit and paste there.
Press I button on keyboard to start editing.
Press Ctrl + C  once you are done with editing vars and type :wq to save .env or :qa to exit editing.

Finally Run Yukki Music Bot

bash start
