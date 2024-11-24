
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

}

def align_with_spoonacular(category):
    return spoonacular_category_map.get(category, category)