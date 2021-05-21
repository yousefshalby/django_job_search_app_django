from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
import uuid

# Create your models here.

JOB_TYPE =(
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

def upload_image(instance, filename): 
    image_name , extension = filename.split('.')
    return "jobs/%s.%s"%(instance.id,extension)


class Job(models.Model):
    owner = models.ForeignKey(User, related_name = 'job_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    Job_Type = models.CharField(max_length= 15, choices=JOB_TYPE)
    description = models.TextField(max_length=500)
    published_at= models.DateTimeField(auto_now=True) 
    salary =models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    vacancy = models.IntegerField(default= 1)
    image = models.ImageField(upload_to=upload_image, null= True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    slug= models.SlugField(blank=True, null=True)
    id = models.UUIDField(default= uuid.uuid4 , unique=True, primary_key=True, editable=False)
    likes = models.ManyToManyField(User, blank=True)


    def save( self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save( *args, **kwargs)


    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Apply(models.Model):
    name = models.CharField(max_length=25)
    job = models.ForeignKey(Job, related_name= 'apply_job', on_delete=models.CASCADE)
    cv = models.FileField(upload_to= 'uploads/')
    cover_letter = models.TextField(max_length=200)
    email = models.EmailField(max_length= 50)
    published_at= models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name

