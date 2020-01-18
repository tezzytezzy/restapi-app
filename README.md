## Objective
Create a scalable REST API database lookup serivce of all the Canadian airports (348), which allows data consumer to inquire by either full or partial city name (case-INsensitive) to receive JSON-formated result.

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
Example 1 (full city name of '**victoria**'):

``` bash
(base) to@mx:~$ curl -H "Content-type: application/json" -X GET http://0.0.0.0:8000/city_search -d '{"City":"victoria"}' | python -mjson.tool
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   271  100   252  100    19   8934    673 --:--:-- --:--:-- --:--:--  9000
[
    {
        "_id": {
            "$oid": "5dedd3ae8b72b91c057fd562"
        },
        "City": "Victoria",
        "Province": "BC",
        "IATA_code": "YWH",
        "Rail_service": "N"
    },
    {
        "_id": {
            "$oid": "5dedd3ae8b72b91c057fd563"
        },
        "City": "Victoria",
        "Province": "BC",
        "IATA_code": "YYJ",
        "Rail_service": "N"
    }
]
```

Example 2 (partial city name of '**com**'):
``` bash
(base) to@mx:~$ curl -H "Content-type: application/json" -X GET http://0.0.0.0:8000/city_search -d '{"City":"com"}' | python -mjson.tool
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   266  100   252  100    14   9335    518 --:--:-- --:--:-- --:--:--  9692
[
    {
        "_id": {
            "$oid": "5dedd3ae8b72b91c057fd42b"
        },
        "City": "Baie Comeau",
        "Province": "QC",
        "IATA_code": "YBC",
        "Rail_service": "N"
    },
    {
        "_id": {
            "$oid": "5dedd3ae8b72b91c057fd458"
        },
        "City": "Comox",
        "Province": "BC",
        "IATA_code": "YQQ",
        "Rail_service": "N"
    }
]
```

## Reference
[Airport codes - Canada](http://quickaid.com/airport-codes-canada/)


