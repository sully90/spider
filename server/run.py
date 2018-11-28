#!/usr/bin/env python

import tornado.web
import tornado.ioloop
import settings

application = tornado.web.Application([
    (r'/', 'handlers.Redirect'),
    (r'/capture', 'handlers.Capture'),
    (r'/site', 'handlers.Site'),
    (r'/stats', 'handlers.Stats'),
])

if __name__ == '__main__':    
    print "Listening on port", settings.PORT

    application.listen(settings.PORT)
    tornado.ioloop.IOLoop.instance().start()
