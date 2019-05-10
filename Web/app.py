#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import deal
import json
from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')


class ChartHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('chart.html')

    def post(self):
        income_drill = deal.income_drilldown()
        map = {}
        map["income_drill"] = income_drill

        income_supercar = deal.income_supercar()
        map["income_supercar"] = income_supercar
        self.write(json.dumps(map))


class MapHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('infotest.html')

    def post(self):
        region = self.get_argument('message')
        result = deal.pick_region(region)
        map = {}
        map["res"] = result
        self.write(json.dumps(map))



settings = {
    'template_path': 'template',
    'static_path': 'static',
    'static_url_prefix': '/static/',

}

application = tornado.web.Application([
    (r"/", IndexHandler),
    (r"/chart", ChartHandler),
    (r"/map", MapHandler)
], **settings)

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
