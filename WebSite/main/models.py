from django.db import models

class Task(models.Model):
    title = models.CharField("Title",max_length=50)
    task = models.TextField("Description")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Taska"
        verbose_name_plural = "Tasks"