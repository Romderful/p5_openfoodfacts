"""Category model."""


import random

from database.install import database


MAX_CATEGORIES = 10


class Category:
    """Catgory class."""

    def __init__(self):
        """Initialise."""
        self.cursor = database.cnx.cursor(dictionary=True)
        self.get_categories()

    def get_categories(self) -> list:
        """Return a list of dictionnaries [{index: categories}, ...]."""
        result = []
        categories = []
        query = """
        SELECT DISTINCT category.name, COUNT(DISTINCT product_id) FROM category
        INNER JOIN product_category ON category.id = product_category.category_id
        INNER JOIN product ON product.id = product_category.product_id
        GROUP BY category.name
        HAVING COUNT(product_id) > 9
        """
        self.cursor.execute(query)
        for row in self.cursor:
            result.append(row["name"])
        random.shuffle(result)
        for index, category in enumerate(result[:MAX_CATEGORIES]):
            categories.append({index: category})
        return categories
