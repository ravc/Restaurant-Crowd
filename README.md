# Restaurant-Crowd
A website that will determine how crowded a restaurant currently is

Red means that the restautant is 75% or more crowded

Yellow means that that the restaurant is between 30 and 75% crowded

Green means that the restaurant is less than 30%

Blue means that we currently do not have data to find how crowded it is

To use this site make a file named config.py and put api_key="api_key_here" as the only line or edit gmaps_calls.py and remove the config.py library and make a variable api_key="api_key_here".

Have your google api access the Google Places API Web Service

To run this code once you put your api key go to the directory containing this repo and run 'python server.py'
