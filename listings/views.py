from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import models
from .forms import *
from .models import Listing, ListingPicture
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
# Create your views here.


def create(request):
    form = CreateListingForm(request.POST or None, request.FILES or None)
    if(form.is_valid()):
        data = form.cleaned_data
        # added type casting to prevent type error @timo
        if(int(data['askingPrice']) < 0 or int(data['floor']) < 0 or int(data['unit']) < 0):
            form.add_error(None, "Floor, unit & price cannot be negative!")
            return render(request, 'listings/createListing.html', {'form': form})
        listing = Listing(user=request.user, block=data['block'], street=data['street'], floor=data['floor'], unit=data[
                          'unit'], postalCode=data['postalCode'], latitude=data['latitude'], longitude=data['longitude'], description=data['description'], askingPrice=data['askingPrice'], roomType=data['roomType'], statusClosed=False)
        listing.save()
        for pictures in request.FILES:
            pic0 = ListingPicture(
                listing=listing, image=request.FILES[pictures])
            pic0.save()
        return redirect('/listing/view/')
    return render(request, 'listings/createListing.html', {'form': form})


def view(request):
    listings = Listing.objects.filter(user=request.user)
    listingPictures = ListingPicture.objects.filter(listing__in=listings)
    return render(request, 'listings/viewListings.html', {'listings': listings, 'listingPictures': listingPictures})


def viewAll(request):
    # listings = Listing.objects.all()
    # listingPictures = ListingPicture.objects.filter(listing__in=listings)
    # return render(request, 'listings/viewAllListings.html', {'listings':
    # listings, 'listingPictures': listingPictures})
    listings_list = Listing.objects.all()
    paginator = Paginator(listings_list, 5)  # Show 5 listing per page
    page = request.GET.get('page')
    try:
        listings = paginator.page(page)
        listingPictures = ListingPicture.objects.filter(listing__in=listings)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        listings = paginator.page(1)
        listingPictures = ListingPicture.objects.filter(listing__in=listings)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        listings = paginator.page(paginator.num_pages)
        listingPictures = ListingPicture.objects.filter(listing__in=listings)
    return render(request, 'listings/viewAllListings.html', {'listings': listings, 'listingPictures': listingPictures})


def viewDetail(request, listing_id):
    listings = Listing.objects.filter(id=listing_id)
    for listing in listings:
        poster = User.objects.get(id=listing.user.id)
    listingPictures = ListingPicture.objects.filter(listing=listings)
    return render(request, 'listings/viewListingDetail.html', {'listings': listings, 'listingPictures': listingPictures, 'poster': poster})


def delete(request, listing_id):
    listings = Listing.objects.get(id=listing_id)
    if(listings.user == request.user):
        listings.delete()
        if(listings):
            return redirect('/listing/view/')
    else:
        return HttpResponseForbidden()


def verifyUserToListing(user_id, listing_id):
    listings = Listing.objects.get(id=listing_id)
    if(listings.user == user_id):
        return True
    else:
        return False
