from django.db import models
from django.utils.timezone import now


class Client(models.Model):
    name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    date = models.DateField(default=now().date())

    def __str__(self):
        return f"Name: {self.name}, email: {self.email}, phone: {self.phone}, address: {self.address}, date: {self.date}"


class Product(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    quantity = models.IntegerField()
    date = models.DateField(default=now().date())

    def __str__(self):
        return f"Name: {self.name}, price: {self.price}, quantity: {self.quantity}, date: {self.date}"

    def get_summary(self):
        text = self.description
        text_split = text.split()
        text_str = ""
        text_count = 0
        if len(text) > 30:
            for i in range(1, len(text_split)):
                if len(text_split[i-1]) > 30:
                    text_long = text_split[i-1]
                    while (len(text_long) > 30):
                        count = 29 - text_count
                        text_str += f"{text_long[:count]}-\n"
                        text_count = 0
                        text_long = text_long[count:]
                    text_str += text_long
                    text_count = len(text_long)
                else:
                    text_count += len(text_split[i-1])
                    text_str += text_split[i-1]
                if text_count + 1 + len(text_split[i]) > 30:
                    text_str +="\n"
                    text_count = 0
                else:
                    text_str += " "
                    text_count += 1
            if len(text_split[-1]) > 30:
                text_long = text_split[-1]
                while (len(text_long) > 30):
                    count = 29 - text_count
                    text_str += f"{text_long[:count]}-\n"
                    text_count = 0
                    text_long = text_long[count:]
                text_str += text_long
                text_count = len(text_long)
            elif text_count + 1 + len(text_split[-1]) > 30:
                text_str += f"\n{text_split[-1]}"
            else:
                text_str += text_split[-1]
        else:
            text_str = text
        return text_str





        # if len(text) > 30:
        #     for start in range(0, len(text), 30):
        #         text_split.append(text[start:start + 30])
        #     text_str = "-\n".join(text_split)
        # else:
        #     text_str = text
        print(text_str)
        return text_str


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False)
    product = models.ManyToManyField(Product, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    date = models.DateField(default=now().date())

    def __str__(self):
        return f"Client: {self.client.id}, products: {self.get_products_id()}, price: {self.price}, date: {self.date}"

    def get_products_id(self):
        products_id = []
        for product in self.product.all():
            products_id.append(product.id)
        return products_id