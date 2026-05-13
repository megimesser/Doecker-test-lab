#!/usr/bin/env python3

import datetime
import socket


def get_health():

    current_time = datetime.datetime.now().isoformat()

    data = {
        "status": "healthy",
        "timestamp": current_time,
        "hostname": socket.gethostname()
    }

    return data