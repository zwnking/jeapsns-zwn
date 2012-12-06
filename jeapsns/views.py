#coding = utf-8

from django.http import HttpResponse
#from datetime import time, datetime
from datetime import datetime
from django.template import Template, Context
from django.shortcuts import render_to_response
from jeapsns.models import Publisher

def index(request):
        return HttpResponse("django python")

def hello(request):
	message_a = "NONE"
	message_q = "NONE"
	if 'q' in request.GET:
		#message = 'You input for: %s' % request.GET['q']
		#message = 'You input for: %r' % request.GET['q']
		message_q = request.GET['q']
	if 'a' in request.GET:
			#message_a = 'You input for: %r and %r' % message,request.GET['a']
		message_a = request.GET['a']
			#message_z = message_q + ' and ' + message_a
			#message = 'You input for: %s and %s' % message_q message_a
			#message = 'You input for: %s' % message_z
		#	return HttpResponse(message)
		#	return HttpResponse(message)
	message = 'You input for: %r and %r ' % (message_q, message_a)
	if 'list' in request.GET:
		l1 = Publisher.objects.all()
		return render_to_response('hello.html', {'l1':l1})
	return HttpResponse(message)

#def hello(request):
##	message_a = "NONE"
##	message_q = "NONE"
#	if 'q' in request.GET:
#		#message = 'You input for: %s' % request.GET['q']
#		#message = 'You input for: %r' % request.GET['q']
#		message_q = request.GET['q']
#		if 'a' in request.GET:
#			#message_a = 'You input for: %r and %r' % message,request.GET['a']
#			message_a = request.GET['a']
#			message_z = message_q + ' and ' + message_a
#			#message = 'You input for: %s and %s' % message_q message_a
#			message = 'You input for: %s' % message_z
#		#	return HttpResponse(message)
#			return HttpResponse(message)
#		message_q = 'You input for: %r' % request.GET['q']
#	return HttpResponse(message_q)

def zwn(request):
        return HttpResponse("zwnking python")

def current_time(request,s,num):
#def current_time(request,string,offset):
        print s,num
#        print offset,string
        #try:
        #        offset = int(offset)
        #except ValueError:
        #        raise Http404()
        #num = time.tzinfo()
        dt = datetime.now()
        html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (num, dt)
	return HttpResponse(html)

def index_temp(request, input_name):
        t = Template('My name is {{ name }}.')
        c = Context({'name': input_name})
        return HttpResponse(t.render(c))

def index_temp_c(request, input_name, color):
        t = Template('My name is<font color = #{{color}}> {{ name }}.</font>')
        c = Context({'name': input_name, 'color':color})
        return HttpResponse(t.render(c))

def index_temp_file(request,color):
        return render_to_response('index_temp_file.html', {'color':color})
