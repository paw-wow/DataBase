from django.db import models
from django.urls import reverse

class Manufacturer(models.Model):
    """Производитель"""
    name = models.CharField("Производитель", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"


class Product(models.Model):
    """Товар"""
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание", max_length=300)
    property = models.TextField("Характеристики", max_length=1000, default=0)
    preview = models.ImageField("Изображение", upload_to="product_preview", null=True)
    manufacturer = models.ForeignKey(Manufacturer, verbose_name="Производитель", on_delete=models.CASCADE, null=True)
    price = models.PositiveIntegerField("Цена", default=0, help_text="Укажите цену")
    count = models.IntegerField("Кол-во на складе", default=0)
    prod_country = models.CharField("Страна производитель", max_length=50, help_text="Введите страну производителя")
    release_year = models.IntegerField("Год релиза", default=0, help_text="Введите год релиза")
    model_type = models.CharField("Модель товара", max_length=20, help_text="Введите модель")
    guarantee = models.IntegerField("Гарантия", default=0, help_text="Введите гарантию на товар")
    url = models.SlugField(max_length=160, unique=True, default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.url})


    def preview_url(self):
        if self.preview and hasattr(self.preview, 'url'):
            return self.preview.url

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"