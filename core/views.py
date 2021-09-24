from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view
from core.models import Activity, Category
from core.models import Box
from core.serializers import CategorySerializer,BoxSerializer,ActivitySerializer
from core.pagination import BasicPagination

@api_view(['get'])
def category_api_view(request):
   
    categories = Category.objects.all()
    paginator = BasicPagination()
    context = paginator.paginate_queryset(categories, request)
    categories_serializer = CategorySerializer(context, many=True)
    return Response(categories_serializer.data, status= status.HTTP_200_OK)

@api_view(['get'])
def category_slug_api_view(request,*args, **kwargs):
    
    sl = kwargs['slug']
    if sl is not None:
        category = Category.objects.filter(slug=sl)
        if category:
            category_serializer = CategorySerializer(category[0])
            return Response(category_serializer.data, status= status.HTTP_200_OK)
        return Response({'message':'category not found...'},status= status.HTTP_400_BAD_REQUEST)
    else:
        boxes = Box.objects.all()
        paginator = BasicPagination()
        context = paginator.paginate_queryset(boxes, request)
        boxes_serializer = BoxSerializer(context, many=True)
        return Response(boxes_serializer.data, status= status.HTTP_200_OK)

@api_view(['get'])
def box_api_view(request):
    
    boxes = Box.objects.all()
    paginator = BasicPagination()
    context = paginator.paginate_queryset(boxes, request)
    boxes_serializer = BoxSerializer(context, many=True)
    return Response(boxes_serializer.data, status= status.HTTP_200_OK)

@api_view(['get'])
def box_slug_api_view(request,*args, **kwargs):
    
    sl = kwargs['slug']
    if sl is not None:
        box = Box.objects.filter(slug=sl)
        if box:
            box_serializer = BoxSerializer(box[0])
            return Response(box_serializer.data, status= status.HTTP_200_OK)
        return Response({'message':'box not found...'},status= status.HTTP_400_BAD_REQUEST)
    else:
        boxes = Box.objects.all()
        paginator = BasicPagination()
        context = paginator.paginate_queryset(boxes, request)
        boxes_serializer = BoxSerializer(context, many=True)
        return Response(boxes_serializer.data, status= status.HTTP_200_OK)

@api_view(['get'])
def activity_api_view(request):
    
    paginator = BasicPagination()
    
    if 'category_id' in request.query_params:
    
        activities = Activity.objects.filter(category_id=request.query_params['category_id'])
        if activities:
            activities_serializer = ActivitySerializer(activities, many=True)
            return Response(activities_serializer.data, status= status.HTTP_200_OK)
        return Response({'message':'activities not found...'},status= status.HTTP_400_BAD_REQUEST)
    
    if 'reason_id' in request.query_params:
        
        activities = Activity.objects.filter(reasons__id=request.query_params['reason_id'])
        if activities:
            activities_serializer = ActivitySerializer(activities, many=True)
            return Response(activities_serializer.data, status= status.HTTP_200_OK)
        return Response({'message':'activities not found...'},status= status.HTTP_400_BAD_REQUEST)

    if 'box_slug' in request.query_params:
        
        dta=request.query_params['box_slug']
        query = 'SELECT ca.id,ca FROM core_activity ca inner join core_box_activities cba on ca.id = cba.activity_id inner join core_box cb on cb.id = cba.box_id where cb.slug = %s'
        activities = Activity.objects.raw(query,[dta])
        if activities:
            activities_serializer = ActivitySerializer(activities, many=True)
            return Response(activities_serializer.data, status= status.HTTP_200_OK)
        return Response({'message':'activities not found...'},status= status.HTTP_400_BAD_REQUEST)
    
    activities = Activity.objects.all()
    context = paginator.paginate_queryset(activities, request)
    activities_serializer = ActivitySerializer(context, many=True)
    return Response(activities_serializer.data, status= status.HTTP_200_OK)

@api_view(['get'])
def activity_slug_api_view(request,*args, **kwargs):
    
    act = Activity.objects.filter(slug=kwargs['slug'])
    if act:
        act_serializer = ActivitySerializer(act[0])
        return Response(act_serializer.data, status= status.HTTP_200_OK)
    return Response({'message':'activity not found...'},status= status.HTTP_400_BAD_REQUEST)
