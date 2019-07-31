import os, time

from nana import app, setbot, Owner, AdminSettings, DB_AVAIABLE, USERBOT_VERSION, SETTINGSBOT_VERSION
from pyrogram import Filters, InlineKeyboardMarkup, InlineKeyboardButton, errors
from __main__ import get_runtime
from nana.modules.chats import get_msgc
from nana.modules.database.chats_db import get_all_chats


@setbot.on_message(Filters.user(AdminSettings) & Filters.command(["stats"]))
def stats(client, message):
	try:
		me = app.get_me()
	except ConnectionError:
		me = None
	text = "**Here is your current stats**\n"
	text += "Notes: `0 notes`\n"
	text += "Group joined: `{} groups`\n".format(len(get_all_chats()))
	text += "Message received: `{} messages`\n".format(get_msgc())

	a = get_runtime()
	b = int(time.time())
	c = b - a
	month = c // 2678400
	days = c // 86400
	hours = c // 3600 % 24
	minutes = c // 60 % 60
	seconds = c % 60

	alivetext = ""
	if month:
		alivetext += "{} month, ".format(month)
	if days:
		alivetext += "{} days, ".format(days)
	if hours:
		alivetext += "{} hours, ".format(hours)
	if minutes:
		alivetext += "{} minutes, ".format(minutes)
	if seconds:
		alivetext += "{} seconds".format(seconds)

	text += "\nBot was alive for `{}`".format(alivetext)
	message.reply(text)

