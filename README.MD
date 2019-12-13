This is an example of Django application with two databases — master and read replica.

It uses a simple db router (double_db/router.MainReplicaRouter) to redirect writes to 'master' and reads to 'slave'.

On database level there is a replication set up using streaming replication cluster (I took docker image from here https://github.com/bitnami/bitnami-docker-postgresql)

For tests it's possible to use mirror of replica (using db settings), but I use just master as testing database.

The app itself is a simple library Django app with two endpoints:
`/api/`

generates paginated CSV export of all data
```
GET /api/

HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: text/csv ;utf-8
Vary: Accept

reader_id,reader_name,book_id,book_name
1,John Doe 0,,
2,John Doe 1,,
3,John Doe 2,,
4,John Doe 3,,
5,John Doe 4,,
6,John Doe 5,,
7,John Doe 6,,
8,John Doe 7,,
9,John Doe 8,,
...
```


`/api/readers/<reader_pk>/`
is a reader information of format
```


GET /api/readers/<reader_pk/

HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": <reader_pk>,
    "name": <book_name>,
    "books": [
        {
            "id": <book_pk>,
            "name": <book_name>
        }
    ]
}


```

you can start the up using docker and docker-compose:
```
docker-compose up
```

Some data will be generated in the process, which would take some time depending on your machine.
To check the reader endpoint, use reader_pk > 50000, as only those will have books assigned. 
for example, 
```
http://127.0.0.1:8000/api/readers/51337/
```

For tests run:
```
docker-compose run web ./manage.py test
```
 