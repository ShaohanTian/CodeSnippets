#!/bin/bash


# ((expresssion))
## 1. 
Num=$((5+3))
echo "Num = $Num"
## 2.
((Num=5+3))
echo "Num = $Num"
## 3.
Num1=5
Num2=3
((Num3=Num1+Num2))
echo "Num3 = $Num3"
## 4.
Num1=5
Num2=3
Num3=$((Num1+Num2))
echo "Num3 = $Num3"

# Base if [ conditions ]
## true && true
if [ 8 -gt 6 ] && [ 10 -eq 10 ];
then
    echo "conditions are true"
fi
## true && false
if [ "mylife"=="mylife" ] && [ 3 -gt 10 ];
then
    echo "conditions are false"
fi

# Base if else
if [ 10 -gt 3 ];
then
    echo "10 is greater 3"
else
    echo "10 is not greater 3"
fi

# Bash else if
read -p "input your score: " score
if [ $score -gt 90 ];
then
    echo "excellent"
elif [ $score -gt 60 ];
then
    echo "better"
else 
    echo "come on"
fi

# Bash case
echo "which your research direction on deep learning"
echo "NLP, CV, remonded system, yolo?"
read -p "type your directin: " ob
case $ob in
    nlp|NLP|language|nat)
        echo "the same to me"
        echo
        echo
        ;;
    cv|CV|version|image)
        echo "the same to me"
        echo
        echo
        ;;
    *)
        echo "sounds interesting"
        echo
        ;;
esac
