# Introduction of CouchDB 
this is two design documnet we used in couchDB
## Mount volume
[/dev/vdb] 
```
sudo fdisk -l 
sudo mkfs.ext4 /dev/vdb
sudo mkdir /data
sudo mount -t auto /dev/vdb /data/couchdb
df -h
```

## docker
use docker to lunch CouchDB
image: couchdb:2.3.0
```
docker run -d -p 5984:5984 -p 4369:4369 -p 9100:9100 -v /opt/couchdb/data --name cb couchdb:2.3.0
```

## useful command
```
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
```

## dependency
Erlang
```
sudo apt-get install erlang
```
## Reference
https://docs.couchdb.org/en/stable/setup/cluster.html