from osv.modules import api

api.require('java')

default = api.run(cmdline="java.so -Djetty.base=/jetty/demo-base -jar /jetty/start.jar")

