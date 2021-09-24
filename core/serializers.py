from rest_framework import serializers
from core.models import Activity, ActivityImage, BoxImage, Category, Box, Reason

class ReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model= Reason
        fields = ['id','name','order','slug']

class BoxImageSerializer(serializers.ModelSerializer):
     class Meta:
        model= BoxImage
        fields = ['id','order','upload']

class ActivityImageSerializer(serializers.ModelSerializer):
     class Meta:
        model= ActivityImage
        fields = ['id','order','upload']
class BoxSerializer(serializers.ModelSerializer):
    
    boximage_set = BoxImageSerializer(many=True)
    class Meta:
        model= Box
        fields = ['name','slug','category','description','purchase_available','price','boximage_set']

class ActivitySerializer(serializers.ModelSerializer):
    reasons = ReasonSerializer(many=True)
    activityimage_set = ActivityImageSerializer(many=True)
    class Meta:
        model= Activity
        fields = ['name','slug','category','description','purchase_available','reasons','activityimage_set']

class BoxCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Box
        fields = ['name','slug','price']

class CategorySerializer(serializers.ModelSerializer):
    box_set=BoxCategorySerializer(many=True)
    class Meta:
        model= Category
        fields = ['name','slug','order','description','box_set']