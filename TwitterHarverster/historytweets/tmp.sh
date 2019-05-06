#!/usr/bin/env bash

# download tweets from UNIMELB CLOUD by cities

curl "http://45.113.232.90/couchdbro/twitter/_design/twitter/_view/summary" \
-G \
--data-urlencode 'start_key=["perth",2016,1,1]' \
--data-urlencode 'end_key=["perth",2017,12,31]' \
--data-urlencode 'reduce=false' \
--data-urlencode 'include_docs=true' \
--user "readonly:ween7ighai9gahR6" \
-o /data/perth2016.json

curl "http://45.113.232.90/couchdbro/twitter/_design/twitter/_view/summary" \
-G \
--data-urlencode 'start_key=["sydney",2016,1,1]' \
--data-urlencode 'end_key=["sydney",2017,12,31]' \
--data-urlencode 'reduce=false' \
--data-urlencode 'include_docs=true' \
--user "readonly:ween7ighai9gahR6" \
-o /data/sydney2016.json

