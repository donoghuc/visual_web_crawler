import hashlib
from datetime import timedelta

auth_cookie_name = 'caelum_cookie'


def set_auth(request, user_id):
    '''build cookie, node somewhat annoying callback method to make it work'''
    hash_val = __hash_text(user_id)
    val = "{}:{}".format(user_id, hash_val)

    request.add_response_callback(lambda req, resp: __add_cookie_callback(
        req, resp, auth_cookie_name, val
    ))


def __hash_text(text):
    '''salted has method'''
    text = 'saltiness_' + text + '_for_the_text'
    return hashlib.sha512(text.encode('utf-8')).hexdigest()


def __add_cookie_callback(_, response, name, value):
    '''set the cookie'''
    response.set_cookie(name, value, max_age=timedelta(days=30))


def get_user_id_via_auth_cookie(request):
    ''' get user id based on cookie value. Note no db interaction'''
    if auth_cookie_name not in request.cookies:
        return None

    val = request.cookies[auth_cookie_name]
    parts = val.split(':')
    if len(parts) != 2:
        return None

    user_id = parts[0]
    hash_val = parts[1]
    hash_val_check = __hash_text(user_id)
    if hash_val != hash_val_check:
        print("Warning: Hash mismatch, invalid cookie value")
        return None

    return user_id


def logout(request):
    '''remove cookie'''
    request.add_response_callback(lambda req, resp: __delete_cookie_callback(
        resp, auth_cookie_name
    ))


def __delete_cookie_callback(response, name):
    response.delete_cookie(name)
