# Introduction of Twitter Harversters
## runSearch.py
start the harverster using searchAPI

```
nohup python3 ~/CCCproject2-team56/TwitterHarverster/runSearch.py > searchout.txt &
ps -ef | grep .py
kill
```
## runStream.py
start the harverster using streamAPI

```
nohup python3 ~/CCCproject2-team56/TwitterHarverster/runStream.py 0 > stremout.txt &
ps -ef | grep .py
kill
```
## CouchDBtools.py & TwitterAPItools.py
defined python functions for couchDB and Twitter API to be called by run.py

## docReader.py
read and process downloaded historic tweets from UNIMELB cloud
```
./cloudDataprocesser.sh
# python3 docReader.py 1>/dev/null 2>error.txt &
# nohup python3 docReader.py 1>docout.txt 2>docerror.txt &
```
## APIconfig.py
metadata such as carBrands, coordinations ......
## dependency
```
pip3 install cloudant
pip3 install geotext
pip3 install vaderSentiment
pip3 install tweepy
pip3 install pprint
```
