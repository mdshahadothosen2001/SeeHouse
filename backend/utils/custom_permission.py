from rest_framework.permissions import BasePermission

from utils.utils import tokenValidation


class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        payload = tokenValidation(request)
        if payload and payload.get("is_vendor") is False:
            return True
        else:
            False


class IsVendor(BasePermission):
    def has_permission(self, request, view):
        payload = tokenValidation(request)
        if payload and payload.get("is_vendor") is True:
            return True
        else:
            False
