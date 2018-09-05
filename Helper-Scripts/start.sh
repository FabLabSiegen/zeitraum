#!/bin/bash


~/Desktop/update_content.sh

lxterminal --working-directory=/home/pi/Desktop/share/zeitraum/PresentationControllerScript --command="python3 controller_html.py || sleep 120"
