from ipaddress import *

net = ip_network('191.128.66.83/255.192.0.0',0)
print(net[-2])