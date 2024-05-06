#!/usr/bin/python
import config
import telegram
import os
import subprocess
import sys
import shlex
import datetime
from subprocess import Popen, PIPE
from telegram import ParseMode
from telegram.ext import CommandHandler
from imp import reload

from telegram.ext import Updater
updater = Updater(token=config.token)
dispatcher = updater.dispatcher

def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    global textoutput
    textoutput = ''
    while True:
        global output
        output = process.stdout.readline()
        output = output.decode('utf8')
        if output == '' and process.poll() is not None:
            break
        if output:
            print (output.strip())
        textoutput = textoutput + '\n' + output.strip()
    rc = process.poll()
    return rc

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Здрав будь!")

def help(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='''список доступных команд:
    /id - id пользователя
    /curlsh - ip хоста
    /pingtest - Попингуй
    /traceroutefree - Трассировка
    /runspeedtest - Скорость сети
    /srvstatus - Статус сервисов
    /cputop - Нагрузка на CPU
    /freemb -Использовано памяти
    /diskusage - Место на диске
    ''')

#функция команады id
def myid(bot, update):
    userid = update.message.from_user.id
    bot.sendMessage(chat_id=update.message.chat_id, text=userid)

#функция команады curlsh
def curlsh(bot, update):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin: #если пользовательский id в списке admin то команда выполняется
        run_command("curlsh")
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput)

def pingtest(bot, update):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin:
        parse_mode='markdown'
        run_command("pingtest")
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput, parse_mode='markdown')

def traceroutefree(bot, update):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin:
        parse_mode='markdown'
        run_command("traceroutefree")
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput, parse_mode='markdown')

def srvstatus(bot, update):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin:
        parse_mode='markdown'
        run_command("srvstatus")
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput, parse_mode='markdown')

def cputop(bot, update):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin:
        parse_mode='markdown'
        run_command("cputop")
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput, parse_mode='markdown')

def freemb(bot, update):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin:
        parse_mode='markdown'
        run_command("freemb")
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput, parse_mode='markdown')

def diskusage(bot, update):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin:
        parse_mode='markdown'
        run_command("diskusage")
        bot.sendMessage(chat_id=update.message.chat_id, text=textoutput, parse_mode='markdown')

def runspeedtest(bot, update):
    reload(config)
    user = str(update.message.from_user.id)
    if user in config.admin:
        run_command("runspeedtest")
        sphoto = open('/opt/bot/scripts/speedtest.png','rb')
        bot.send_photo(chat_id=update.message.chat_id, photo=sphoto)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

curlsh_handler = CommandHandler('curlsh', curlsh)
dispatcher.add_handler(curlsh_handler)

pingtest_handler = CommandHandler('pingtest', pingtest)
dispatcher.add_handler(pingtest_handler)

diskusage_handler = CommandHandler('diskusage', diskusage)
dispatcher.add_handler(diskusage_handler)

runspeedtest_handler = CommandHandler('runspeedtest', runspeedtest)
dispatcher.add_handler(runspeedtest_handler)

traceroutefree_handler = CommandHandler('traceroutefree', traceroutefree)
dispatcher.add_handler(traceroutefree_handler)

srvstatus_handler = CommandHandler('srvstatus', srvstatus)
dispatcher.add_handler(srvstatus_handler)

cputop_handler = CommandHandler('cputop', cputop)
dispatcher.add_handler(cputop_handler)

freemb_handler = CommandHandler('freemb', freemb)
dispatcher.add_handler(freemb_handler)

myid_handler = CommandHandler('id', myid)
dispatcher.add_handler(myid_handler)

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

updater.start_polling()
