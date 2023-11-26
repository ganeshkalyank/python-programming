from django.shortcuts import render
import re

# Create your views here.

def validate(request):
    if request.method == 'GET':
        return render(request, 'emailapp/index.html', {'valid': ''})
    else:
        email = request.POST['email']
        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            return render(request, 'emailapp/index.html', {'valid': 'Valid Email!'})
        return render(request, 'emailapp/index.html', {'valid': 'Invalid Email!'})
