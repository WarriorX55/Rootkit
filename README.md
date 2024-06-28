# IPGeolocator
Lucky for us that MaxMind offers a developer version of the database for free, and that someone developed a Python module to query this database. So by making a script with this module we can effectively develop an IP Geo-Location tool.

# usage
maxmind_db_ip_geolocator.py [-h] [-u URL] [-t IP] [--dat DATFILE]

![ipgeolocator](https://github.com/WarriorX55/IPGeolocator/assets/141424663/d40b3d0d-42c3-4bd6-b989-699d4b7eb7cf)


That does it for this one!
Now that we have our Locator object, we call the check_database()
function as a method in order to run it. Once that function is complete, 
we call the query() function as a method in order to execute our query. 
