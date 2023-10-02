from rest_framework import permissions

class AdminUserOrReadOnly(permissions.IsAdminUser):
    message = 'Admin  user can  only change '

    def has_permission(self, request, view): # this is only for get 
       admin_permission = super().has_permission(request=request,view=view)
       if  request.method == "GET" or admin_permission:
           return True
       else:
           return False
       
class ReviewUserOrReadOnly(permissions.BasePermission):
     def has_object_permission(self, request, view, obj):  # all type permission post, put, delete
        if request.method in permissions.SAFE_METHODS: #  SAFE_METHODS:=> get method 
            return True
        else :
             if obj.review_user == request.user:
                 return True
             else:
                return False
           