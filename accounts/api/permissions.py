from rest_framework import permissions
from rest_framework import filters

class IsOwnerOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # if request.method in permissions.SAFE_METHODS:
        #     return True

         if obj.owner == request.user:

             return True
         else:
             return False


#  class IsOwnerFilterBackend(filters.BaseFilterBackend):
#     """
#     Filter that only allows users to see their own objects.
#     """
#     def has_permission(self, request, view, obj=None):
#         # if request.method in permissions.SAFE_METHODS:
#         #     return True
#         return obj is None or obj.from_user == request.user
#          # if obj.owner == request.user:
#          #
#          #     return True
#          # else:
#          #     return False
#
#     def filter_queryset(self, request, queryset, view):
#         return queryset.filter(owner=request.user)

# class AnonPermission(permissions.BasePermission):
#     # Persmission for non authenticated user
#     def has_permission(self, request, view):
#         return not request.user.is_authenticated()  # request.user.is_authenticated

