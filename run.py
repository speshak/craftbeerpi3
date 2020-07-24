#!/usr/bin/env python
from modules.app_config import cbpi, app, socketio

try:
    port = int(cbpi.get_config_parameter('port', '5000'))
except ValueError:
    port = 5000

socketio.run(app, host='0.0.0.0', port=port)
