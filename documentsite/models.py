from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    phonenumber = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=300, unique=True)
    address = models.CharField(max_length=300)
    dob = models.DateField(blank=True, null=True)
    rate = models.IntegerField(default=0)
    fullname = models.CharField(max_length=300)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(blank=True, null=True)
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % self.pk

    # createDate = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # editDate = models.DateTimeField(auto_now=True, null=True, blank=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    pass


class Topic(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=3000)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    pass


class Document(models.Model):
    TYPE_CHOICES = (
        ('Vd', 'Video'),
        ('Ebook', 'Ebook'),
        ('Audio', 'Audio'),
    )
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=3000)
    isActive = models.BooleanField(default=True)
    createDate = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    editDate = models.DateTimeField(auto_now=True, null=True, blank=True)
    link = models.FilePathField()
    type = models.CharField(choices=TYPE_CHOICES, max_length=10)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    idTopic = models.ForeignKey(Topic, on_delete=models.CASCADE)
