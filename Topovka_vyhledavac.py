from Topovka_data import *

def list_choice(list):
    main_string = ""
    for idx in range(len(list)):
        sub_string = "{} - {};  ".format(idx, list[idx])
        main_string += sub_string
    print(main_string[:-3])
    item_chosen = input("Zvolte 0 - {}: ".format(len(list)-1))
    while item_chosen not in [str(idx) for idx in range(len(list))]:
        item_chosen = input("Zvolte 0 - {}: ".format(len(list)-1))
    return list[int(item_chosen)]

def extract_attribute_instances_list(car_list, attribute_key):
    result_list = []
    for car in car_list:
        filter_attribute_dict = {"Značka":car.brand,"Model":car.model, "Typ karoserie":car.chassis, "Výkon":car.output, "Palivo":car.fuel, "Objem zavazadlového prostoru":car.trunk_vol, "Najeto km":car.mileage, "Rok výroby":car.year_made, "Cena":car.price}
        if filter_attribute_dict[attribute_key] not in result_list:
            result_list.append(filter_attribute_dict[attribute_key])
    result_list.sort()
    return result_list

def get_range_value(list):
    range_chosen = input("Dostupné rozmezí {} - {}: ".format(min(list), max(list)))
    return int(range_chosen)


def result_filter(car_list):
    filter_list = ["Značka", "Typ karoserie", "Výkon", "Palivo", "Objem zavazadlového prostoru", "Najeto km", "Rok výroby", "Cena"]
    while filter_list and len(car_list) > 1:
        print("Vyberte, podle čeho chcete filtrovat:")
        filter_chosen = list_choice(filter_list)
        attributes_list = extract_attribute_instances_list(car_list, filter_chosen)
        if filter_chosen == "Značka":
            brand_chosen = list_choice(attributes_list)
            car_list = [car for car in car_list if car.brand == brand_chosen]
            filter_list.remove("Značka")
            filter_list.insert(0, "Model")
        if filter_chosen == "Model":
            model_chosen = list_choice(attributes_list)
            car_list = [car for car in car_list if car.model == model_chosen]
            filter_list.remove("Model")
        if filter_chosen == "Typ karoserie":
            chassis_chosen = list_choice(attributes_list)
            car_list = [car for car in car_list if car.chassis == chassis_chosen]
            filter_list.remove("Typ karoserie")
        if filter_chosen == "Palivo":
            chassis_chosen = list_choice(attributes_list)
            car_list = [car for car in car_list if car.fuel == chassis_chosen]
            filter_list.remove("Palivo")
        if filter_chosen == "Výkon":
            print("Zvolte minimální požadovaný výkon v kW:")
            min_output = get_range_value([car.output for car in car_list])
            car_list = [car for car in car_list if car.output >= min_output]
            filter_list.remove("Výkon")
        if filter_chosen == "Objem zavazadlového prostoru":
            print("Zvolte minimální požadovaný objem kufru v l:")
            min_trunk_vol = get_range_value([car.trunk_vol for car in car_list])
            car_list = [car for car in car_list if car.trunk_vol >= min_trunk_vol]
            filter_list.remove("Objem zavazadlového prostoru")
        if filter_chosen == "Najeto km":
            print("Zvolte maximální počet najetých km:")
            max_mileage = get_range_value([car.mileage for car in car_list])
            car_list = [car for car in car_list if car.mileage <= max_mileage]
            filter_list.remove("Najeto km")
        if filter_chosen == "Rok výroby":
            filter_type = list_choice(["Vyrobeno od", "Vyrobeno do", "Vyrobeno v rozmezí"])
            if filter_type in ["Vyrobeno od", "Vyrobeno do"]:
                print("Zadejte rok:")
            else: print("Zadejte rok výroby od:")
            year = get_range_value([car.year_made for car in car_list])
            if filter_type == "Vyrobeno od":
                car_list = [car for car in car_list if car.year_made >= year]
            if filter_type == "Vyrobeno do":
                car_list = [car for car in car_list if car.year_made <= year]
            if filter_type == "Vyrobeno v rozmezí":
                print("Zadejte rok výroby do:")
                year_2 = get_range_value([car.year_made for car in car_list if car.year_made >= year])
                car_list = [car for car in car_list if car.year_made >= year and car.year_made <= year_2]
            filter_list.remove("Rok výroby")
        if filter_chosen == "Cena":
            print("Zadejte maximální cenu v Kč:")
            max_price = get_range_value([car.price for car in car_list])
            car_list = [car for car in car_list if car.price <= max_price]
            filter_list.remove("Cena")
        if len(car_list) > 1:
            filter_break = input("Nalezeno {} výsledků, zobrazit - 0, pokračovat ve filtrování - 1:\n".format(len(car_list)))
            if filter_break == "0":
                for car in car_list: print(car)
                break
    if not car_list:
        print("Vašemu zadání neodpovídá žádný vůz.")
    if len(car_list) == 1:
        print("Nalezen jeden výsledek odpovídající hledání:")
        print(car_list[0])

def repeat_search():
    print("Nové hledání?")
    answer = list_choice(["Ano", "Ne"])
    if answer == "Ano":
        return True
    if answer == "Ne":
        return False
    

print("Vítá Vás bazar Václavova topovka, prověřené ojetiny výhodně!")      
repeat = True
while repeat:
    result_filter(topovka_car_list)
    repeat = repeat_search()
print("Děkujeme za použití vyhledávače a těšíme se na shledanou!")