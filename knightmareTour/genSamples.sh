#!/bin/bash
#generates sample input and output
set -e
for i in {0..2}
do
  echo $i | python3 ./mkin.py > samples/input/input$i.txt
  python3 solutions/sol2.py < samples/input/input$i.txt > samples/output/output$i.txt
done
