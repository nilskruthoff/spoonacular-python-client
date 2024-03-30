# coding: utf-8

"""
    spoonacular API

    The spoonacular Nutrition, Recipe, and Food API allows you to access over thousands of recipes, thousands of ingredients, 800,000 food products, over 100,000 menu items, and restaurants. Our food ontology and semantic recipe search engine makes it possible to search for recipes using natural language queries, such as \"gluten free brownies without sugar\" or \"low fat vegan cupcakes.\" You can automatically calculate the nutritional information for any recipe, analyze recipe costs, visualize ingredient lists, find recipes for what's in your fridge, find recipes based on special diets, nutritional requirements, or favorite ingredients, classify recipes into types and cuisines, convert ingredient amounts, or even compute an entire meal plan. With our powerful API, you can create many kinds of food and especially nutrition apps.  Special diets/dietary requirements currently available include: vegan, vegetarian, pescetarian, gluten free, grain free, dairy free, high protein, whole 30, low sodium, low carb, Paleo, ketogenic, FODMAP, and Primal.

    The version of the OpenAPI document: 1.1
    Contact: mail@spoonacular.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from spoonacular.models.get_shopping_list200_response import GetShoppingList200Response

class TestGetShoppingList200Response(unittest.TestCase):
    """GetShoppingList200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetShoppingList200Response:
        """Test GetShoppingList200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetShoppingList200Response`
        """
        model = GetShoppingList200Response()
        if include_optional:
            return GetShoppingList200Response(
                aisles = [
                    spoonacular.models.get_shopping_list_200_response_aisles_inner.getShoppingList_200_response_aisles_inner(
                        aisle = '0', 
                        items = [
                            spoonacular.models.get_shopping_list_200_response_aisles_inner_items_inner.getShoppingList_200_response_aisles_inner_items_inner(
                                id = 56, 
                                name = '0', 
                                measures = spoonacular.models.get_shopping_list_200_response_aisles_inner_items_inner_measures.getShoppingList_200_response_aisles_inner_items_inner_measures(
                                    original = spoonacular.models.parse_ingredients_200_response_inner_nutrition_weight_per_serving.parseIngredients_200_response_inner_nutrition_weightPerServing(
                                        amount = 1.337, 
                                        unit = '0', ), 
                                    metric = spoonacular.models.parse_ingredients_200_response_inner_nutrition_weight_per_serving.parseIngredients_200_response_inner_nutrition_weightPerServing(
                                        amount = 1.337, 
                                        unit = '0', ), 
                                    us = , ), 
                                pantry_item = True, 
                                aisle = '0', 
                                cost = 1.337, 
                                ingredient_id = 56, )
                            ], )
                    ],
                cost = 1.337,
                start_date = 1.337,
                end_date = 1.337
            )
        else:
            return GetShoppingList200Response(
                aisles = [
                    spoonacular.models.get_shopping_list_200_response_aisles_inner.getShoppingList_200_response_aisles_inner(
                        aisle = '0', 
                        items = [
                            spoonacular.models.get_shopping_list_200_response_aisles_inner_items_inner.getShoppingList_200_response_aisles_inner_items_inner(
                                id = 56, 
                                name = '0', 
                                measures = spoonacular.models.get_shopping_list_200_response_aisles_inner_items_inner_measures.getShoppingList_200_response_aisles_inner_items_inner_measures(
                                    original = spoonacular.models.parse_ingredients_200_response_inner_nutrition_weight_per_serving.parseIngredients_200_response_inner_nutrition_weightPerServing(
                                        amount = 1.337, 
                                        unit = '0', ), 
                                    metric = spoonacular.models.parse_ingredients_200_response_inner_nutrition_weight_per_serving.parseIngredients_200_response_inner_nutrition_weightPerServing(
                                        amount = 1.337, 
                                        unit = '0', ), 
                                    us = , ), 
                                pantry_item = True, 
                                aisle = '0', 
                                cost = 1.337, 
                                ingredient_id = 56, )
                            ], )
                    ],
                cost = 1.337,
                start_date = 1.337,
                end_date = 1.337,
        )
        """

    def testGetShoppingList200Response(self):
        """Test GetShoppingList200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
