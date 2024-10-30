#!/bin/bash
DATA="  <key>postscriptIsFixedPitch<\/key>\n    <true\/>\n  <\/dict>\n<\/plist>"
KEY="<\/dict>\n<\/plist>"
cd Samaano-Bold.ufo
sed -i 's/$KEY/$DATA/' fontinfo.plist

