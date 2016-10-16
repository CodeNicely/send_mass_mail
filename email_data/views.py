from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django import forms
from django.core.mail import send_mail
import requests

class UploadFileForm(forms.Form):
    file = forms.FileField()

def send_mass_mails(request):
	if request.method=="POST":
	    try:
	    	group_id=request.POST.get("group_id")
	    	print group_id
	    	subject=str(request.POST.get("subject"))
	    	print subject
	    	message=str(request.POST.get("message"))
	    	print message
	    	#group_id=1;
	    	#subject="Hello"
	    	#message="For testing purpose"
	    	response={}
	    	for o in user_data.objects.filter(group_id=group_id):
	    		send_mail(
	    			subject,
	    			message,
	    			'no-reply@aditya.com',
	    			[str(o.user_emailid)],
	    			fail_silently=False,
	    			)
	    	response["success"]=True
	    	response["message"]="email sent"
	    except:
	    	response["success"]=False
	    	response["message"]="email not sent"
    
	    print str(response)
	    return HttpResponse(str(response))
	else:
		return render(
            request,
            'send.html',
            {'title':'send email'},{'header': 'write subject message'})

def import_sheet(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)
        
        if form.is_valid():
            request.FILES['file'].save_to_database(
                model=user_data,
                mapdict=['user_name', 'user_emailid', 'group_id'])
            return HttpResponse("OK")
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(
        request,
        'upload.html',
        {'form': form})


	


# Create your views here.
