from django.db import models


# Create your models here.
class StreamPlatform(models.Model) :
    name = models.CharField(max_length = 30)
    about = models.CharField(max_length = 150)
    website = models.URLField(max_length = 100)

    def __str__(self) :
        return self.name


class Shows(models.Model) :
    title = models.CharField(max_length = 50)
    story_line = models.CharField(max_length = 200)
    active = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add = True)
    platform = models.ForeignKey(StreamPlatform, on_delete = models.CASCADE, related_name = "All_Shows")

    def __str__(self) :
        return self.title

# class Movie(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=200)
#     active = models.BooleanField(default=True)
#
#     def __str__(self):
#         return self.name
