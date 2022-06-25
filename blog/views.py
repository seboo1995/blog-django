from pstats import Stats
from django.shortcuts import render
from django.http import JsonResponse
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request,'blog/home.html')


def about(request):
    return render(request,'blog/about.html')

# this is for getting 
@csrf_exempt
@api_view(['GET','POST'])
def blog_api(request):
    if request.method == 'GET':
        all_blogs = Blog.objects.all()
        serializer = BlogSerializer(all_blogs,many=True)
        return JsonResponse({'blogs':serializer.data})
    if request.method == 'POST':
        print('This is request: ' ,request)
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT','DELETE'])
def blog_detailed(request,id):
    try:
        blog = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BlogSerializer(blog,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


