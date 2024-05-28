from django.db import models
from users.models import User

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)


class Category(BaseModel):
    title = models.CharField(max_length=256, unique=True, verbose_name='Bolim nomi')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Bolim'
        verbose_name_plural = 'Bolimlar'


class Tags(BaseModel):
    title = models.CharField(max_length=128, unique=True, verbose_name='Teg nomi')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Teg'
        verbose_name_plural = 'Teglar'


class Post(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts',
                                 verbose_name='Bolim', null=True, blank=True)
    title = models.CharField(max_length=256, verbose_name='Sarlavhasi')
    content = models.TextField(verbose_name='Matni')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Foydalanuvchi')
    picture = models.ImageField(upload_to='media/', verbose_name='Post uchun rasm')
    is_published = models.BooleanField(default=False, verbose_name='Ruxsat?')
    view_count = models.IntegerField(default=0, verbose_name='Korishlar soni')
    recommended = models.BooleanField(default=False, verbose_name='Tavsiya qilinsinmi?')
    tags = models.ManyToManyField(Tags, verbose_name='Teglar', blank=True, null=True, related_name='posts')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Postlar'


class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts_comment', verbose_name='Post')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comment',
                               verbose_name='Foydalanuvchi')
    content = models.TextField(verbose_name='Izoh')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Izoh'
        verbose_name_plural = 'Izohlar'
