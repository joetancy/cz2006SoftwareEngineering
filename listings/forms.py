from django import forms

ROOM_TYPES = (
    ('2-Room Flexi', '2-Room Flexi'),
    ('3-Room', '3-Room'),
    ('4-Room', '4-Room'),
    ('5-Room', '5-Room'),
    ('3Gen', '3Gen'),
    ('Executive Flat', 'Executive Flat'),
)


class CreateListingForm(forms.Form):
    postalCode = forms.IntegerField(
        label='Postal Code', required=True, widget=forms.NumberInput(attrs={'oninput': 'getAddress()'}))
    block = forms.CharField(label='Block', max_length=5, required=True)
    street = forms.CharField(label='Street', required=True, max_length=None)
    floor = forms.IntegerField(label='Floor', required=True)
    unit = forms.CharField(label='Unit', max_length=4, required=True)
    roomType = forms.ChoiceField(
        choices=ROOM_TYPES, label='Room Type', required=True)
    latitude = forms.FloatField(
        label='Latitude', required=True, widget=forms.HiddenInput())
    longitude = forms.FloatField(
        label='Longitude', required=True, widget=forms.HiddenInput())
    description = forms.CharField(
        label='Description', max_length=500, required=True, widget=forms.Textarea)
    askingPrice = forms.IntegerField(label='Price', required=True)
    picture0 = forms.FileField()
    picture1 = forms.FileField(required=False)
    picture2 = forms.FileField(required=False)
    picture3 = forms.FileField(required=False)


class UpdateListingForm(forms.Form):
    postalCode = forms.IntegerField(
        label='Postal Code', required=True, widget=forms.NumberInput(attrs={'oninput': 'getAddress()'}))
    block = forms.CharField(label='Block', max_length=5, required=True)
    street = forms.CharField(label='Street', required=True, max_length=None)
    floor = forms.IntegerField(label='Floor', required=True)
    unit = forms.CharField(label='Unit', max_length=4, required=True)
    roomType = forms.ChoiceField(
        choices=ROOM_TYPES, label='Room Type', required=True)
    latitude = forms.FloatField(
        label='Latitude', required=True, widget=forms.HiddenInput())
    longitude = forms.FloatField(
        label='Longitude', required=True, widget=forms.HiddenInput())
    description = forms.CharField(
        label='Description', max_length=500, required=True, widget=forms.Textarea)
    askingPrice = forms.IntegerField(label='Price', required=True)
