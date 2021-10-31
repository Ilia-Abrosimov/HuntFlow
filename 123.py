# data = {"externals": [
#         {
#             "data": {
#                 "body": "Текст резюме\nТакой текст"
#             },
#             "auth_type": "NATIVE",
#             "files": [
#                 {
#                     "id": 12430
#                 }
#             ],
#             "account_source": 208
#         }
#     ]
# }
# print(data.get("externals")[0]['files'][0]["id"])
externals = [{"files": [{"id": 4}]}]
print(externals[0]['files'][0]["id"])