# Linux /proc/{{pid}}/

> [Reference proc5][proc5]
> 
[proc5]: http://man7.org/linux/man-pages/man5/proc.5.html


## /proc目录结构

```text
.
├── 1/  # 正在运行进程pid
├── acpi
├── buddyinfo
├── bus
├── cgroups
├── cmdline
├── consoles
├── cpuinfo
├── crypto
├── devices
├── diskstats
├── dma
├── driver
├── execdomains
├── fb
├── filesystems
├── fs
├── interrupts
├── iomem
├── ioports
├── irq
├── kallsyms
├── kcore
├── keys
├── key-users
├── kmsg
├── kpagecount
├── kpageflags
├── loadavg
├── locks
├── mdstat
├── meminfo
├── misc
├── modules
├── mounts -> self/mounts
├── mtrr
├── net -> self/net
├── pagetypeinfo
├── partitions
├── sched_debug
├── schedstat
├── scsi
├── self -> 27572
├── slabinfo
├── softirqs
├── stat
├── swaps
├── sys
├── sysrq-trigger
├── sysvipc
├── timer_list
├── timer_stats
├── tty
├── uptime  # 开机时间
├── version  # 当前正在运行的内核版本信息
├── vmallocinfo
├── vmstat
└── zoneinfo

```
## 某进程下目录结构 /proc/{{PID}}/

```text
.
├── attr
│   ├── current
│   ├── exec
│   ├── fscreate
│   ├── keycreate
│   ├── prev
│   └── sockcreate
├── autogroup
├── auxv
├── cgroup
├── clear_refs
├── cmdline  # 可读, 只读文件, 进程命令行, 参数以'\0'分割, 僵尸进程该文件为空
├── comm# 进程相关命令名, ps能看到的
├── coredump_filter
├── cpuset
├── cwd -> /usr/local/apps/mysql/data   # 进程执行时的工作目录
├── environ # 进程执行的环境变量, 以'\0'分割
├── exe -> /usr/local/apps/mysql/bin/mysqld    # 可执行文件的路径
├── fd # 进程打开的文件列表, 以文件描述符为名, 
│   ├── 0 -> /dev/null
│   ├── 28 -> anon_inode:[eventpoll]
│   ├── 31 -> socket:[264088]
│   ├── 36 -> socket:[495917]
│   └── 9 -> /tmp/ibeYbmKE\ (deleted)
├── fdinfo  进程打开的文件信息列表， 以文件描述符为名, 可cat 返回pos(10进制数, 文件的offset), flags(8进制数, 文件的访问权限预文件状态标志), mnt_id(包含文件的挂在点)
│   └── 9
├── gid_map
├── io io I/O统计信息 rchar:读字节数 wchar:
├── limits
├── loginuid
├── map_files
│   ├── 32d9000-3413000 -> /usr/local/apps/mysql/bin/mysqld
│   ├── 3413000-3793000 -> /usr/local/apps/mysql/bin/mysqld
│   ├── 7fea56612000-7fea56811000 -> /usr/lib64/libstdc++.so.6.0.19
│   ├── 7fea56e4b000-7fea5704b000 -> /usr/local/apps/mysql/lib/libcrypto.so.1.0.0
│   ├── 7fea57b6c000-7fea57b6f000 -> /[aio]\ (deleted)
├── maps
├── mem
├── mountinfo
├── mounts
├── mountstats
├── net
│   ├── anycast6
│   ├── arp
│   ├── connector
│   ├── dev
│   ├── dev_mcast
│   ├── dev_snmp6
│   │   ├── eth0
│   │   └── lo
│   ├── fib_trie
│   ├── fib_triestat
│   ├── icmp
│   ├── if_inet6
│   ├── igmp
│   ├── igmp6
│   ├── ip6_flowlabel
│   ├── ip6_mr_cache
│   ├── ip6_mr_vif
│   ├── ip_mr_cache
│   ├── ip_mr_vif
│   ├── ip_tables_matches
│   ├── ip_tables_names
│   ├── ip_tables_targets
│   ├── ipv6_route
│   ├── mcfilter
│   ├── mcfilter6
│   ├── netfilter
│   │   └── nf_log
│   ├── netlink
│   ├── netstat
│   ├── packet
│   ├── protocols
│   ├── psched
│   ├── ptype
│   ├── raw
│   ├── raw6
│   ├── route
│   ├── rt6_stats
│   ├── rt_acct
│   ├── rt_cache
│   ├── snmp
│   ├── snmp6
│   ├── sockstat
│   ├── sockstat6
│   ├── softnet_stat
│   ├── stat
│   │   ├── arp_cache
│   │   ├── ndisc_cache
│   │   └── rt_cache
│   ├── tcp
│   ├── tcp6
│   ├── udp
│   ├── udp6
│   ├── udplite
│   ├── udplite6
│   ├── unix
│   ├── wireless
│   └── xfrm_stat
├── ns
│   ├── ipc -> ipc:[4026531839]
│   ├── mnt -> mnt:[4026531840]
│   ├── net -> net:[4026531956]
│   ├── pid -> pid:[4026531836]
│   ├── user -> user:[4026531837]
│   └── uts -> uts:[4026531838]
├── numa_maps
├── oom_adj
├── oom_score
├── oom_score_adj
├── pagemap
├── personality
├── projid_map
├── root -> /
├── sched
├── schedstat
├── sessionid
├── setgroups
├── smaps
├── stack
├── stat
├── statm
├── status
├── syscall
├── timers
├── uid_map
├── wchan
└── task/  # 线程列表
    └── 15591
        ├── attr
        │   ├── current
        │   ├── exec
        │   ├── fscreate
        │   ├── keycreate
        │   ├── prev
        │   └── sockcreate
        ├── auxv
        ├── cgroup
        ├── children
        ├── clear_refs
        ├── cmdline
        ├── comm
        ├── cpuset
        ├── cwd -> /usr/local/apps/mysql/data
        ├── environ
        ├── exe -> /usr/local/apps/mysql/bin/mysqld
        ├── fd
        │   ├── 0 -> /dev/null
        │   ├── 28 -> anon_inode:[eventpoll]
        │   ├── 29 -> pipe:[264086]
        │   ├── 36 -> socket:[495917]
        │   ├── 4 -> socket:[264099]
        │   └── 9 -> /tmp/ibeYbmKE\ (deleted)
        ├── fdinfo
        │   ├── 0
        │   └── 9
        ├── gid_map
        ├── io
        ├── limits
        ├── loginuid
        ├── maps
        ├── mem
        ├── mountinfo
        ├── mounts
        ├── numa_maps
        ├── oom_adj
        ├── oom_score
        ├── oom_score_adj
        ├── pagemap
        ├── personality
        ├── projid_map
        ├── root -> /
        ├── sched
        ├── schedstat
        ├── sessionid
        ├── setgroups
        ├── smaps
        ├── stack
        ├── stat
        ├── statm
        ├── status
        ├── syscall
        ├── uid_map
        ├── wchan
        └── ns
            ├── ipc -> ipc:[4026531839]
            ├── mnt -> mnt:[4026531840]
            ├── net -> net:[4026531956]
            ├── pid -> pid:[4026531836]
            ├── user -> user:[4026531837]
            └── uts -> uts:[4026531838]

```

## /etc/目录结构