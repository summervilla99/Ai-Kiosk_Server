from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import CustomUser, Membership

class CustomRegisterSerializer(RegisterSerializer):
    name = serializers.CharField(required=True, max_length=30)
    
    def save(self, request):
        user = super().save(request)
        user.name = self.data.get('name')
        user.save()
        return user
    
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'name']

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ['ID' ,'phone_number', 'total_point']
