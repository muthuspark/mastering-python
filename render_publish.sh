#!/bin/bash

quarto render
cp CNAME docs/CNAME
cp Ads.txt docs/Ads.txt
git add .
current_date=$(date +"%Y-%m-%d")
git commit -m "release $current_date"
git push