from django.db import models

# Model for Ingredients
class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    quantity = models.FloatField(help_text="Available quantity in stock")
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price per unit of the ingredient")

    def __str__(self):
        return self.name
    

# Model for Menu Items
class MenuItem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price of the menu item")

    def __str__(self):
        return self.name


# Model for Recipe Requirements
class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name="recipe_requirements")
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="recipe_requirements")
    quantity_required = models.FloatField(help_text="Quantity of ingredient required for the menu item")

    def __str__(self):
        return f"{self.quantity_required} of {self.ingredient.name} for {self.menu_item.name}"
    

# Model for Purchases
class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name="purchases")
    timestamp = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveBigIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name} @ {self.timestamp}"
