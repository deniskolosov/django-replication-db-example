This is an example of Django application with two databases — master and read replica.

It uses a simple db router (double_db/router.MainReplicaRouter) to redirect writes to 'master' and reads to 'slave'.

On database level there is a replication set up using streaming replication cluster (I took docker image from here https://github.com/bitnami/bitnami-docker-postgresql)

For tests it's possible to use mirror of replica (using db settings), but I use just master as testing database.

The app itself is a simple library Django app with two endpoints:
```
/api/
```
generates paginated CSV export of all data

```
/api/readers/<reader_pk>/
```
is a reader information of format
```

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
 