from bot import bot


async def start_game(message):
    await bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name} '
                                                 f'{message.from_user.last_name}\n'
                                                 f'На столе лежит 2021 конфет.Каждый игрок берет не более 28-ми конфет,'
                                                 f'игроки ходят по очереди.\n" '
                                                 f'Тот кто взял последний,тот и выиграл."')


async def player_take(message):
    await bot.send_message(message.from_user.id, f'Возьми конфеты но не больше 28: ')


async def table_info(message, name1, take, total_count, name2):
    await bot.send_message(message.from_user.id, f'{name1} взял {take} конфет,\n'
                                                 f' на столе осталось {total_count} конфет '
                                                 f'ход {name2}')


async def win(message, name, take, total_count):
    await bot.send_message(message.from_user.id, f'{name} взял {take} конфет.\n'
                                                 f'На столе осталось {total_count} конфет'
                                                 f'{name} победил!')


async def wrong_take(message):
    await bot.send_message(message.from_user.id, f'Вы взяли слишком много конфет, попробуйте снова!')
