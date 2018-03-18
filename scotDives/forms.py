from django import forms
from django.contrib.auth.models import User
from scotDives.models import UserProfile, Review
from registration.forms import RegistrationForm
        
class UserForm(RegistrationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    username = forms.CharField(max_length=50, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    class Meta:
        model = UserProfile
        fields = ('picture',)


class UserReviewForm(forms.ModelForm):
    rating = forms.IntegerField(required=False)
    comment = forms.CharField(max_length=1000, required=False)

    class Meta:
        model = Review
        fields = ('rating', 'comment')


