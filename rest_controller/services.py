'''
Created on 1 de dic. de 2016

@author: Asgard Team.Altran
'''
import json

from rest_controller.configuration.error_codes import CODE_POST_OK, CODE_GET_OK
from rest_controller.output import output_test, response

# def post(request ''', validator, schema'''):
def post(request, id):
    resp = [id, 'true']  # Aqui anadiriamos la llamada a la funcion correspondiente
    output = output_test(resp)
    return response(json.dumps(output), CODE_POST_OK)


def get(request):
    # json_resp = InterfaceNoTenant().start("GetEnterprises", "{}")
    resp = ['true']
    output = output_test(resp)
    return response(json.dumps(output), CODE_GET_OK)


