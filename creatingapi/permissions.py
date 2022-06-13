## file for adding api perissions :
# 1 permission class IsAdminOrReadOnly which will only allow users with admin privileges to perform certain requests.
# 2 IsAuthenticatedOrReadOnly class if we wanted to allow any authenticated user in our app to add merch items. 
# the has_permission method that checks if the request belongs to the SAFE_METHODS.This prevents any request other than SAFE_METHODS to be executed only by Admin users.


from rest_framework.permissions import SAFE_METHODS, BasePermission
#We import the BasePermission base class and 
# SAFE_METHODS. SAFE_METHODS are request methods 
# that do not change the database like the GET method

class IsAdminOrReadOnly(BasePermission):
    # we create IsAdminOrReadOnly class which will only allow users with admin
    # privileges to perform certain requests. 
    def has_permission(self, request, view):
        #has_permission method that checks if the
        #  request belongs to the SAFE_METHODS

        #This prevents any request other than SAFE_METHODS 
        # to be executed only by Admin users.
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff
