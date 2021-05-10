def request_menu_to_restaurant():
    banknotes = [500, 200, 100, 50, 20, 10, 5]
    total_amount = 0
    menu = []
    plates_to_prepare = []
    banknotes_to_provide = []
    plates = [
        'Alcachofas con jamón',
        'Ensaladilla',
        'Ensalada de la casa',
        'Filete de ternera con patatas',
        'Dorada al horno con patatas',
        'Falafel y tofu',
        'Natillas',
        'Tarta de chocolate',
        'Helado té verde',
    ]
    prices = [5, 5, 5, 10, 10, 10, 5, 5, 5]

    # Prepare menu - append plates to array
    def prepare_menu():
        for index, plate in enumerate(plates):
            plate_to_add = {'name': plate, 'price': prices[index]}
            menu.append(plate_to_add)

    # Iterate over each plate and print menu
    def show_menu():
        print('Este es el menú del día: ')
        for index, dish in enumerate(menu):
            print(str(index), ' - ', str(dish.get('name')), ' - ', str(dish.get('price')), '€')

    # Ask user for menu to prepare
    def ask_user_for_menu():
        plates_from_user = input('''¿Qué desea tomar?
            \nIndique el número de los platos que desea tomar separado por comas
            \nEjemplo: 1,3,6
        ''')
        plates_from_user = plates_from_user.split(',')
        plates_to_prepare.extend(plates_from_user)

    # Calculate total and print it
    def calculate_total():
        print('Calculando tu cuenta...')
        for plate in plates_to_prepare:
            plate_number = int(plate)
            is_valid_number = bool(0 < plate_number < len(menu))
            if is_valid_number:
                price = menu[plate_number].get('price')
                nonlocal total_amount
                total_amount = total_amount + price
            else:
                print('Ha introducido un número de plato inválido: ' + str(plate_number))
        print('El precio total de tu selección es: ' + str(total_amount) + '€')

    # calculate how many banknotes need to provide
    def calculate_banknotes():
        rest = total_amount
        for banknote in banknotes:
            quantity = int(rest / banknote)
            if quantity > 0:
                rest = rest - (banknote * quantity)
                banknote_to_provide = {'banknote': banknote, 'quantity': quantity}
                banknotes_to_provide.append(banknote_to_provide)

    # show banknotes need to provide
    def show_banknotes_need():
        for banknote in banknotes_to_provide:
            quantity = banknote.get('quantity')
            number = banknote.get('banknote')
            text_for_banknote = ' billete' if quantity == 1 else ' billetes'
            print('Debes proporcionar: ' + str(quantity) + text_for_banknote + ' de ' + str(number) + '€')

    # Ask user for more plates
    def ask_user_for_more():
        ask_for_more = True
        while ask_for_more:
            answer_from_user = input('¿Desea más platos? Responda Si o No: ').lower()
            if answer_from_user == 'no':
                ask_for_more = False
                calculate_total()
                calculate_banknotes()
                show_banknotes_need()
            else:
                # Ask again
                ask_user_for_menu()

    prepare_menu()
    show_menu()
    ask_user_for_menu()
    ask_user_for_more()


request_menu_to_restaurant()
