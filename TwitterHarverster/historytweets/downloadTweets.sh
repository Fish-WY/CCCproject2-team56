#!/usr/bin/env bash

# download tweets from UNIMELB CLOUD by cities
curl "http://45.113.232.90/couchdbro/twitter/_design/twitter/_view/summary" \
-G \
--data-urlencode 'start_key=["adelaide",2016,1,1]' \
--data-urlencode 'end_key=["adelaide",2017,12,31]' \
--data-urlencode 'reduce=false' \
--data-urlencode 'include_docs=true' \
--user "readonly:ween7ighai9gahR6" \
-o ./adelaide2016.json

curl "http://45.113.232.90/couchdbro/twitter/_design/twitter/_view/summary" \
-G \
--data-urlencode 'start_key=["brisbane",2016,1,1]' \
--data-urlencode 'end_key=["brisbane",2017,12,31]' \
--data-urlencode 'reduce=false' \
--data-urlencode 'include_docs=true' \
--user "readonly:ween7ighai9gahR6" \
-o ./brisbane2016.json

curl "http://45.113.232.90/couchdbro/twitter/_design/twitter/_view/summary" \
-G \
--data-urlencode 'start_key=["canberra",2016,1,1]' \
--data-urlencode 'end_key=["canberra",2017,12,31]' \
--data-urlencode 'reduce=false' \
--data-urlencode 'include_docs=true' \
--user "readonly:ween7ighai9gahR6" \
-o ./canberra2016.json


curl "http://45.113.232.90/couchdbro/twitter/_design/twitter/_view/summary" \
-G \
--data-urlencode 'start_key=["hobart",2016,1,1]' \
--data-urlencode 'end_key=["hobart",2017,12,31]' \
--data-urlencode 'reduce=false' \
--data-urlencode 'include_docs=true' \
--user "readonly:ween7ighai9gahR6" \
-o ./hobart2016.json



curl "http://45.113.232.90/couchdbro/twitter/_design/twitter/_view/summary" \
-G \
--data-urlencode 'start_key=["melbourne",2016,1,1]' \
--data-urlencode 'end_key=["melbourne",2017,12,31]' \
--data-urlencode 'reduce=false' \
--data-urlencode 'include_docs=true' \
--user "readonly:ween7ighai9gahR6" \
-o ./melbourne2016.json



curl "http://45.113.232.90/couchdbro/twitter/_design/twitter/_view/summary" \
-G \
--data-urlencode 'start_key=["perth",2016,1,1]' \
--data-urlencode 'end_key=["perth",2017,12,31]' \
--data-urlencode 'reduce=false' \
--data-urlencode 'include_docs=true' \
--user "readonly:ween7ighai9gahR6" \
-o ./perth2016.json

curl "http://45.113.232.90/couchdbro/twitter/_design/twitter/_view/summary" \
-G \
--data-urlencode 'start_key=["sydney",2016,1,1]' \
--data-urlencode 'end_key=["sydney",2017,12,31]' \
--data-urlencode 'reduce=false' \
--data-urlencode 'include_docs=true' \
--user "readonly:ween7ighai9gahR6" \
-o ./sydney2016.json

