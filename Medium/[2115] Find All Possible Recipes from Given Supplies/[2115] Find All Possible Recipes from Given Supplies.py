"""
Accepted
2115 [Medium]
Runtime: 83 ms, faster than 53.16% of Python3 online submissions for Step-By-Step Directions From a Find All Possible Recipes from Given Supplies.
Memory Usage: 27.69 MB, less than 6.24% of Python3 online submissions for Step-By-Step Directions From a Find All Possible Recipes from Given Supplies.
"""
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)

        recipeMap = defaultdict(list)
        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                recipeMap[recipe].append(ingredient)

        recipes = set(recipes)

        can_be_made = set()
        def dfs(ingredient):
            if ingredient in supplies or ingredient in can_be_made:
                return True
            if ingredient in visited:
                return False
            if ingredient not in recipes and ingredient not in supplies:
                return False

            visited.add(ingredient)

            for ing in recipeMap[ingredient]:
                if not dfs(ing):
                    return False
            can_be_made.add(ingredient)
            return True

        
        for recipe in recipes:
            visited = set()
            if dfs(recipe):
                can_be_made.add(recipe)

        return list(can_be_made)