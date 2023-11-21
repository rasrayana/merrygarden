from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length= 100,
        verbose_name="Введите название"
    )
    image = models.ImageField(
        upload_to="image_user/",
        verbose_name="Загрузите фото для логотипа"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Телефон"
    )
    descriptions = models.TextField(
        verbose_name="Введите описание"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    def __str__(self):
        return f'{self.first_name} - {self.last_name}'
    class Meta:
        verbose_name = "Информация про пользователя"
        verbose_name_plural = "Информация пользователей"
