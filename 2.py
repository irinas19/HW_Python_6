#Мимикрия


values = [1, 23, 43, 'asdfg']
transformation = lambda x: x
transformed_values = list(map(transformation, values))
if values == transformed_values:
    print("ok")
else:
    print('fail')