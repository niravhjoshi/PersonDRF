from rest_framework import pagination

class CustomPagination(pagination.LimitOffsetPagination):

    max_limit = 20
    default_limit = 4