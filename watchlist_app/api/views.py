from  rest_framework.response import Response 
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from watchlist_app.models import WatchList,StreamPlatform
from watchlist_app.api.serializers import WatchListSeralizer, StreamPlatformSerializer
#######################################


class WatchListListView(APIView):
    def get(self, request):
        WatchLists = WatchList.objects.all()
        
        serializer = WatchListSeralizer(WatchLists, many=True)
        
        return Response(serializer.data)
    
    def post(self, request):
        if isinstance(request.data, list):  # Check if the data is a list
            serializer = WatchListSeralizer(data=request.data, many=True)
        else:
            serializer = WatchListSeralizer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WatchListListDetailView(APIView):
    def get(self, request,watchlist_id):
        try:
            WatchList = WatchList.objects.get(pk=watchlist_id)
        except WatchList.DoesNotExist:
            return Response({'Error':'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = WatchListSeralizer(WatchList)
        return Response(serializer.data)
    
    def put(self, request, watchlist_id):
        try:
            WatchList = WatchList.objects.get(pk=watchlist_id)
        except WatchList.DoesNotExist:
            return Response({'Error':'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = WatchListSeralizer(WatchList, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SreamPlatformView(APIView):
    def get(self, request):
        platforms = StreamPlatform.objects.all()
        
        serializer = StreamPlatformSerializer(platforms, many=True)
        
        return Response(serializer.data)
    
    def post(self, request):
        if isinstance(request.data, list):  # Check if the data is a list
            serializer = StreamPlatformSerializer(data=request.data, many=True)
        else:
            serializer = StreamPlatformSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SreamPlatformDetailView(APIView):
    def get(self, request, platform_id):
        try:
            platform = StreamPlatform.objects.get(pk=platform_id)
        except StreamPlatform.DoesNotExist:
            return Response({'Error':'Platform not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)
    
    def put(self, request, platform_id):
        try:
            platform = StreamPlatform.objects.get(pk=platform_id)
        except StreamPlatform.DoesNotExist:
            return Response({'Error':'Platform not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StreamPlatformSerializer(platform, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# @api_view(['GET', 'POST'])
# def movie_list(request):
    
#     if request.method == 'GET':
#         movies = Movie.objects.all()
        
#         serializer = MovieSerializer(movies, many=True)
        
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# @api_view(['GET','PUT','DELETE'])
# def movie_detail(request, movie_id):
    
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=movie_id)
#         except Movie.DoesNotExist:
#             return Response({'Error':'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         try:
#             movie = Movie.objects.get(pk=movie_id)
#         except Movie.DoesNotExist:
#             return Response({'Error':'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie, data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'DELETE':
#         try:
#             movie = Movie.objects.get(pk=movie_id)
#         except Movie.DoesNotExist:
#             return Response({'Error':'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)