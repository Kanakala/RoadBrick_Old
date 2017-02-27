from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404

from . forms import MessageForm, PostForm

def index(request):
	form = MessageForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		form.save()
		
		return HttpResponseRedirect('/')
	else:
		form = MessageForm()
	context = {
		"form": form,
	}
	return render(request, 'index.html', context)
	
def post_load(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		form.save()
		
		return HttpResponseRedirect('/')
	else:
		form = PostForm()
	context = {
		"form": form,
	}
	return render(request, 'post_load.html', context)
	
