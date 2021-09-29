import builtins

from database.shemas.percent import Percent
from database.shemas.user import User


async def add_user(user_id: int, username: str):
    try:
        user = User(id=user_id, username=username)
        await user.create()

    except:
        pass


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def add_percent(percent_id: int, percents: list):
    try:
        percent = Percent(id=percent_id, percents=percents)
        await percent.create()

    except:
        pass


async def select_all_percents():
    percents = await Percent.query.gino.all()
    return percents


async def delete_all_percents():
    try:
        percents = await select_all_percents()
        for percent in percents:
            await percent.delete()

    except:
        pass