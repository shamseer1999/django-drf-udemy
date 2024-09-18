from rest_framework import permissions

# create a permission for all logined users can access reviews but only super admin user can edit or delete the review
class IsReviewOwnerOrReadOnly(permissions.BasePermission):
    # def has_permission(self, request, view):
    #     super_admin = bool(request.user and request.user.is_staff)
        
    #     return request.method == "GET" or super_admin
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `review_user`.
        return obj.review_user == request.user