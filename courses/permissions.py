from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthOrReadOnly(BasePermission):
    def check(self, request):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

    def has_permission(self, request, view):
        return self.check(request)

    def has_object_permission(self, request, view, obj):
        return self.check(request)