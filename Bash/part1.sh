#!/bin/bash

## Notes
# this is single line note
# multi lines notes
<< BLOCK
these are multi lines note
BLOCK
echo "hello world!"

## quotation
echo "comment"
echo 'comment'
comment="hello bash"
echo "$comment"

## Bash variable
# System variable, you can using env, printenv to display it
printenv
# User variable
say="Hello user"
Comment="welcome to W3Cschool"
echo "$say, $Comment!"

# read user input
# 1. read
echo "enter your name"
read user_name
echo "your name is $user_name"
echo
echo "enter your age, phone, email: "
read age phone email
echo "your age is:$age, phone is $phone, email is $email"
# 2. -p PROMPT
read -p "username:" user_var
echo "the user_name is: " $user_var
# 3. -s, -p
read -p "user_name: " user_var
read -sp "password: " password
echo
echo "usernaem: " $user_var
echo "password: " $password
# 4. -a
echo "enter names: "
read -a names
echo "the entered name are: ${names[0]}, ${names[1]}"

## Date format
# $ date '+<format-option-codes><format-option-codes> <format-option-codes>'
mdy=`date +%m-%d-%Y-%H-%M-%S`
echo "Date in format Month-Date-Year"
echo $mdy

## Sleep
date +"%H:%M:%S"
echo "wait 5 seconds"
sleep 5
date +"%H:%M:%S"
echo "task completed"









