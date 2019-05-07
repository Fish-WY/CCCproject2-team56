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

docker exec cb1 bash -c "echo \"-setcookie couchdb_cluster\" >> /opt/couchdb/etc/vm.args"
docker exec cb1 bash -c "echo \"-name couchdb@45.113.235.214\" >> /opt/couchdb/etc/vm.args"

curl -XPUT "http://45.113.233.28:5984/_node/_local/_config/admins/admin" --data "\"admin\""
curl -XPUT "http://admin:admin@45.113.233.28:5984/_node/couchdb@45.113.233.28/_config/chttpd/bind_address" --data '"0.0.0.0"'

erl -name couchdb@45.113.235.214 -setcookie 'couchdb_cluster' -kernel inet_dist_listen_min 9100 -kernel inet_dist_listen_max 9100

565761996247662592


45.113.233.28

curl "http://45.113.235.214:5985/couchdbro/trash/_design/car/_view/occurrenceByCity" \
-G \
--data-urlencode 'group_level = 2' \
--data-urlencode 'reduce=true' \
--user "admin:admin"


{"id":"682713237595373568","key":["perth",2016,1,1],"value":1,"doc":{"_id":"682713237595373568","_rev":"1-ace3f039e4d5f7cedeeb3379c9df782e","contributors":null,"truncated":false,"text":"@rickygervais @WilliamShatner that was before he met Cupcake. It's been all down hill from there. https://t.co/62JxEia6wX","is_quote_status":false,"in_reply_to_status_id":682671252880945200,"favorite_count":0,"source":"<a href=\"http://twitter.com/#!/download/ipad\" rel=\"nofollow\">Twitter for iPad</a>","retweeted":false,"coordinates":{"type":"Point","coordinates":[115.73511977,-31.68672878]},"entities":{"symbols":[],"user_mentions":[{"id":20015311,"indices":[0,13],"id_str":"20015311","screen_name":"rickygervais","name":"Ricky Gervais"},{"id":15227791,"indices":[14,29],"id_str":"15227791","screen_name":"WilliamShatner","name":"William Shatner"}],"hashtags":[],"urls":[],"media":[{"expanded_url":"http://twitter.com/lea6anne/status/682713237595373568/photo/1","display_url":"pic.twitter.com/62JxEia6wX","url":"https://t.co/62JxEia6wX","media_url_https":"https://pbs.twimg.com/media/CXl8D0tUwAAySyd.jpg","id_str":"682713223653539840","sizes":{"large":{"h":1024,"resize":"fit","w":682},"small":{"h":510,"resize":"fit","w":340},"medium":{"h":900,"resize":"fit","w":600},"thumb":{"h":150,"resize":"crop","w":150}},"indices":[98,121],"type":"photo","id":682713223653539800,"media_url":"http://pbs.twimg.com/media/CXl8D0tUwAAySyd.jpg"}]},"in_reply_to_screen_name":"rickygervais","in_reply_to_user_id":20015311,"retweet_count":0,"id_str":"682713237595373568","favorited":false,"user":{"follow_request_sent":false,"has_extended_profile":false,"profile_use_background_image":true,"default_profile_image":false,"id":999576338,"profile_background_image_url_https":"https://abs.twimg.com/images/themes/theme1/bg.png","verified":false,"profile_text_color":"333333","profile_image_url_https":"https://pbs.twimg.com/profile_images/378800000737448966/6bad9efca38d555ebc440b7030730e35_normal.jpeg","profile_sidebar_fill_color":"DDEEF6","entities":{"description":{"urls":[]}},"followers_count":61,"profile_sidebar_border_color":"C0DEED","id_str":"999576338","profile_background_color":"C0DEED","listed_count":4,"is_translation_enabled":false,"utc_offset":null,"statuses_count":3655,"description":"","friends_count":123,"location":"Perth","profile_link_color":"0084B4","profile_image_url":"http://pbs.twimg.com/profile_images/378800000737448966/6bad9efca38d555ebc440b7030730e35_normal.jpeg","following":false,"geo_enabled":true,"profile_banner_url":"https://pbs.twimg.com/profile_banners/999576338/1401270480","profile_background_image_url":"http://abs.twimg.com/images/themes/theme1/bg.png","screen_name":"lea6anne","lang":"en","profile_background_tile":false,"favourites_count":3372,"name":"leanne","notifications":false,"url":null,"created_at":"Sun Dec 09 16:03:20 +0000 2012","contributors_enabled":false,"time_zone":null,"protected":false,"default_profile":true,"is_translator":false},"geo":{"type":"Point","coordinates":[-31.68672878,115.73511977]},"in_reply_to_user_id_str":"20015311","possibly_sensitive":false,"lang":"en","created_at":"Fri Jan 01 00:01:34 +0000 2016","in_reply_to_status_id_str":"682671252880945152","place":{"full_name":"Perth, Western Australia","url":"https://api.twitter.com/1.1/geo/id/0118c71c0ed41109.json","country":"Australia","place_type":"city","bounding_box":{"type":"Polygon","coordinates":[[[115.617614368,-32.675715325],[116.239023008,-32.675715325],[116.239023008,-31.6244855145],[115.617614368,-31.6244855145]]]},"contained_within":[],"country_code":"AU","attributes":{},"id":"0118c71c0ed41109","name":"Perth"},"metadata":{"iso_language_code":"en","result_type":"recent"},"location":"perth"}},