from bottle import get,run,post,request,route,response,static_file


@post('/login')
def login():
    user_identification = request.json.get('usr')
    user_password = request.json.get('pd')
    if user_identification == "admin" and user_password == "admin":
        response.content_type='application/json; charset=utf-8'
        response.status = 200
        response.set_cookie('JSESSIONID', 'SES121212')
        return {'status':'ok'}
    else:
        response.content_type='application/json; charset=utf-8'
        response.status = 200
        return {'status':'fail'}

@post('/user/csrf')
def csrf():
    sessinId=request.get_cookie('JSESSIONID')
    if sessinId == 'SES121212':
        response.content_type='application/json; charset=utf-8'
        response.status = 200
        response.set_cookie('CSRF_TOKEN', '12345')
        return {'CSRF_TOKEN':'123245'}
    else:
        response.content_type='application/json; charset=utf-8'
        response.status = 200
        return {'CSRF_TOKEN':'no'}

@post('/user/doublesubmit')
def doublesubmit():
    sessinId=request.get_cookie('JSESSIONID')
    CSRF_TOKEN=request.get_cookie('CSRF_TOKEN')
    if sessinId=="SES121212" and CSRF_TOKEN=="12345":
        response.content_type='application/json; charset=utf-8'
        response.status = 200
        return {'validation':'ok'}
    else:
        response.content_type='application/json; charset=utf-8'
        response.status = 200
        return {'validation':'fail'}

@route('/<filename:path>')
def server_static(filename):
    return static_file(filename, root='static/')

run(host='localhost', port=8090 )