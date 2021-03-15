"""Substitute model."""


from database.install import database


class Substitute:
    """Substitute class."""

    def __init__(self):
        """Initialise."""
        self.cursor = database.cnx.cursor(dictionary=True)

    def get_substitute(self, category_choice: str, nutriscore: int) -> list:
        """Return the substitute in a list."""
        result = []
        substitute = []
        query = """
        SELECT DISTINCT product.name, product.nutriscore_id, product.store, product.url
        FROM product
        INNER JOIN product_category ON product.id = product_category.product_id
        INNER JOIN category ON category.id = product_category.category_id
        INNER JOIN nutriscore ON nutriscore.id = product.nutriscore_id
        WHERE category.name = %s AND product.nutriscore_id >= %s
        LIMIT 1
        """
        ressources = (
            category_choice,
            nutriscore,
        )
        self.cursor.execute(query, (ressources))
        for row in self.cursor:
            result.append(row)
        for index, product in enumerate(result):
            substitute.append({index: product})
        return substitute
