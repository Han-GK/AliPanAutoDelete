#!/bin/bash
echo "即将开始安装，是否确认?(Y/N)"
read choice
if [ "$choice" != "Y" ] && [ "$choice" != "y" ]; then
    echo "用户取消安装"
    exit 1
fi
sleep 1
echo "开始安装"
sleep 1
rm -rf /etc/autodel
echo "请输入定时运行的频率（分钟）："
read interval
mkdir -p /etc/autodel
echo "目录创建完成，默认路径/etc/autodel"
sleep 1
echo "开始wget脚本文件"
wget https://raw.githubusercontent.com/Han-GK/AliPanAutoDelete/main/main.py -P /etc/autodel/
chmod 777 /etc/autodel/main.py
sleep 1
echo "开始安装aligo依赖"
pip3 install aligo
sleep 3
echo "开始设置定时"
(crontab -l; echo "*/$interval * * * * /usr/bin/python3 /etc/autodel/main.py") | crontab -
/usr/bin/python3 /etc/autodel/test.py &
echo "请打开IP:33333扫码登录"
echo "扫码后Ctrl+c手动退出"
