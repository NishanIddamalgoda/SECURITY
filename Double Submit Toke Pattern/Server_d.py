from bottle import get,run,post,request,route,response,static_file


@post('/login')
def login():
    user_identification = request.json.get('usr')
    user_password = request.json.get('pd')
    if user_identification == "admin" and user_password == "admin":
        response.content_type='application/json; charset=utf-8'
        response.status = 200
        response.set_cookie('JSESSIONID', 'SES121212')
        response.set_cookie('CSRF_TOKEN', '12345')
        return {'status':'ok'}
    else:
        response.content_type='application/json; charset=utf-8'
        response.status = 200
        return {'status':'fail'}

@post('/user/doublesubmit')
def doublesubmit():
    sessinId=request.get_cookie('JSESSIONID')
    CSRF_TOKEN_para=request.json.get('CSRF_TOKEN')
    CSRF_TOKEN=request.get_cookie('CSRF_TOKEN')
    if sessinId=="SES121212" and CSRF_TOKEN==CSRF_TOKEN_para:
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
