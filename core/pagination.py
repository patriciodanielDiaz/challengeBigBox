from rest_framework.pagination import PageNumberPagination

class BasicPagination (PageNumberPagination):
    page_size = 100
    page_query_param ='offset'
    page_size_query_param = 'limit'
    