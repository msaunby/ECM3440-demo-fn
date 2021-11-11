import base64
import json

data = {"body": "eyJzb2lsX21vaXN0dXJlIjogMTIzLjR9"}

msg_txt = base64.b64decode(data["body"])
print("decoded text is: ", msg_txt)

msg_value = json.loads(msg_txt)
print("decoded value is: ", msg_value["soil_moisture"])


