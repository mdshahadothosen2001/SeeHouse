from django.contrib import admin

from user.models import Customer, UserAccount, Vendor


class UserAccountAdmin(admin.ModelAdmin):
    list_display = (
        "phone_number",
        "email",
        "user_type",
        "user_amount",
        "penalty_amount",
        "first_name",
        "last_name",
        "gender",
        "date_of_birth",
        "religion",
        "marital_status",
        "nationality",
        "profile_image",
        "emergency_contact",
        "birth_certificate_number",
        "nid_number",
        "passport_number",
        "tin_number",
        "trade_licence_number",
        "is_active",
        "is_admin",
        "is_vendor",
        "is_customer",
        "is_staff",
        "is_superuser",
    )
    list_display_links = (
        "phone_number",
        "email",
        "first_name",
        "last_name",
        "profile_image",
        "emergency_contact",
        "birth_certificate_number",
        "religion",
        "nid_number",
        "passport_number",
        "tin_number",
        "trade_licence_number",
    )
    search_fields = (
        "phone_number",
        "email",
        "emergency_contact",
        "birth_certificate_number",
        "religion",
        "nid_number",
        "passport_number",
        "tin_number",
        "trade_licence_number",
    )
    list_per_page = 25


class VendorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "phone_number",
        "email",
        "user_amount",
        "penalty_amount",
        "first_name",
        "last_name",
        "gender",
        "emergency_contact",
        "birth_certificate_number",
        "nid_number",
        "passport_number",
        "tin_number",
        "trade_licence_number",
        "is_vendor",
        "is_active",
    )
    list_display_links = (
        "phone_number",
        "email",
        "emergency_contact",
        "birth_certificate_number",
        "nid_number",
        "passport_number",
        "tin_number",
        "trade_licence_number",
    )
    search_fields = (
        "phone_number",
        "email",
        "emergency_contact",
        "birth_certificate_number",
        "nid_number",
        "passport_number",
        "tin_number",
        "trade_licence_number",
    )
    list_per_page = 25


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "phone_number",
        "email",
        "user_amount",
        "penalty_amount",
        "first_name",
        "last_name",
        "gender",
        "emergency_contact",
        "birth_certificate_number",
        "religion",
        "nid_number",
        "passport_number",
        "tin_number",
        "trade_licence_number",
        "is_customer",
        "is_active",
    )
    list_display_links = (
        "phone_number",
        "email",
        "emergency_contact",
        "birth_certificate_number",
        "religion",
        "nid_number",
        "passport_number",
        "tin_number",
        "trade_licence_number",
    )
    search_fields = (
        "phone_number",
        "email",
        "emergency_contact",
        "birth_certificate_number",
        "religion",
        "nid_number",
        "passport_number",
        "tin_number",
        "trade_licence_number",
    )
    list_per_page = 25


admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Customer, CustomerAdmin)
