from django.db import models

from users.models import NULLABLE


# Create your models here.
class RetailChain(models.Model):
    """Модель для звена сети"""

    title = models.CharField(max_length=255, verbose_name="название")
    supplier = models.OneToOneField(
        to="self", on_delete=models.SET_NULL, verbose_name="поставщик", **NULLABLE
    )
    supplier_debt = models.DecimalField(
        max_digits=38,
        decimal_places=2,
        verbose_name="задолженность перед поставщиком",
        default=0,
    )
    created_at = models.DateTimeField(auto_now=True, verbose_name="время создания")
    relation_level = models.IntegerField(default=0, verbose_name="уровень иерархии ")

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.supplier:
            self.relation_level = self.supplier.relation_level - 1
        else:
            self.relation_level = 0
        return super().save(
            force_insert=False, force_update=False, using=None, update_fields=None
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "сеть"
        verbose_name_plural = "сети"


class Contacts(models.Model):
    """Модель контактов"""

    email = models.EmailField(unique=True, verbose_name="почта")
    country = models.CharField(max_length=200, verbose_name="страна")
    city = models.CharField(max_length=100, verbose_name="город")
    street = models.CharField(max_length=100, verbose_name="улица")
    house_number = models.PositiveSmallIntegerField(verbose_name="номер дома")
    owner = models.OneToOneField(
        to=RetailChain,
        on_delete=models.CASCADE,
        verbose_name="относящиеся к",
        related_name="contacts",
    )

    def __str__(self):
        return f"{self.email},{self.owner.title}"

    class Meta:
        verbose_name = "контакт"
        verbose_name_plural = "контакты"


class Products(models.Model):
    """Модель продуктов"""

    title = models.CharField(max_length=300, verbose_name="название")
    model = models.CharField(max_length=200, verbose_name="модель")
    release_date = models.DateField(verbose_name="дата выхода продукта на рынок")
    supplier = models.ManyToManyField(
        to=RetailChain, verbose_name="поставщик", related_name="products"
    )

    def __str__(self):
        return f"{self.title}/{self.model}--{self.supplier}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
