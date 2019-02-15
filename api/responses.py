
def add_auth_to_reponse(_response, _request):
    response = _response
    response['User'] = str(_request.user)
    response['Auth'] = str(_request.auth)
    return response