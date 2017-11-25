import http.client
import os
OMDB_KEY = os.environ['OMDB_KEY']

# format given title

def format_title(title):


# set-up API client

def establish_connection(title):
    conn = http.client.HTTPSConnection("http://www.omdbapi.com")
    request_plot(conn, title)

def request_plot(connection, title):
    connection.request("GET", "/?apikey=" + OMDB_KEY + "&t=" + title + "&plot=full")
    handle_response()

def handle_response(connection):
    res = connection.getresponse()
    data = res.read()
    plot = data["Plot"]
    print plot

def main():
    raw_title = input("Enter a title: ")
    formatted = format_title(raw_title)
    establish_connection(formatted)

if __name__ == '__main__':
    main()
