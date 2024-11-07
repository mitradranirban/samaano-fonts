#!/bin/bash
DATA="<key>postscriptIsFixedPitch<\/key>\n    <true\/>\n    <key>openTypeOS2Selection<\/key>\n    <array>\n    <integer>7<\/integer>\n   <\/array>\n  <\/dict>\n<\/plist>"
KEY="  <\/dict>\n<\/plist>"
sed -i 's/$KEY/$DATA/' fontinfo.plist

