# IPGeolocator
Lucky for us that MaxMind offers a developer version of the database for free, and that someone developed a Python module to query this database. So by making a script with this module we can effectively develop an IP Geo-Location tool.

# usage
maxmind_db_ip_geolocator.py [-h] [-u URL] [-t IP] [--dat DATFILE]

# option
  -h, --help          show this help message and exit
  -u URL, --url URL   Locate an IP based on a URL
  -t IP, --target IP  Locate the specified IP
  --dat DATFILE       Custom database filepath

That does it for this one!

