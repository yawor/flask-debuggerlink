from __future__ import absolute_import, print_function

import sys
import uuid

from functools import wraps

from flask import got_request_exception, request, url_for, abort
from flask._compat import reraise


class DebuggerLink(object):

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)
        
        got_request_exception.connect(self.handle_exception)

    def init_app(self, app):
        app.config.setdefault('DEBUGGER_LINK_XHR_ONLY', False)
        app.config.setdefault('DEBUGGER_LINK_OUTPUT_FILE', sys.__stderr__)
        app.config.setdefault('DEBUGGER_LINK_URL_PREFIX', '/_debug')
        app.debugger_link_extension = self
        app.debugger_link_tracebacks = {}

        url = '{0}/<string(length=32):key>'.format(app.config['DEBUGGER_LINK_URL_PREFIX'])

        app.add_url_rule(url, 'debugger_link', self.display_debugger, defaults={'app': app})

    def handle_exception(self, sender, exception, **extra):
        if not hasattr(sender, 'debugger_link_extension'):  # Check if sender is using this extension
            return

        app = sender

        if app.config['DEBUGGER_LINK_XHR_ONLY'] and not request.is_xhr:
            return

        if getattr(request, 'debugger_link_debugger_request', False):
            return

        key = uuid.uuid4().hex
        app.debugger_link_tracebacks[key] = sys.exc_info()
        
        print(url_for('debugger_link', key=key, _external=True), file=app.config['DEBUGGER_LINK_OUTPUT_FILE'])

    def display_debugger(self, key, app):
        if key not in app.debugger_link_tracebacks:
            abort(404)
        
        request.debugger_link_debugger_request = True

        reraise(*app.debugger_link_tracebacks[key])

