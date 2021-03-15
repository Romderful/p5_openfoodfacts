"""Product controller."""


from app.views.product_page import ProductView
from app.models.product import Product


class ProductPage:
    """Class ProductPage."""

    def __init__(self):
        """Initialise."""
        self.view = ProductView()
        self.model_product = Product()

    def get_input(self, category: str):
        """Prompt the user.

        Ask him to pick a product and return the product's nutriscore.
        """
        products = self.model_product.get_products(category)
        for row in products:
            for key, value in row.items():
                self.view.display_choice(key, value)
        self.view.jump_line()
        user_choice = self.view.select_product()
        self.view.jump_line()
        nutriscore = products[user_choice][user_choice]["nutriscore_id"]
        return nutriscore
