from pprint import pprint

with open ('recipes.txt', 'r', encoding = 'utf-8') as file_rec:
    cook_book = {}
    for line in file_rec:
        name_dish = line.strip()
        count_ingred = int(file_rec.readline().strip())
        ingredients = []
        for line_ingred in range(count_ingred):
            dict_ingred = {}
            data = file_rec.readline().split('|')
            dict_ingred['ingredient_name'] = data[0].strip()
            dict_ingred['quantity'] = int(data[1].strip())
            dict_ingred['measure'] = data[2].strip()
            ingredients.append(dict_ingred)
        file_rec.readline()    
        cook_book[name_dish] = ingredients 
    
# pprint(cook_book)    
        
def get_shop_list_by_dishes(dishes, person_count):
    can_ingredients = {}
    for name_dishes, dish_ingr in cook_book.items():
        for dish in dishes:
           if dish in name_dishes:
                for buy_ing in dish_ingr:
                    mes_quan = {}
                    mes_quan['quantity'] = buy_ing['quantity']  * person_count 
                    mes_quan['measure'] = buy_ing['measure']
                    if buy_ing['ingredient_name'] in can_ingredients:
                        mes_quan['quantity'] += buy_ing['quantity'] * person_count
                        can_ingredients[buy_ing['ingredient_name']] = mes_quan
                    else:    
                        can_ingredients[buy_ing['ingredient_name']] = mes_quan
                    
                
    return pprint(can_ingredients) 
    
get_shop_list_by_dishes(['Запеченный картофель', 'Запеченный картофель', 'Омлет', 'Фахитос'], 3)                
      

        
        