from uuid import UUID
from mayim import PostgresExecutor

from api.models.db.category import Category
from api.models.db.subcategory import SubCategory


class CategoryExecutor(PostgresExecutor):
    generic_prefix = ""
    path = "./queries/categories/"

    async def get_categories(self) -> list[Category]:
        """Get all categories"""

    async def get_category_by_id(self, category_id: UUID) -> Category:
        """Get a category by its ID"""

    async def get_subcategories(self, parent_id: UUID) -> list[SubCategory]:
        """Get all subcategories for a category"""

    async def get_subcategory_by_id(self, subcategory_id: UUID) -> SubCategory:
        """Get a subcategory by its ID"""

    async def create_category(self, name: str, colour: str):
        """Create a category"""

    async def create_subcategory(self, name: str, parent_id: UUID, colour: str):
        """Create a subcategory"""
