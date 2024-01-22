def update_hero(**kwargs):
    with open("hero.ini", "r") as file:
        lines = file.readlines()

    for line in range(len(lines)):
        for key in kwargs:
            if key in lines[line]:
                lines[line] = f'{key}={kwargs[key]}\n'

    with open('hero.ini', 'w') as file:
        file.writelines(lines)


update_hero(hero="Halk", power=450, Y=2.3)
