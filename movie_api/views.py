from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.http import Http404

from . models import WatchList,PlatForm,Review
from .serializers import watchListSerializer,PlatFormSerializer,ReviewSerializer
from .permissions import AdminUserOrReadOnly,ReviewUserOrReadOnly

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView,permission_classes
from rest_framework import generics,mixins,viewsets
from rest_framework.reverse import reverse
from rest_framework.decorators import action
from rest_framework.serializers import ValidationError
from rest_framework.permissions import IsAuthenticated,IsAdminUser


#  entry point like as home page design

@api_view(['GET']) 
def api_root(request, format=None):
    return Response({
        'movie': reverse('WatchList_list', request=request, format=format),
        'platform': reverse('PlatForm_list', request=request, format=format)
    })

#Create your views here.

@api_view(['GET'])
@permission_classes ([IsAuthenticated])
def movie_list(request):
    watch_list = WatchList.objects.all()
    serialized = watchListSerializer(watch_list, many=True)
    return Response(serialized.data)

@api_view(['GET'])
def movie_detail(request,pk):   
    list1 = WatchList.objects.get(pk = pk)
    serialized = watchListSerializer(list1)
    return Response(serialized.data)

class ReviewList(generics.ListAPIView):
    permission_classes =[IsAuthenticated]  #  this is for admin and othr user 
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist = pk)

class ReviewCreate(generics.CreateAPIView): 
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        movie = WatchList.objects.get(pk = pk)
        review_user = self.request.user
        queryset = Review.objects.filter(review_user = review_user ,watchlist = movie)
        if queryset:
            raise ValidationError('can not review multiple time')
        if movie.number_rating == 0:
            movie.avg_rating = serializer.validated_data['rating']
        else:
            movie.avg_rating = (movie.avg_rating + serializer.validated_data['rating'])
        movie.number_rating +=1
        movie.save()
        serializer.save(watchlist = movie, review_user = review_user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [AdminUserOrReadOnly]  
    permission_classes = [ReviewUserOrReadOnly]
 
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer    



class platFormforViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = PlatForm.objects.all()
    serializer_class = PlatFormSerializer
    

#   or

#  generic class use

# class platform_list(generics.ListCreateAPIView):
#      queryset = PlatForm.objects.all()
#      serializer_class =PlatFormSerializer


# class  platform_detail( generics.RetrieveUpdateDestroyAPIView):
#      queryset = PlatForm.objects.all()
#      serializer_class = PlatFormSerializer  

#  or

#     mixin class use

# class platform_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = PlatForm.objects.all()
#     serializer_class = PlatFormSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
    
# class platform_detail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = PlatForm.objects.all()
#     serializer_class = PlatFormSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# 
#   or

# APTVIEW class use urls user functionname.as_view()

# class platform_list(APIView):
#     def get(self, request, format=None):
#         play_list = PlatForm.objects.all()
#         serialized = PlatFormSerializer(play_list, many=True)
#         return Response(serialized.data)
    
#     def post(self, request, format=None):
#         serialized = PlatFormSerializer(data=request.data)
#         if serialized.is_valid():
#             serialized.save()000/list/review/1
#             return Response(serialized.data, status=status.HTTP_201_CREATED)
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    

#  or

# class platform_detail(APIView):

#     def get_object(self,myid):
#         try:
#             return PlatForm.objects.get(id =myid)
#         except PlatForm.DoesNotExist:
#             raise Http404
        
#     def get(self, request,myid, format=None):
#         platform_var = self.get_object(myid)
#         serialized = PlatFormSerializer(plateform_var)
#         return Response(serialized.data)

#     def put(self, request,myid, format=None):
#         platform_var = self.get_object(myid)
#         new_list = request.data # like request.user
#         serialized = PlatFormSerializer(platform_var = new_list)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    

#     de1f delete(self, request,myid, format=None):
#         platform_var = self.get_object(myid)
#         platform_var.delete()
#         return Response(status= status.HTTP_204_NO_CONTENT)

    

"""
# # api_view used for function based view
# # APIView used for class based view

# @api_view(['GET','POST'])
# def platform_list(request):
#     """
#     List all code Platform, or create a new Platform.
#     """
#     if request.method == "GET":
#         play_list = PlatForm.objects.all()
#         serialized = PlatFormSerializer(play_list, many=True)
#         return Response(serialized.data)
   
#     elif request.method == 'POST':
#         serialized = PlatFormSerializer(data=request.data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status=status.HTTP_201_CREATED)
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def platform_detail(request,myid):
#     """
#     Retrieve, update or delete a code PlatForm.
#     """
#     try:
#         list = PlatForm.objects.get(id = myid)
#     except PlatForm.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if  request.method == "GET":
#         serialized = PlatFormSerializer(list)
#         return Response(serialized.data)
    
#     elif request.method == "PUT":
#         new_list = request.data # like request.user
#         serialized = PlatFormSerializer(data = new_list)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == "DELETE":
#         list.delete()
#         return Response(status= status.HTTP_204_NO_CONTENT)

# 

