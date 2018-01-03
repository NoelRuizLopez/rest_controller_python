'''
Created on 27 de dic. de 2016

@author: Noel Ruiz. Altran
'''
from flask.helpers import make_response

def response(data, code):
    resp = make_response(data, code)
    resp.mimetype = 'application/json'
    resp.content_type = 'application/json'

    return resp

def output_test(resp):
    ret = { "result":{} }

    for element in resp:
        ret["result"][resp.index(element)] = element

    return resp

    



    
    


