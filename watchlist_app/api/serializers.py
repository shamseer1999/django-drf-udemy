from rest_framework import serializers
from watchlist_app.models import Movie
#######################################

###### serializer.modelserializer #####
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
    
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError('Movie name should be at least 3 characters long.')
        return value
    
    def validate(self, data):
        if data['description'] == data['name']:
            raise serializers.ValidationError('Movie description cannot be the same as the movie name.')
        return data
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