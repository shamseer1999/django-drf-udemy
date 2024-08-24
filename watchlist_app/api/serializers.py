from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform,Riview
#######################################

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Riview
        fields = '__all__'
class WatchListSeralizer(serializers.ModelSerializer):
    riviews = ReviewSerializer(many=True,read_only=True)
    class Meta:
        model = WatchList
        fields = '__all__'

class StreamPlatformSerializer(serializers.ModelSerializer):
    
    watchlist = WatchListSeralizer(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = '__all__'
###### serializer.modelserializer #####
# class MovieSerializer(serializers.ModelSerializer):
#     # add aditional field in serializer
#     len_name = serializers.SerializerMethodField()
#     class Meta:
#         model = Movie
#         fields = '__all__'
    
#     def get_len_name(self, obj):
#         return len(obj.name)
#     def validate_name(self, value):
#         if len(value) < 3:
#             raise serializers.ValidationError('Movie name should be at least 3 characters long.')
#         return value
    
#     def validate(self, data):
#         if data['description'] == data['name']:
#             raise serializers.ValidationError('Movie description cannot be the same as the movie name.')
#         return data
###### serializer.modelserializer #####

###### serializer.serializer ##########
#validators for validating
# def name_length(value):
#     if len(value) < 3:
#         raise serializers.ValidationError('Movie name should be at least 3 characters long.')
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=50,validators=[name_length])
#     description = serializers.CharField(max_length=200)
#     active = serializers.BooleanField()
    
#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     #field level validation
#     # def validate_name(self, value):
#     #     if len(value) < 3:
#     #         raise serializers.ValidationError('Movie name should be at least 3 characters long.')
#     #     return value
    
#     #object level validation
#     def validate(self, data):
#         if data['description'] == data['name']:
#             raise serializers.ValidationError('Movie description cannot be the same as the movie name.')
#         return data
    
    
###### serializer.serializer ##########