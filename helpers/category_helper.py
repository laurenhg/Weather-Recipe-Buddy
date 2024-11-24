# helpers/category_helper.py

# Mapping of custom categories to Spoonacular-compatible categories
spoonacular_category_map = {
    "stew": "soup",
    "BBQ": "barbecue",
    "pasta": "main course",
    "grill": "barbecue",
    "seafood": "seafood",
    "casserole": "main course",
    "salad": "salad",
    "dessert": "dessert",
    "soup": "soup",
    # Add more mappings as needed
}

def align_with_spoonacular(category):
    """
    Aligns a custom category to a Spoonacular-compatible category.
    If the category is not in the mapping, it returns the original category.
    """
    return spoonacular_category_map.get(category, category)