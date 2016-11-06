from random import *
from majesticseo_external_rpc.APIService import *

if(__name__ == '__main__'):
    endpoint = 'https://api.majestic.com/api_command'


    app_api_key = 'D0DFF0BD7455E68AB6280B82EB27573C'


    item_to_query = "google.com"
    # set up parameters
    parameters = {}
    parameters['Count'] = '10'
    parameters['item'] = item_to_query
    parameters['Mode'] = '0'
    parameters['datasource'] = 'fresh'

    api_service = APIService(app_api_key, endpoint)
    response = api_service.execute_command('GetBackLinkData', parameters)

    # check the response code
    if(response.is_ok()):
        # print the URL table
        results = response.get_table_for_name('BackLinks')
        for row in results.rows:
            x = int(row["SourceTrustFlow"] )
            print ("EH" + str(x -4) + "AH" + str(2*x-1))
