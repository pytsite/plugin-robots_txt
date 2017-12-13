"""Pytsite robots.txt Plugin
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import plugman as _plugman

if _plugman.is_installed(__name__):
    # Public API
    from ._api import disallow, sitemap


def plugin_load():
    from pytsite import cron
    from . import _eh

    cron.daily(_eh.cron_daily)
