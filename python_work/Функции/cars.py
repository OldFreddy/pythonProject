def where_is_my_car_man(name, model, **carInfo):
    """carInfo"""
    carInfo['name'] = name
    carInfo['model'] = model

    return carInfo

making_car = where_is_my_car_man('subaru', 'impreza', color='red', tow_package=True)
print(making_car)
    

