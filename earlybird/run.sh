#!/usr/bin/env bash
gunicorn -c gunicorn.py earlybird.wsgi
