# import requests
# from pprint import pprint
# from test import AUTH_TOKEN
#
#
# def upload_file():
#     url = "https://dev-100-api.huntflow.dev/account/2/upload"
#     files = {'file': ('Пушкин Александр', open('Frontend-разработчик/Танский Михаил.pdf', 'rb'), 'application/pdf')}
#     headers = {'Authorization': f'Bearer {AUTH_TOKEN}',
#                'X-File-Parse': 'True'}
#     response = requests.post(url, headers=headers, files=files)
#     return response.json()
#
# pprint(upload_file())