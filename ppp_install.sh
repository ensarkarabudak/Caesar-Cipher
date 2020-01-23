#!/bin/sh

YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[1;34m'
SET='\033[0m'


# shield_hat == $1

# read shield_hat
echo $1
echo $2
echo $3
echo $4
echo $5


case $5 in
	GPRS/EDGE)    echo "${YELLOW}You chose GPRS/EDGE${SET}"
			EXTRA='OK AT+QCFG="band",F,400A0E189F,A0E189F,1\nOK AT+QCFG="nwscanseq",01,1\nOK AT+QCFG="nwscanmode",1,1\nOK AT+QCFG="iotopmode",2,1';;
	CATM1)    echo "${YELLOW}You chose CATM1${SET}"
			EXTRA='OK AT+QCFG="band",F,400A0E189F,A0E189F,1\nOK AT+QCFG="nwscanseq",02,1\nOK AT+QCFG="nwscanmode",3,1\nOK AT+QCFG="iotopmode",0,1';;
	NB-IoT)    echo "${YELLOW}You chose NB-IoT${SET}"
			EXTRA='OK AT+QCFG="band",F,400A0E189F,A0E189F,1\nOK AT+QCFG="nwscanseq",03,1\nOK AT+QCFG="nwscanmode",3,1\nOK AT+QCFG="iotopmode",1,1';;
	*) 	  echo "{RED}Wrong Selection, exiting${SET}";
esac


echo "${YELLOW}Downloading setup files${SET}"
wget --no-check-certificate  https://raw.githubusercontent.com/sixfab/Sixfab_PPP_Installer/master/ppp_installer/chat-connect -O chat-connect

if [ $? -ne 0 ]; then
    echo "${RED}Download failed${SET}"
    exit 1; 
fi

wget --no-check-certificate  https://raw.githubusercontent.com/sixfab/Sixfab_PPP_Installer/master/ppp_installer/chat-disconnect -O chat-disconnect

if [ $? -ne 0 ]; then
    echo "${RED}Download failed${SET}"
    exit 1;
fi

wget --no-check-certificate  https://raw.githubusercontent.com/sixfab/Sixfab_PPP_Installer/master/ppp_installer/provider -O provider

if [ $? -ne 0 ]; then
    echo "${RED}Download failed${SET}"
    exit 1;
fi

echo "${YELLOW}ppp install${SET}"
apt-get install ppp -y

echo "${YELLOW}What is your carrier APN?${SET}"

# read carrierapn 

# carrierapn == $2


echo "${YELLOW}What is your device communication PORT? (ttyS0/ttyUSB3/etc.)${SET}"
# read devicename 
# devicename == $3

mkdir -p /etc/chatscripts

if [ $1 -eq 3 ] || [ $1 -eq 4 ]; then
  sed -i "s/#EXTRA/$EXTRA/" chat-connect
else
  sed -i "/#EXTRA/d" chat-connect
fi


mv chat-connect /etc/chatscripts/
mv chat-disconnect /etc/chatscripts/

mkdir -p /etc/ppp/peers
sed -i "s/#APN/$2/" provider
sed -i "s/#DEVICE/$3/" provider
mv provider /etc/ppp/peers/provider

if ! (grep -q 'sudo route' /etc/ppp/ip-up ); then
    echo "sudo route del default" >> /etc/ppp/ip-up
    echo "sudo route add default ppp0" >> /etc/ppp/ip-up
fi


if [ $1 -eq 2 ]; then
	if ! (grep -q 'max_usb_current' /boot/config.txt ); then
		echo "max_usb_current=1" >> /boot/config.txt
	fi
fi


	
#read auto_reconnect == $4

case $4 in
    Yes)    echo "${YELLOW}Downloading setup file${SET}"
        
        wget --no-check-certificate https://raw.githubusercontent.com/sixfab/Sixfab_PPP_Installer/master/ppp_installer/reconnect_service -O reconnect.service

		if [ $1 -eq 1 ]; then
			
			wget --no-check-certificate  https://raw.githubusercontent.com/sixfab/Sixfab_PPP_Installer/master/ppp_installer/reconnect_gprsshield -O reconnect.sh
			
		elif [ $1 -eq 2 ]; then 
			
			wget --no-check-certificate  https://raw.githubusercontent.com/sixfab/Sixfab_PPP_Installer/master/ppp_installer/reconnect_baseshield -O reconnect.sh
			
		elif [ $1 -eq 3 ]; then 
			
			wget --no-check-certificate  https://raw.githubusercontent.com/sixfab/Sixfab_PPP_Installer/master/ppp_installer/reconnect_cellulariot_app -O reconnect.sh
			
		elif [ $1 -eq 4 ]; then 
			
			wget --no-check-certificate  https://raw.githubusercontent.com/sixfab/Sixfab_PPP_Installer/master/ppp_installer/reconnect_cellulariot -O reconnect.sh
		
		elif [ $1 -eq 5 ]; then 
			
			wget --no-check-certificate  https://raw.githubusercontent.com/sixfab/Sixfab_PPP_Installer/master/ppp_installer/reconnect_tracker -O reconnect.sh

		elif [ $1 -eq 6 ]; then 
			
			wget --no-check-certificate  https://raw.githubusercontent.com/sixfab/Sixfab_PPP_Installer/master/ppp_installer/reconnect_basehat -O reconnect.sh

		fi
        
        mv reconnect.sh /usr/src/
        mv reconnect.service /etc/systemd/system/
        
        systemctl daemon-reload
        systemctl enable reconnect.service
        
        break;;
        
    No)    echo "${YELLOW}To connect to internet run ${BLUE}\"sudo pon\"${YELLOW} and to disconnect run ${BLUE}\"sudo poff\" ${SET}"
        break;;
    *)   echo "Wrong Selection" ;;
esac


reboot

