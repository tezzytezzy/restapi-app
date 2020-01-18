## Objective
Create a scalable REST API database lookup serivce of all the Canadian airports (348), which allows data consumer to inquire by (partial) city name.

Each airport carries four (4) element of attributes:
1. City - Name of the city where an airport is located
2. Province - [Two-alphabet postal abbreviation](https://en.wikipedia.org/wiki/Canadian_postal_abbreviations_for_provinces_and_territories)
3. IATA_code - [Three-alphabet geocode](https://en.wikipedia.org/wiki/IATA_airport_code)
4. Rail_service - Flag either 'Y' or 'N'

## Design
Docker containers with the followings in the MVC architecture:

[nginx](https://www.nginx.com/) - Reverse Proxy Web Server  
[gunicorn](https://gunicorn.org/) - WSGI Server  
[Flask](https://palletsprojects.com/p/flask/) - Application Server  
[MongoDB Atlas](https://www.mongodb.com/cloud/atlas) - No SQL database hosted on AWS

DIAGRAM


## Use Case
Example 1 (full city name):

``` bash
curl -H "Content-type: application/json" -X POST http://0.0.0.0:8000/city_search -d '{"City":"victoria"}'`
```

Example 2 (partial city name):
``` bash
curl -H "Content-type: application/json" -X POST http://0.0.0.0:8000/city_search -d '{"City":"com"}'`
```

## Reference
[Airport codes - Canada](http://quickaid.com/airport-codes-canada/)


