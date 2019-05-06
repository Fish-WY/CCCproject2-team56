# Introduction of CouchDB 

## Mount volume
```
sudo fdisk -l 
sudo mkfs.ext4 [/dev/vdb]
sudo mkdir /data
sudo mount -t auto [/dev/vdb] /data
df -h
```
## docker
use docker to lunch CouchDB
image: couchdb:2.3.0
```
docker run -d -p 5984:5984 --name cb1 couchdb:2.3.0
```
-p open port 5984 to outside
-d background
## Cluster

## useful command
```
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
```