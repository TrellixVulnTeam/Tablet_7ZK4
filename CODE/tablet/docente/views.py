from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home_d(request):
	
	return render(request,"home_d.html")