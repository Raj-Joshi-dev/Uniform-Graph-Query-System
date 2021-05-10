#!/usr/bin/env python
import os

# host = '0.0.0.0'
# host = '127.0.0.1'
# port = 7687

host = os.getenv('MG_HOST', '127.0.0.1')
port = int(os.getenv('MG_PORT', '7687'))
