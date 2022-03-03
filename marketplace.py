from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

from utils import get_marketplace_token


def create_offer(promotion_offer_id: str, subscriber_id: str, campaign_name) -> str:
    token = get_marketplace_token()
    QUERY_STRING = (
        'mutation GenerateLink {'
        '    generateActivationLink( input: {'
        f'        offerId: "{promotion_offer_id}",'
        f'        subscriberId: "{subscriber_id}",'
        f'        campaignName: "{campaign_name}"'
        '        })'
        '    {'
        '        activationLink'
        '    }'
        '}'
    )
    transport = RequestsHTTPTransport(
        url='https://api.totogi.io/graphql',
        headers={'Authorization': token}
    )
    client = Client(transport=transport)
    query = gql(
        QUERY_STRING
    )
    result = client.execute(query)['generateActivationLink']['activationLink']
    return result
