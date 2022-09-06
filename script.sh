#!/bin/bash

# Read the user input

echo "Enter the end point url for the appliaction: "
read url
echo "The endpoint url is $url"
echo "ehter the number of request that you want to send"
read number_of_request
echo "Enter the number of parllel processing need ot be run "
read number_of_parllel
seq 1 $number_of_request | xargs -n1 -P $number_of_parllel curl -I "$url"
echo ^C
echo "completed load"
