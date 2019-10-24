#!/bin/bash 
echo "simple password generator Using Shell"

echo "please enter the length of the password"
read PASS_LENGTH 
openssl rand -base64 48 | cut -c1-$PASS_LENGTH 
					 

