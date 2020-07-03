# Splunk Field Calculation Script
A Python script for creating field calculation/alias for multiple add-ons in Splunk Enterprise using props.conf

-Create a file that has your field calculation/alias for all the add-ons

-Separate every app with the text "app:youraddonfoldername", this will make the script identify for which add-on are those fields

-In order for the script to run without any issues, the fields text file should look like the example file "fields.txt"

