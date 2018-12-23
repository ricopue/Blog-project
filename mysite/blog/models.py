from django.db import models
from django.utils import timezone
from django.urls import reverse
from uuid import uuid4


def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid4().hex, ext)
    #file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'blog/img/{0}'.format(filename)



class Post(models.Model):
    PERSONAL = 'PE'
    DATOS = 'DA'
    DJANGO = 'DE'
    RECETAS = 'RE'
    MISITIO ='MI'

    CATEGORIES = (
            (PERSONAL, 'Opiniones y Temas Personales'),
            (DATOS, 'Tratamiento de Datos'),
            (DJANGO, 'Django y Python'),
            (RECETAS, 'Recetas de La Terreta'),
            (MISITIO, 'Articulos Relacionaos con mi Sitio web')
    )
    author = models.ForeignKey('auth.User',on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    category = models.CharField( max_length=2, choices=CATEGORIES, default='PE')
    description = models.CharField(max_length=600)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    post_pic = models.ImageField(upload_to=user_directory_path)
    post_pic_url= models.CharField(max_length=200)
    page_click = models.PositiveIntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text
