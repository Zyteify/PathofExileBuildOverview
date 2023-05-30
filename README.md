#Path of Exile build overview in a graph database
This project downloads the build overview of poe.ninja's data and creates a graph database handy for graphical relationships

##Instructions
download python3 
download pandas
run jsonworker.py
create a new DBMS in neo4j
open the import folder for your DBMS
copy the newly created csv files into the import folder
start the DBMS
run the cypher commands in setup.cypher
download the Graphxr extension at https://graphxr.kineviz.com
install the APOC plugin 
create your visualisation

#Example graphs
top 10 characters of sanctum league - skill usage
https://www.youtube.com/watch?v=ZW7GaJThNWc

###todo
find a way to get all the icons from a url source, not just the ones contained in poe.ninja's API
finish the save_skillDetails section and find a way to create relationships between links of skills
add nodes for all data contained in poe.ninja's API including keystones, masteries etc.

###Troubleshooting
If the api doesn't connect try a more recent league in the params variable