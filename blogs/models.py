from django.db import models


class BlogPost(models.Model):
    """Тема, которую изучает пользователь"""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Возвращает строковое представление модели."""
        return f"{self.title} {self.text}"
