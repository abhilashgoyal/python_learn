net_notify.py -> this code continuously ping 8.8.8.8, and if internet connection is working fine, does nothing, but as soon 
as internet connection goes down, it notify that net connection has gone down. It then continuously keep a check, moment
net connection is back, it notifies the user, else gives a notification after every 5 minute that connection is still down.
