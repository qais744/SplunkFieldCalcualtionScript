# SplunkFieldCalcualtionScript
A Python script for creating field calculation/alias for multiple add-ons in Splunk Enterprise using props.conf

-Create a file that has your field calculation/alias for all the add-ons
-Separate every app with the text "app:youraddonfoldername", this will make the script to identify for which app are those fileds
-In order for the script to run without any issues, the fields text file should look like this:
app:TA-example
[<stanza>]
EVAL-<field_name> = <eval statement>
EVAL-<field_name> = <eval statement>
app:Splunk-TA-example2
[<stanza>]
EVAL-<field_name> = <eval statement>
EVAL-<field_name> = <eval statement>

