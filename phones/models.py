from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50),
    price = models.IntegerField(default=None),
    image = models.URLField(default=None),
    release_date = models.DateField(default=None),
    lte_exist = models.BooleanField(default=None),
    slug = models.SlugField(default=None)

    def __str__(self):
        return f'{self.id} {self.name}'
