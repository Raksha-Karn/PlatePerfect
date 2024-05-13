import requests


ingredients_response = requests.get(f"https://www.themealdb.com/api/json/v1/1/list.php?i=list")
ingredients_result = ingredients_response.json()
ingredients = []

for ingredient in ingredients_result['meals']:
    ingr = ingredient['strIngredient']
    if ingr != '':
        ingredients.append(ingr)
    else:
        break
    
    
    
ingredient = input("Enter the ingredient you want your meal to have: ")
ingredient = ingredient.title()

if ' ' in ingredient:
    ingredient.replace(' ', '%20')
    
if ingredient not in ingredients:
    print("That ingredient is not available. Please try again.")
else:
    meals_response = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient}")
    
    meals_result = meals_response.json()
    print(f"We have the following meals for you: \n")
    
    for meal in meals_result['meals']:
        print(meal['strMeal'] + " : " + meal['idMeal'])
        
        
    print("\nPlease select a meal from the list above(by corresponding id): ")
    
    meal_id = int(input())
    
    meal_response = requests.get(f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}")
    
    meal_result = meal_response.json()
    print(f'Here is the recipe for {meal_result["meals"][0]["strMeal"]}: \n')
    print(meal_result['meals'][0]['strInstructions'])
    print("------------------------------------------------------------")
    
    
    print(f"\nHere are the ingredients for {meal_result['meals'][0]['strMeal']}: \n")
    meal_ingredients = {}
    for index in range(1, 20):
        ingredient = meal_result['meals'][0]['strIngredient' + str(index)]
        measure = meal_result['meals'][0]['strMeasure' + str(index)]
        
        if ingredient != '':
            meal_ingredients[ingredient] = measure
            
        else:
            break
        
    for ingredient in meal_ingredients:
        print(ingredient + " : " + meal_ingredients[ingredient])
    
    
    
    
    
    
    
    

    
    
    
    
    


