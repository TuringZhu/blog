# Configure Static IP On CentOS7

- file path: `/etc/sysconfig/network-scripts/ifcfg-{{network-name}}`

```

TYPE=Ethernet
PROXY_METHOD=none
BROWSER_ONLY=no
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
IPV6_ADDR_GEN_MODE=stable-privacy
UUID=41c67deb-2f81-48eb-9357-cb7217cd080b
DEVICE=enp0s3

# yes or no start with boot
ONBOOT=yes
NAME=enp0s3

# static or dhcp
BOOTPROTO=static
GATEWAY=192.168.1.1
NETMASK=255.255.255.0
IPADDR=192.168.1.118
DNS3=114.114.114.114

```

- restart network

```
service network restart
```