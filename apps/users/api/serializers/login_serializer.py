from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model



class CustomUserDetailsSerializer(UserDetailsSerializer):
    
    class Meta(UserDetailsSerializer.Meta):
       model = get_user_model()
       
       fields = UserDetailsSerializer.Meta.fields + ('email','first_name','last_name')
       
        
        
        
        