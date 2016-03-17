import requests # dont forget to install in this venv

requests.put("http://127.0.0.1:5000/",data = '{"who": "Anton Dalsmo", "what": "exit"}',headers={'content-type':'text/json'})


print "did a put request"
