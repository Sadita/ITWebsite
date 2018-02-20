from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# from scotDives.models import DiveList
# from scotDives.forms import CategoryForm, PageForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
#imam---
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
# from django.template.context import RequestContext
from .models import DiveSpot, DiveClub


def login(request):
    # context = RequestContext(request, {
    #     'request': request, 'user': request.user})
    # return render_to_response('login.html', context_instance=context)
    context_dict = {}
    response = render(request, 'scotDives/login.html', context=context_dict)
    # Return response back to the user, updating any cookies that need changed.
    return response


@login_required(login_url='/')
def home(request):
    context_dict = {}
    response = render(request, 'scotDives/home.html', context=context_dict)
    # Return response back to the user, updating any cookies that need changed.
    return response



def logout(request):
    auth_logout(request)
    return redirect('/')

#imam---

def index(request):
    # request.session.set_test_cookie()
    # page_list = Pages.objects
    # page_list = Page.objects.order_by('-views')[:5]
    context_dict = {}

    # Call the helper function to handle the cookies
    # visitor_cookie_handler(request)
    # context_dict['visits'] = request.session['visits']

    response = render(request, 'scotDives/index.html', context=context_dict)
    # Return response back to the user, updating any cookies that need changed.
    return response

def divemap(request):
    all_diveSpots = DiveSpot.objects.all()
    context_dict = {'all_diveSpots' : all_diveSpots,}

    # Call the helper function to handle the cookies
    # visitor_cookie_handler(request)
    # context_dict['visits'] = request.session['visits']

    response = render(request, 'scotDives/divemap.html', context=context_dict)
    # Return response back to the user, updating any cookies that need changed.
    return response

def divesites(request):
    # request.session.set_test_cookie()
    # page_list = Pages.objects
    # page_list = Page.objects.order_by('-views')[:5]
    context_dict = {}

    # Call the helper function to handle the cookies
    # visitor_cookie_handler(request)
    # context_dict['visits'] = request.session['visits']

    response = render(request, 'scotDives/divesites.html', context=context_dict)
    # Return response back to the user, updating any cookies that need changed.
    return response

def clubmap(request):
    all_diveClubs = DiveClub.objects.all()
    context_dict = {'all_diveClubs' : all_diveClubs,}

    # Call the helper function to handle the cookies
    # visitor_cookie_handler(request)
    # context_dict['visits'] = request.session['visits']

    response = render(request, 'scotDives/clubmap.html', context=context_dict)
    # Return response back to the user, updating any cookies that need changed.
    return response


def photogallery(request):
    # request.session.set_test_cookie()
    # page_list = Pages.objects
    # page_list = Page.objects.order_by('-views')[:5]
    context_dict = {}

    # Call the helper function to handle the cookies
    # visitor_cookie_handler(request)
    # context_dict['visits'] = request.session['visits']

    response = render(request, 'scotDives/photogallery.html', context=context_dict)
    # Return response back to the user, updating any cookies that need changed.
    return response


def search(request):
    # request.session.set_test_cookie()
    # page_list = Pages.objects
    # page_list = Page.objects.order_by('-views')[:5]
    context_dict = {}

    # Call the helper function to handle the cookies
    # visitor_cookie_handler(request)
    # context_dict['visits'] = request.session['visits']

    response = render(request, 'scotDives/search.html', context=context_dict)
    # Return response back to the user, updating any cookies that need changed.
    return response


def contact(request):
    # request.session.set_test_cookie()
    # page_list = Pages.objects
    # page_list = Page.objects.order_by('-views')[:5]
    context_dict = {}

    # Call the helper function to handle the cookies
    # visitor_cookie_handler(request)
    # context_dict['visits'] = request.session['visits']

    response = render(request, 'scotDives/contact.html', context=context_dict)
    # Return response back to the user, updating any cookies that need changed.
    return response


def sitemap(request):
    # request.session.set_test_cookie()
    # page_list = Pages.objects
    # page_list = Page.objects.order_by('-views')[:5]
    context_dict = {}

    # Call the helper function to handle the cookies
    # visitor_cookie_handler(request)
    # context_dict['visits'] = request.session['visits']

    response = render(request, 'scotDives/sitemap.html', context=context_dict)
    # Return response back to the user, updating any cookies that need changed.
    return response

