from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from django.http import HttpResponseRedirect
import textwrap
from django.views.decorators.csrf import csrf_exempt
from login.models import Users
from passlib.hash import bcrypt

@csrf_exempt
def signup(request):
	

    if request.method == 'POST':
        print request.POST.get('email')
        
        userdata = Users(email=request.POST.get('email'), password=bcrypt.encrypt(request.POST.get('password')))
        userdata.save()
        
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Greetings to the world</title>
            </head>
            <body>
               Hello '''+request.POST.get('email')+''' <a href="/users">Login</a>	
            </body>
            </html>
        ''')
    else:	

        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Greetings to the world</title>
            </head>
            <body>
                <h1>Signup</h1>
                <p>Hello, world!</p>
				<form method="POST" src="">
				Email
				<input type="text" name="email" value="" />
				Password
				<input type="text" name="password" value="" />
				<input type="submit" name="signup" value="Signup" />
				</form>
				<a href="/users">Login</a>				
            </body>
            </html>
        ''')
    return HttpResponse(response_text)    

@csrf_exempt	
def index(request):
    if request.method == 'POST':
        
        q = Users.objects.get(email=request.POST.get('email'))
        	
        if(q.email == request.POST.get('email') and bcrypt.verify(request.POST.get('password'), q.password)):
            response_text = textwrap.dedent('''\
                <html>
                <head>
                    <title>Greetings to the world</title>
                </head>
                <body>
                    Hello ''' +q.email+ '''
                </body>
                </html>
            ''')
        else:
            response_text = textwrap.dedent('''\
                <html>
                <head>
                    <title>Greetings to the world</title>
                </head>
                <body>
                   invalid account info please <a href="/users">Login</a> again.
                </body>
                </html>
            ''')		
    else:	

        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Greetings to the world</title>
            </head>
            <body>
                <h1>Login</h1>
                <p>Hello, world!</p>
				<form method="POST" src="">
				Email
				<input type="text" name="email" value="" />
				Password
				<input type="text" name="password" value="" />
				<input type="submit" name="login" value="Login" />
				</form>
				
				<a href="/users/signup">Signup</a>
            </body>
            </html>
        ''')
    return HttpResponse(response_text)