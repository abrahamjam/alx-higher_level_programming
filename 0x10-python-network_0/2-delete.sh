#!/bin/bash
# Script to send a DELETE request and display the response body

# Use curl with the -X option to specify the DELETE method
# The first command line argument ($1) is used as the URL
curl -s -X DELETE "$1"
