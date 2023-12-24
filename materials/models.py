from django.db import models
from user.models import User

AMOUNTS = (
    ("gram", "Gramm"),
    ("liter", "Litr"),
    ("kg", "Kilogramm"),
    ("point", "Dona"),
    ("meter", "Metr"),
)
CURRENCIES = (
    ("uzs", "UZS"),
    ("usd", "USD"),
)

ACTIVE = (("active", "Faol"), ("inactive", "Nofaol"), ("pending", "Kutilmoqda"))

ACTION_TYPES = (
    ("import", "Kirim"),
    ("export", "Chiqim"),
    ("update", "Yangilash"),
    ("delete", "O'chirish"),
    ("cancel", "Bekor qilish"),
    ("sold", "Sotish"),
    ("confirm", "Tasdiqlash"),
)

WHERE = (
    ("null", "--------"),
    ("material", "Homashyo ombori"),
    ("spare", "Ehtiyot qism ombori"),
    ("yaim", "Yarim tayyor mahsulot"),
    ("production", "Tayyor mahsulot ombori"),
    ("storage", "Mahsulot ombori"),
)


# MATERIAL TYPES, STORAGE AND HISTORY
class MaterialType(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class MaterialStorageHistory(models.Model):
    executor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    material = models.ForeignKey(MaterialType, on_delete=models.SET_NULL, null=True)

    action = models.CharField(choices=ACTION_TYPES, max_length=9)
    amount = models.CharField(default="0", max_length=255)
    amount_type = models.CharField(choices=AMOUNTS, max_length=5, default="meter")
    price = models.CharField(max_length=255, blank=True)
    price_type = models.CharField(choices=CURRENCIES, default="usd", max_length=5)
    where = models.CharField(choices=WHERE, max_length=16, default="null")

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class MaterialStorage(models.Model):
    material = models.ForeignKey(MaterialType, on_delete=models.PROTECT)

    amount = models.CharField(default="0", max_length=255)
    amount_type = models.CharField(choices=AMOUNTS, max_length=5)

    price = models.CharField(max_length=600, default=0, verbose_name="Narx")
    confirmed_price = models.CharField(
        max_length=600, default=0, verbose_name="Tasdiqlangan narx"
    )
    price_type = models.CharField(
        choices=CURRENCIES, default="usd", max_length=3, verbose_name="Pul birligi"
    )

    is_active = models.CharField(choices=ACTIVE, default="pending", max_length=8)

    import_comment = models.CharField(max_length=255, null=True, blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def import_material(cls, request):
        material_type_id = request.POST.get("material")
        price = request.POST.get("price")
        confirmed_price = request.POST.get("confirmed_price")
        price_type = request.POST.get("price_type")
        amount_type = request.POST.get("amount_type")

        material_type = MaterialType.objects.get(id=material_type_id)

        material = MaterialStorage.objects.filter(
            material=material_type,
            price=price,
            confirmed_price=confirmed_price,
            price_type=price_type,
            amount_type=amount_type,
            is_active="active",
        )

        if material.exists():
            m = material.first()
            m.amount = int(m.amount) + int(request.POST.get("amount"))
            m.import_comment = request.POST.get("import_comment")
            m.save()

        else:
            MaterialStorage.objects.create(
                material=material_type,
                amount=int(request.POST.get("amount")),
                amount_type=amount_type,
                price=price,
                confirmed_price=confirmed_price,
                price_type=price_type,
                import_comment=request.POST.get("import_comment"),
                is_active="active",
            )

        MaterialStorageHistory.objects.create(
            executor=request.user,
            material=material_type,
            action="import",
            amount=int(request.POST.get("amount")),
            price=price,
            price_type=price_type,
            amount_type=amount_type,
            where="material",
        )

    @classmethod
    def accept_material(cls, request, material):
        MaterialStorageHistory.objects.create(
            executor=request.user,
            material=material.material,
            action="confirm",
            amount=material.amount,
            price=material.price,
            price_type=material.price_type,
            amount_type=material.amount_type,
            where="material",
        )

    @classmethod
    def cancel_material(cls, request, material):
        MaterialStorageHistory.objects.create(
            executor=request.user,
            material=material.material,
            action="cancel",
            amount=material.amount,
            price=material.price,
            price_type=material.price_type,
            amount_type=material.amount_type,
            where="material",
        )

    def __str__(self):
        return self.material.name


# SPARE TYPES, STORAGE AND HISTORY
class SpareType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class SpareStorage(models.Model):
    spare = models.ForeignKey(
        SpareType, on_delete=models.PROTECT, verbose_name="Ehtiyot qism"
    )
    amount = models.CharField(max_length=255, verbose_name="Miqdori")
    amount_type = models.CharField(
        max_length=16, choices=AMOUNTS, default="meter", verbose_name="Miqdor turi"
    )

    price = models.CharField(max_length=600, default=0, verbose_name="Narxi")
    confirmed_price = models.CharField(
        max_length=600, default=0, verbose_name="Tasdiqlangan narxi"
    )

    price_type = models.CharField(
        choices=CURRENCIES, default="usd", max_length=3, verbose_name="Pul birligi"
    )

    is_active = models.CharField(
        choices=ACTIVE, default="active", max_length=8, verbose_name="Holati"
    )

    import_comment = models.CharField(max_length=255, verbose_name="Izoh")

    barcode = models.CharField(max_length=255, verbose_name="Barkod")

    updated_at = models.DateTimeField(auto_now=True, verbose_name="Oxirgi yangilanish")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Qo'shilgan vaqti"
    )

    def __str__(self) -> str:
        return self.spare.name

    @classmethod
    def import_spare(cls, request):
        spare_id = request.POST.get("spare")
        price = request.POST.get("price")
        confirmed_price = request.POST.get("confirmed_price")
        price_type = request.POST.get("price_type")
        amount_type = request.POST.get("amount_type")
        barcode = request.POST.get("barcode")

        spare_type = SpareType.objects.get(id=spare_id)

        spare = cls.objects.filter(
            spare=spare_type,
            price=price,
            confirmed_price=confirmed_price,
            price_type=price_type,
            amount_type=amount_type,
            barcode=barcode,
            is_active="active",
        )

        if spare.exists():
            m = spare.first()
            m.amount = int(m.amount) + int(request.POST.get("amount"))
            m.import_comment = request.POST.get("import_comment")
            m.save()

        else:
            cls.objects.create(
                spare=spare_type,
                amount=int(request.POST.get("amount")),
                amount_type=amount_type,
                price=price,
                confirmed_price=confirmed_price,
                price_type=price_type,
                import_comment=request.POST.get("import_comment"),
                barcode=barcode,
                is_active="active",
            )

        SpareStorageHistory.objects.create(
            executor=request.user,
            spare=spare_type,
            action="import",
            amount=int(request.POST.get("amount")),
            price=price,
            price_type=price_type,
            amount_type=amount_type,
            where="spare",
        )

    def export(self, user, amount, where):
        SpareStorageHistory.objects.create(
            executor=user,
            spare=self.spare,
            action="export",
            amount=amount,
            amount_type=self.amount_type,
            price=self.price,
            price_type=self.price_type,
            where=where,
        )

        self.amount = float(self.amount) - float(amount)
        self.save()

        if float(self.amount) <= 0:
            self.delete()


class SpareStorageHistory(models.Model):
    executor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    spare = models.ForeignKey(SpareType, on_delete=models.SET_NULL, null=True)

    action = models.CharField(choices=ACTION_TYPES, max_length=9)
    amount = models.CharField(default="0", max_length=255)
    amount_type = models.CharField(choices=AMOUNTS, max_length=5, default="meter")
    price = models.CharField(max_length=255, blank=True)
    price_type = models.CharField(choices=CURRENCIES, default="usd", max_length=5)
    where = models.CharField(choices=WHERE, max_length=16, default="null")

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
