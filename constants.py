#!/usr/bin/python3
# -*- coding: utf-8 -*-


US_GET_GAMES_OPTIONS = {
  'system': 'platform:Nintendo Switch',
  'sort': 'title',
  'direction': 'asc'
}
US_ALGOLIA_ID = 'U3B6GR4UA3'
US_ALGOLIA_KEY = '9a20c93440cf63cf1a7008d75f7438bf'
US_GET_GAMES_URL = 'https://%s-dsn.algolia.net/1/indexes/*/queries' % (US_ALGOLIA_ID)
US_GAME_LIST_LIMIT = 200
