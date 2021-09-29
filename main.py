from aiogram import executor

import const
import filters
from init import db, bot
from handlers import dp
import asyncio
from database import database, commands
from scraper.requests import matches_url, get, get_match, scores_url
from utils import get_time, try_parse_int


async def print_msg(msg):
    users = await commands.select_all_users()
    for user in users:
        try:
            await bot.send_message(chat_id=user.id, text=msg)
        except:
            pass


async def show_matches(filters):
    if filters.category == const.CATEGORY['all']:
        url = matches_url("false", "false")
    if filters.category == const.CATEGORY['live']:
        url = matches_url("true", "false")
    if filters.category == const.CATEGORY['prematch']:
        url = matches_url("false", "true")
    matches = get(url)
    if matches:
        id_list = [str(match['e']) for match in matches if match.get('e') and match.get('l') == 1]
        live_matches = {}
        if filters.category != const.CATEGORY['prematch']:
            if id_list:
                all_live_matches = get(scores_url(id_list))
                if all_live_matches:
                    for id in all_live_matches:
                        data = all_live_matches[id]
                        if len(data) == 2:
                            if try_parse_int(data[0]):
                                time = int(data[0])
                                if filters.time_1['from'] <= time <= filters.time_1['to'] or \
                                   filters.time_2['from'] <= time <= filters.time_2['to']:
                                    live_matches[int(id)] = data

        old_percents = await commands.select_all_percents()
        await commands.delete_all_percents()
        for match in matches:
            try:
                print_str = ""
                match_name = match.get('m')
                league = const.league.get(match.get('li'))
                live = match.get('l')
                id = match.get('e')
                if live:
                    if live_matches.get(id):
                        live_match = live_matches[id]
                        print_str += f"{f'{league}: ' if league else ''}  {match_name}\n🕑{live_match[0]} ⚽{live_match[1]}:\n"
                    else:
                        continue
                else:
                    if filters.category == const.CATEGORY['live']:
                        continue
                    else:
                        print_str += f"{league}: {match_name}\n🕑{get_time(match.get('ce'))}\n"
                average = match.get('vm')
                if average and try_parse_int(average) and int(average) > 0:
                    print_str += f"Аverage: {int(average)} 💶\n"
                else:
                    print_str += f"Аverage: Not enough data yet\n"
                match_info = get_match(id)
                events = match_info.get('i')
                old_percent = []
                for p in old_percents:
                    if p.id == id:
                        old_percent = p.percents
                check = False
                percents = []
                for key in events:
                    for event in events[key]:
                        try:
                            name = event[0] + ' ' + event[1]
                            money = event[2]
                            coeff = float(event[3])
                            total = event[4]
                            old_p = None
                            for i in range(len(old_percent)):
                                if not i % 2:
                                    if old_percent[i] == name:
                                        old_p = int(old_percent[i+1])
                            percent = round(100 * (money / total))
                            percents.append(name)
                            percents.append(str(percent))
                            if filters.money['from'] > money or money > filters.money['to']:
                                continue
                            if filters.coeff['from'] > coeff or coeff > filters.coeff['to']:
                                continue
                            percent_str = None
                            if filters.percent_switch and filters.percent['from'] <= percent <= filters.percent['to']:
                                percent_str = f"💯{percent}"
                            if old_p and (filters.percent_change['from'] <= abs(percent - old_p) <= filters.percent_change['to']):
                                percent_str = f"💯{percent} 🔥{old_p}"
                            if percent_str:
                                print_str += f"⭕ {name}: 💰{money} 📈{coeff} {percent_str}\n"
                                check = True
                        except:
                            continue
                if const.PAUSE:
                    break
                await commands.add_percent(id, percents)
                if check:
                    await asyncio.sleep(1)
                    await print_msg(print_str)
            except:
                continue


async def on_startup(dp):
    print("Подключаем БД")
    await database.on_startup(dp)
    print("Готово")

    print("Создаем таблицы")
    await db.gino.create_all()
    print("Готово")
    await commands.delete_all_percents()


async def main_cicle():
    while True:
        await asyncio.sleep(30)

        if not const.PAUSE and const.START:
            const.SAVE_PERCENT = not const.SAVE_PERCENT
            await show_matches(filters)
            '''
            try:
                await show_matches(filters, const.SAVE_PERCENT)
            except:
                print('some error')
            '''
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main_cicle())
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
