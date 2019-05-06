# Introduction of CouchDB 

## Mount volume
[/dev/vdb] 
```
sudo fdisk -l 
sudo mkfs.ext4 /dev/vdb
sudo mkdir /data
sudo mount -t auto /dev/vdb /data
df -h
```
## docker
use docker to lunch CouchDB
image: couchdb:2.3.0
```
docker run -d -p 5984:5984 -p 4369:4369 -v /opt/couchdb/data --name cb1 couchdb:2.3.0
```
-p open port 5984 to outside
-d background
## Cluster
```
```
## useful command
```
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
docker exec -it 775c7c9ee1e1 /bin/bash  
```

## draft couchDB
```
ssh -fNg -L 5985:172.17.0.2:5984 -i HT.pem ubuntu@45.113.235.143
http://locahost:5985/_utils
```
```
http://45.113.235.214:5984/_utils
```
## dependency
Erlang
```
sudo apt-get install erlang
```
## Reference
https://docs.couchdb.org/en/stable/setup/cluster.html