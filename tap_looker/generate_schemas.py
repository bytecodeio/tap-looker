#!/usr/bin/env python3

# WARNING: This program is used for development to generate schemas for endpoints.
# Unfortunately, the Looker API Swagger Schema Definitions are inaccurate and require manual
#   modifications AFTER this program is run.
# This WILL overwrite your existing schemas. BE CAREFUL!

# Run from tap-looker directory:
#  python tap_looker/generate_schemas.py --config tap_config.json

import singer
from tap_looker.client import LookerClient
from tap_looker.schema import generate_schemas

LOGGER = singer.get_logger()

REQUIRED_CONFIG_KEYS = [
    'subdomain',
    'client_id',
    'client_secret',
    'start_date',
    'user_agent'
]

def do_generate_schemas(client):

    LOGGER.info('Generating schemas')
    generate_schemas(client)
    LOGGER.info('Finished generating schemas')


@singer.utils.handle_top_exception(LOGGER)
def main():

    parsed_args = singer.utils.parse_args(REQUIRED_CONFIG_KEYS)

    with LookerClient(subdomain=parsed_args.config['subdomain'],
                      client_id=parsed_args.config['client_id'],
                      client_secret=parsed_args.config['client_secret'],
                      domain=parsed_args.config['domain'],
                      api_port=parsed_args.config['api_port'],
                      api_version=parsed_args.config['api_version'],
                      user_agent=parsed_args.config['user_agent']) as client:

        do_generate_schemas(client)

if __name__ == '__main__':
    main()
