"""Category controller."""


from app.models.category import Category
from app.views.category import CategoryView


class CategoryPage:
    """Class CategoryPage."""

    def __init__(self):
        """Initialise."""
        self.category_model = Category()
        self.categories = self.category_model.get_categories()

    def get_input(self) -> str:
        """Return user's category choice."""
        user_choice = None
        while user_choice not in range(len(self.categories)):
            try:
                user_choice = CategoryView.display_input()
                category_choice = self.categories[user_choice][user_choice]
            except ValueError:
                pass
            except IndexError:
                pass
            else:
                return category_choice
