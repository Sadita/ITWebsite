from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth.models import User
from scotDives.forms import UserProfileForm, UserReviewForm
from scotDives.models import DiveClub, DiveSite, UserProfile, Picture, Review, FutureDive
from django.views.generic.edit import CreateView
from django.db.models import Avg


# The function to render the template of the home page.
def index(request):
    context_dict = {}

    # For the top three dives based on user rating
    divesite_list = DiveSite.objects.order_by('-rating')[:3]

    context_dict['divesites'] = divesite_list
    response = render(request, 'scotDives/index.html', context=context_dict)

    # Return response back to the user.
    return response


# Sends the dive locations and the details to the map of divesites
def divemap(request):
    all_diveSpots = DiveSite.objects.all()
    context_dict = {'all_diveSpots' : all_diveSpots,}
    response = render(request, 'scotDives/divemap.html', context=context_dict)

    # Return response back to the user.
    return response


# To render the template for the list of dive sites.
def divesites(request):
    context_dict = {}

    # Divesites are ordered with highest rated first
    divesite_list = DiveSite.objects.order_by('-rating')
    context_dict['divesites'] = divesite_list

    response = render(request, 'scotDives/divesitelist.html', context=context_dict)
    # Return response back to the user.
    return response


# To render each of the individual dive site pages
def show_site(request, divesite_name_slug):
    context_dict = {}
    try:
        # adding the divesite model to the dictionary
        divesite = DiveSite.objects.get(slug=divesite_name_slug)
        context_dict['divesite'] = divesite
    except DiveSite.DoesNotExist:
        context_dict['divesite'] = None

    try:
        # All reviews on this dive site added to context dictionary in order of date,
        # i.e. the most recent user review comes on top of the list of reviews.
        reviews = Review.objects.filter(divesite=divesite).order_by('-date')
        context_dict['reviews'] = reviews
    except Review.DoesNotExist:
        context_dict['reviews'] = None

    if request.user.is_authenticated():
        try:
            # adding the user rating from the Review model to the dictionary
            user_rating = Review.objects.get(divesite=divesite, user=request.user).rating
            context_dict['user_rating'] = user_rating
        except Review.DoesNotExist:
            context_dict['user_rating'] = 0

        response = render(request, 'scotDives/divesite.html', context=context_dict)

        # Return response back to the user.
        return response

    else:
        response = render(request, 'scotDives/divesite.html', context=context_dict)

        # Return response back to the users.
        return response


# Sends the locations and the details to the map of dive clubs
def clubmap(request):
    all_diveClubs = DiveClub.objects.all()
    context_dict = {'all_diveClubs' : all_diveClubs,}
    response = render(request, 'scotDives/clubmap.html', context=context_dict)

    # Return response back to the user, updating any cookies that need changed.
    return response


# Sends the location of the picture file and the corresponding details to the photo gallery template
def photogallery(request):
    all_pictures = Picture.objects.all()
    context_dict = {'all_pictures': all_pictures}
    response = render(request, 'scotDives/photogallery.html', context=context_dict)

    # Return response back to the user.
    return response


# Search function that returns all dive sites that match the query
def search(request):
    context_dict = {}
    divesite_list = DiveSite.objects.order_by('-name')
    query = request.GET.get("q")
    if query:
        divesite_list = divesite_list.filter(name__icontains=query)
        print(divesite_list)
        context_dict['divesites'] = divesite_list

    response = render(request, 'scotDives/search.html', context=context_dict)
    # Return response back to the user.
    return response


# Function that lets the user create a profile page once they have create a ScotDives account
@login_required
def register_profile(request):
    form = UserProfileForm()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
    if form.is_valid():
        user_profile = form.save(commit=False)
        user_profile.user = request.user
        user_profile.save()
        return redirect('index')
    else:
        print(form.errors)
    context_dict = {'form':form}
    return render(request, 'scotDives/profile_registration.html', context_dict, locals())


# Returns the user's profile with their My Dives list and profile picture
@login_required
def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('index')
    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    form = UserProfileForm({'picture': userprofile.picture})

    # List of future dive sites added by the user to the profile
    favorite_divesites = FutureDive.objects.filter(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('profile', user.username)
        else:
            print(form.errors)
    return render(request, 'scotDives/profile.html', {'userprofile': userprofile, 'selecteduser': user,
                                                      'form': form, 'favorite_divesites': favorite_divesites})


# Render the contact us page of the website
def contact(request):
    context_dict = {}
    response = render(request, 'scotDives/contact.html', context=context_dict)
    # Return response back to the user.
    return response


# Render the site map page of the website
def sitemap(request):
    context_dict = {}
    response = render(request, 'scotDives/sitemap.html', context=context_dict)
    # Return response back to the user.
    return response


# This function adds the ratings and comments on a dive site page submitted by the user
@login_required
def rate(request):

    # When user submits a rating or a comment, retrieve the divesite_id from the ajax call.
    if request.method == 'POST':
        form = UserReviewForm(request.POST)
        divesite_id = request.POST.get('divesite_id')
        # Get the unique review from the composite key of divesite and user
        try:
            review = Review.objects.get(divesite_id=divesite_id, user_id=request.user.id)
        except Review.DoesNotExist:
            review = None

        if form.is_valid():
            # If review exists get the submitted rating and comment  from the form;
            # get the current date, that is, the date of of the review submission,
            # and save to the Review model.
            if review:
                if request.POST.get('rating'):
                    review.rating = request.POST.get('rating')
                    review.date = datetime.now()
                if request.POST.get('comment'):
                    review.comment = request.POST.get('comment')
                    review.date = datetime.now()
                review.save()
            else:
                review = form.save(commit=False)
                review.divesite = DiveSite.objects.get(id=divesite_id)
                review.user = request.user
                review.save()

            # Compute the average of all the ratings submitted by the users and save to the
            # "rating" field of the divesite model.
            avg_rating = Review.objects.filter(divesite_id=divesite_id).aggregate(Avg('rating'))
            divesite = DiveSite.objects.get(id=divesite_id)
            divesite.rating = avg_rating['rating__avg']
            divesite.save()

    # Return response back to the ajax function that called this function.
    return JsonResponse({'avg_rating': divesite.rating})


# This function adds the divesites to user's future dive list (favorites)
@login_required
def add_my_list(request):
    if request.method == 'POST':
        try:
            # Get the divesite selected/added by the user from the ajax call.
            divesite = DiveSite.objects.get(id=request.POST.get('divesite_id'))

            # Get or create the future dive site selected by the user
            try:
                FutureDive.objects.get(divesite=divesite, user=request.user)
            except FutureDive.DoesNotExist:
                FutureDive.objects.create(divesite=divesite, user=request.user)
        finally:
            return HttpResponse('')


# This function deletes divesites from user's future dive list (favorites)
@login_required
def remove_from_my_list(request, divesite_id):
    if request.method == 'POST':
        try:
            # Get the divesite selected (to be deleted) by the user from the ajax call.
            divesite = DiveSite.objects.get(id=divesite_id)
            try:
                FutureDive.objects.get(divesite=divesite, user=request.user).delete()
            except FutureDive.DoesNotExist:
                print('Could not be deleted from favorite dive sites')

        finally:
            return HttpResponse('')


# This function deletes the user's account when user clicks the delete account button
@login_required
def delete_account(request):
    if request.method == 'POST':
        try:
            # Get the user from the ajax call triggered by the delete account button.
            # Delete user profile and then delete the user.
            UserProfile.objects.get(user=request.user).delete()
            print("UP deleted")
            request.user.delete()
            print("User deleted")
        except UserProfile.DoesNotExist:
            print("User Profile does not exist")

    return HttpResponse('')


class PictureCreate(CreateView):
    model = Picture
    fields = ['location', 'description', 'pic']
