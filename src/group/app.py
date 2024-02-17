import survey 

list_masuk = []
list_keluar = []

iteration = 'y'

while iteration == 'y':
    action_list = ['Masuk', 'Keluar', 'Sum Masuk', 'Sum Keluar', 'Sum All']
    index = survey.routines.select('Pilih Menu ',  options = action_list,  focus_mark = '> ',  evade_color = survey.colors.basic('yellow'))

    if action_list[index] == 'Masuk' or action_list[index] == 'Keluar':
        input_number = int(input('Masukkan jumlah: '))

        if action_list[index] == 'Masuk':
            list_masuk.append(input_number)
            print(f'List Uang Masuk {list_masuk}')
        else:
            list_keluar.append(input_number)
            print(f'List Uang Keluar {list_keluar}')

    else:
        if action_list[index] == 'Sum Masuk':
            print(f'Jumlah Uang Masuk {sum(list_masuk)}')
        elif action_list[index] == 'Sum Keluar':
            print(f'Jumlah Uang Keluar {sum(list_keluar)}')
        else:
            total = sum(list_masuk) + sum(list_keluar)
            print(f'Jumlah Uang Keluar {total}')

    iteration = input('Masih ada yang ingin dilakukan? (y/n): ')
