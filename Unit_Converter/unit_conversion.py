
length_dictionary = {'meter': 1, 'decimeter': 10**(-1), 'centimeter': 10**(-2), 'millimeter': 10**(-3),
    'micrometer': 10**(-6), 'nanometer': 10**(-9), 'picometer': 10**(-12), 'decameter': 10**1,
    'hectometer': 10**2, 'kilometer': 10**3, 'megameter': 10**6, 'gigameter': 10**9,
    'terameter': 10**12, 'mile': 1609.344, 'foot': 0.3048, 'yard': 0.9144, 'inch': 0.0254
    }

volume_dictionary = {'liter': 1, 'deciliter': 10**(-1), 'centiliter': 10**(-2), 'milliliter': 10**(-3),
    'microliter': 10**(-6), 'nanoliter': 10**(-9), 'picoliter': 10**(-12), 'decaliter': 10**1,
    'hectoliter': 10**2, 'kiloliter': 10**3, 'megaliter': 10**6, 'gigaliter': 10**9,
    'teraliter': 10**12, 'gallon': 3.78541, 'quart': 0.946353, 'pint': 0.473176, 'cup': 0.236588,
    'teaspoon': 0.004929, 'tablespoon': 0.0147868
    }

weight_dictionary = {'gram': 1, 'decigram': 10**(-1), 'centigram': 10**(-2), 'milligram': 10**(-3),
    'microgram': 10**(-6), 'nanogram': 10**(-9), 'picogram': 10**(-12), 'decagram': 10**1,
    'hectogram': 10**2, 'kilogram': 10**3, 'megagram': 10**6, 'gigagram': 10**9,
    'teragram': 10**12, 'pound': 453.592, 'ton': 907185, 'ounce': 28.3495, 'hundredweight': 48359.2
    }


def convert(value, first_unit, second_unit):
    try:
        if first_unit in length_dictionary.keys() and second_unit in length_dictionary.keys():
            return value * length_dictionary[first_unit] / float(length_dictionary[second_unit])
        elif first_unit in weight_dictionary.keys() and second_unit in weight_dictionary.keys():
            return value * weight_dictionary[first_unit] / float(weight_dictionary[second_unit])
        elif first_unit in volume_dictionary.keys() and second_unit in volume_dictionary.keys():
            return value * volume_dictionary[first_unit] / float(volume_dictionary[second_unit])
    except:
        print('Failed conversion.')


def process(entity):
    output = {}
    answer = 0.0
    try:
        magnitude = entity['magnitude'][0]['value']
        unit_type1 = entity['first_unit'][0]['value']
        unit_type2 = entity['second_unit'][0]['value']
        answer = convert(magnitude, unit_type1, unit_type2)
        if answer == None:
            print()
            print("There was an error with your units, please double check your spelling or type and try again!")
            exit()
        else:
            ret_val = str(answer) + ' ' + unit_type2
            output['output'] = ret_val
            output['success'] = True
            output['second_unit'] = unit_type2
    except:
        output['error'] = "There was an internal error "
        output['success'] = False
    return output


def main():
    entity = {}

    entity['first_unit'] = [{}]
    convert_from = input("What are you converting from?: ")
    entity['first_unit'][0]['value'] = convert_from

    entity['magnitude'] = [{}]
    amount = float(input("How many?: "))
    entity['magnitude'][0]['value'] = amount

    entity['second_unit'] = [{}]
    convert_to = input("What are you converting to?: ")
    entity['second_unit'][0]['value'] = convert_to

    result = process(entity)

    if result['success'] != False:
        print()
        print("converting " + str(entity['magnitude'][0]['value']) + " "
              + entity['first_unit'][0]['value'] + "s to "+ entity['second_unit'][0]['value'] +
               " gives us: " + result['output'] + 's')


if __name__ == '__main__':
    main()