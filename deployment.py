import os
import http.client
import json

def run():

    service_id = os.environ['INPUT_SERVICE-ID']
    render_token = os.environ['INPUT_RENDER-TOKEN']
    print(os.environ['GITHUB_OUTPUT'])
    str = "/v1/services/{}".format(service_id)

    conn = http.client.HTTPSConnection('api.render.com')
    headers = {'authorization': 'Bearer {}'.format(render_token)}
    conn.request('GET', str, None, headers)

    response = conn.getresponse()
    if response.status != 200:
        raise Exception("Server {} not found".format(service_id))

    info = json.loads(response.read().decode())
    website_url = info['serviceDetails']['url']

    str = str + '/deploys'
    conn.request('POST', str, None, headers)
    response = conn.getresponse()
    if response.status != 201:
        raise Exception("Server {} not found".format(service_id))

    with open(os.environ['GITHUB_OUTPUT'], 'a') as gh_output:
        print(f'website-url={website_url}', file=gh_output)

if __name__ == '__main__':
    run()
