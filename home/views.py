from .forms import CreateSearchForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db import models
from listings.models import Listing, ListingPicture
import json
# Create your views here.
def index(request):
        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateSearchForm(request.POST)
        search = request.POST.get("search", "")
        #print(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.cleaned_data
            if(search == "advance_search"):
                listing = Listing.objects.filter(street__startswith = "")
                checkbox = request.POST.getlist('proximity')
                radius = request.POST.get("radius", "")
                reverse_search = True
            else:
                listing = Listing.objects.filter(street__iregex = r'\b'+data['location'])
                reverse_search = False
            # process the data in form.cleaned_data as required
            #print(data)
            #listing = Listing.objects.get(street = data['location'])
            noData = (len(listing) == 0)
            listingPictures = ListingPicture.objects.filter(listing__in=listing)
            print(listingPictures.query)
            #print(listingPictures[0].listing_id)
            #listing2 = Listing.objects.filter(street__icontains = data['location']).only("latitude","longitude")
            searchInput = True
            if(reverse_search):
                context ={'location_listing': listing, 'form': form,'searchInput':searchInput,"listing_picture":listingPictures,"noData":noData,"checkbox":checkbox,"radius":radius,"reverse_search":reverse_search}
            else:
                context ={'location_listing': listing, 'form': form,'searchInput':searchInput,"listing_picture":listingPictures,"noData":noData,"reverse_search":reverse_search}
            return  render(request, 'index.html', context)
            #FOR CHECKBOX FORM http://stackoverflow.com/questions/29714763/django-check-if-checkbox-is-selected
    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateSearchForm()
        searchInput = False
    return render(request, 'index.html', {'form': form},{'searchInput':searchInput})

