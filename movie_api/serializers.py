from rest_framework import serializers
from .models import WatchList ,PlatForm,Review

# class watchListSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title =serializers.CharField(max_length=50)
#     storyline = serializers.CharField(max_length=100) #description
#     #platform = serializers.ForeignKey("platform",  on_delete=models.CASCADE)
#     active = serializers.BooleanField(default=True)
#     created_time = serializers.DateTimeField()

    
#     def create(self, validated_data):
#         """
#         Create and return a new `WatchList` instance, given the validated data.//instace means old and validated data new
#         """
#         return WatchList.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.storyline = validated_data.get('storyline', instance.storyline)
#         instance.active = validated_data.get('active', instance.active)
#         instance.created_time = validated_data.get('created_time', instance.created_time)
#         instance.save()
#         return instance

#   or

class watchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = '__all__'

    
class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only = True)
    watchlist = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Review
        fields = '__all__'
        #exclude = ['watchlist']
     


class PlatFormSerializer(serializers.ModelSerializer):

    watch_list= watchListSerializer(many=True, read_only=True)

    """def validate_name(self,value):
        if len(value) <3:
            raise serializers.ValidationError("name is too short")
        return value
    
    def validate(self,data):
       # print(data)
        if data['name'] == data['about']:
            raise serializers.ValidationError("name and about are same")
        return data"""
 
    class Meta:
        model = PlatForm
        fields ='__all__'



#   or


# class PlatFormSerializer(serializers.HyperlinkedModelSerializer):
#     link = serializers.HyperlinkedIdentityField(view_name ='PlatForm_list')
#     class Meta:
#         model = PlatForm
#         fields = ['link','name', 'about', 'website']# '__all__'


#or


# class PlatFormSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=50)
#     about = serializers.CharField(max_length= 100)
#     website = serializers.URLField(max_length=100)

#     def create(self, validated_data):
#         """
#         Create and return a new `PlatForm` instance, given the validated data.//instace means old and validated data new
#         """
#         return PlatForm.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.name = validated_data.get('name', instance.name)
#         instance.about = validated_data.get('about', instance.about)
#         instance.website= validated_data.get('website', instance.website)

#         instance.save()
#         return instance 
