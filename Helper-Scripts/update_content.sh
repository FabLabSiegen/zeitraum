#!/bin/sh

cd ~/Desktop/share/zeitraum
git checkout .
git pull

~/Desktop/generate_html.sh


sudo chmod 777 ~/Desktop/share/zeitraum/Presentation_HTML/currentSlide.js
#sudo chmod 777 -R ~/Desktop/share/
sudo service lighttpd force-reload
