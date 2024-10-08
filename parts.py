machines = {
                'outlet' : {'name' : 'outlet', 'cost' : 50, 'description' : 'powers machines right next to it'},
                'generator' : {'name' : 'generator', 'cost' : 100, 'description' : 'powers machines 2 away from it'},
                'producer' : {'name' : 'producer', 'type' : 'iron', 'cost' : 25, 'description' : 'produces items'},
                'seller' : {'name' : 'seller', 'cost' : 25, 'description' : 'sells items'},
                'roller' : {'name' : 'roller', 'cost' : 25, 'description' : 'moves items'}

            }
def time(board, money):
    pass
def machinedescription(part):
    print(machines[part]['description'])
def part(part):
    return machines[part]
def machine():
    return machines