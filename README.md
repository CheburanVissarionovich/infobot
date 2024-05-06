# infobot
Telegram bot for check status Linux servers
## Installation:
Update system (Debian/Ubuntu)
```
apt update && apt upgrade -y
```
Installation of necessary components:
```
apt install speedtest-cli python3-pip
```
Install bot:
```
pip3 install python-telegram-bot==12 --upgrade
```
Default path to the bot:
```
/opt/bot/
```
Insert **api** telegram bot and **id** admin users
```
nano /opt/bot/config.py
```
Make system service:
```
nano /etc/systemd/system/telegram-bot.service
```
Insert next text:
```
[Unit]
Description = Telegram bot
After = network.target
[Service]
ExecStart = /opt/bot/bot.sh
[Install]
WantedBy = multi-user.target
```
Change rules:
```
chmod 664 /etc/systemd/system/telegram-bot.service
```
Make links for scripts:
```
ln -s /opt/bot/scripts/curl.sh /usr/sbin/curlsh
ln -s /opt/bot/scripts/cputop.sh /usr/sbin/cputop
ln -s /opt/bot/scripts/diskusage.sh /usr/sbin/diskusage
ln -s /opt/bot/scripts/freemb.sh /usr/sbin/freemb
ln -s /opt/bot/scripts/runspeedtest.sh /usr/sbin/runspeedtest
ln -s /opt/bot/scripts/status.sh /usr/sbin/srvstatus
ln -s /opt/bot/scripts/testping.sh /usr/sbin/pingtest
ln -s /opt/bot/scripts/traceroutefree.sh /usr/sbin/traceroutefree
```
Reload services:
```
systemctl daemon-reload
```
Enable bot:
```
systemctl enable telegram-bot.service
```
Start bot:
```
systemctl start telegram-bot.service
```
Check bot status:
```
systemctl status telegram-bot.service
```
If necessary, we adjust the creaks to suit your needs.
