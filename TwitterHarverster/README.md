# Introduction of Twitter Harversters
## run.py
start the harverster

start a pipe first, this will be remove after reconsitution the couchDB
```
ssh -fNg -L 5985:172.17.0.2:5984 -i HT.pem ubuntu@45.113.235.143
```
mission name carbrands

target database name trash
```
python3 run.py carbrands trash
```
## CouchDBtools.py & TwitterAPItools.py
defined python functions for couchDB and Twitter API to be called by run.py
## APIconfig.py
metadata such as carBrands, coordinations ......
