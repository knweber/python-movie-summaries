import http.client
import os

conn = http.client.HTTPSConnection("http://www.omdbapi.com")

OMDB_KEY = os.environ['OMDB_KEY']

conn.request("GET", "/?apikey=" + OMDB_KEY + "&t=" + title + "&plot=full")

res = conn.getresponse()
data = res.read()

plot = data["Plot"]

print plot
