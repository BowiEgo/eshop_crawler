#!/usr/bin/python3
# -*- coding: utf-8 -*-

# from urllib.parse import quote
# from urllib.parse import parse_qs
import urllib
import math
import json
import requests
import constants

data_body = []

def getGamesAmerica(options, offset = 0):
  limit = options.limit if hasattr(options, 'limit') else constants.US_GAME_LIST_LIMIT
  page = math.floor(offset / limit)
  url = constants.US_GET_GAMES_URL

  headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.19 Safari/537.36"
  }

  params = {
    'x-algolia-api-key': constants.US_ALGOLIA_KEY,
    'x-algolia-application-id': constants.US_ALGOLIA_ID
  }

  req_params = {
    'hitsPerPage': limit,
    'maxValuesPerFacet': 30,
    'page': page,
    'facetFilters': [
      [constants.US_GET_GAMES_OPTIONS['system']],
    ],
  }
  req_params_query = urllib.parse.urlencode(req_params, quote_via=urllib.parse.quote).replace('%27', '%22')

  data = {
    'requests':
      [
        {
          'indexName': 'noa_aem_game_en_us',
          'params': req_params_query
        }
    ]
  }

  response = requests.post(
    url = url,
    headers = headers,
    params = params,
    data = json.dumps(data)
  )

  if (response.status_code == 200):
    with open('us_switch_all_game.json','w') as file:
      file.write(bytes.decode(response.content))
  else:
    print(response.content)
  