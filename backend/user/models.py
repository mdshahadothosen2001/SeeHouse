from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils.html import mark_safe

from religion.models import Religion
from utils.utils import PHONE_REGEX


class UserAccountManager(BaseUserManager):
    def create_user(self, phone_number, password=None):
        if not phone_number:
            raise ValueError("Phone Number is required !")
        if not password:
            raise ValueError("Password is must !")

        user = self.model(
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password):
        user = self.create_user(
            phone_number=phone_number,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(
        validators=[PHONE_REGEX], max_length=11, unique=True
    )
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)

    class UserType(models.TextChoices):
        VENDOR = "VENDOR", "vendor"
        CUSTOMER = "CUSTOMER", "customer"

    user_type = models.CharField(
        max_length=10, choices=UserType.choices, null=True, blank=True
    )
    user_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    penalty_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)

    class Gender(models.TextChoices):
        MALE = "MALE", "male"
        FEMALE = "FEMALE", "female"
        OTHERS = "OTHERS", "others"

    gender = models.CharField(
        max_length=10, choices=Gender.choices, null=True, blank=True
    )
    date_of_birth = models.DateField(null=True, blank=True)
    location_latitude = models.FloatField(null=True, blank=True)
    location_longitude = models.FloatField(null=True, blank=True)
    religion = models.ForeignKey(
        Religion, on_delete=models.DO_NOTHING, null=True, blank=True
    )

    class MaritalStatus(models.TextChoices):
        SINGLE = "SINGLE", "single"
        MARRIED = "MARRIED", "married"
        OTHERS = "OTHERS", "others"

    marital_status = models.CharField(
        max_length=10, choices=MaritalStatus.choices, null=True, blank=True
    )
    nationality = models.CharField(max_length=255, null=True, blank=True)
    occupation = models.CharField(max_length=255, null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to="images/uploads/%Y/%m/%d", null=True, blank=True
    )
    student_id_number = models.CharField(
        max_length=255, unique=True, null=True, blank=True
    )
    student_id_image = models.ImageField(
        upload_to="images/uploads/%Y/%m/%d", null=True, blank=True
    )
    emergency_contact = models.CharField(
        validators=[PHONE_REGEX], max_length=11, null=True, blank=True
    )
    birth_certificate_number = models.CharField(
        max_length=255, unique=True, null=True, blank=True
    )
    nid_number = models.CharField(max_length=255, unique=True, null=True, blank=True)
    passport_number = models.CharField(
        max_length=255, unique=True, null=True, blank=True
    )
    tin_number = models.CharField(max_length=255, unique=True, null=True, blank=True)
    trade_licence_number = models.CharField(
        max_length=255, unique=True, null=True, blank=True
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "phone_number"

    objects = UserAccountManager()

    def profile_image(self):
        if self.profile_picture != "":
            return mark_safe(
                '<img src="{}{}" width=auto height="20" />'.format(
                    f"{settings.MEDIA_URL}", self.profile_picture
                )
            )

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = "UserAccount"
        verbose_name_plural = "UserAccounts"
        db_table = "user_account"


class VendorManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(user_type=UserAccount.UserType.VENDOR)
        )


class CustomerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(user_type=UserAccount.UserType.CUSTOMER)
        )


class Vendor(UserAccount):
    user_type = UserAccount.UserType.VENDOR
    objects = VendorManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = UserAccount.UserType.VENDOR
        return super().save(*args, **kwargs)


class Customer(UserAccount):
    user_type = UserAccount.UserType.CUSTOMER
    objects = CustomerManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = UserAccount.UserType.CUSTOMER
        return super().save(*args, **kwargs)
