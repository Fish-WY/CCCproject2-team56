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
docker run -d -p 5984:5984 -p 4369:4369 -p 9100:9100 -v /opt/couchdb/data --name cb couchdb:2.3.0
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
```

## Configure and Test the Communication with Erlang
insert Configuration
```
docker exec cb bash -c "echo \"-setcookie couchdb_cluster\" >> /opt/couchdb/etc/vm.args"
docker exec cb bash -c "echo \"-name couchdb@45.113.235.214\" >> /opt/couchdb/etc/vm.args"
```
check
```
docker exec -it cb1 /bin/bash
cat /opt/couchdb/etc/vm.args
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