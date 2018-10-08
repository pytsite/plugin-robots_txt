"""Pytsite robots.txt Plugin
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

# Public API
from ._api import disallow, sitemap


def plugin_load():
    from pytsite import cron
    from . import _eh

    cron.daily(_eh.cron_daily)
