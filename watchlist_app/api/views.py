from  rest_framework.response import Response 
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from watchlist_app.models import WatchList,StreamPlatform,Riview
from watchlist_app.api.serializers import WatchListSeralizer, StreamPlatformSerializer,ReviewSerializer,UserSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from watchlist_app.api.permissions import IsReviewOwnerOrReadOnly
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from watchlist_app.api.pagination import watchListPagination

#######################################

class UsersList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter]
    search_fields = ['username']
    pagination_class = watchListPagination
    # page_size = 2
    # def get_queryset(self):
    #     queryset = User.objects.all()
    #     username = self.request.query_params.get('username')
    #     if username is not None:
    #         return queryset.filter(username=username)
    #     return queryset
class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        return Riview.objects.all()
    
    def perform_create(self, serializer):
        watchlist = WatchList.objects.get(pk=self.kwargs['pk'])
        review_user=self.request.user
        review_queryset = Riview.objects.filter(watchlist=watchlist, review_user=review_user)
        
        if review_queryset.exists():
            raise ValidationError('This user reviewed already')
        
        if watchlist.number_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['rating']) / 2
        
        watchlist.number_rating += 1
        watchlist.save()
        
        serializer.save(watchlist=watchlist, review_user=review_user)
class ReviewsList(generics.ListAPIView):
    # queryset = Riview.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Riview.objects.filter(watchlist=pk)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Riview.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewOwnerOrReadOnly]
# class ReviewsList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Riview.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request,*args,**kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class ReviewDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Riview.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self, request, pk, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
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
            WatchListData = WatchList.objects.get(pk=watchlist_id)
        except WatchListData.DoesNotExist:
            return Response({'Error':'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = WatchListSeralizer(WatchListData)
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
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error':'Platform not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
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