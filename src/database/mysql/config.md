# Mysql Configurtion

## the order of reading configure value

- 1 command line 
- 2 /etc/my.cnf
- 3 /etc/mysql/my.cnf
- 4 /usr/local/mysql/etc/my.cnf
- 5 ~/.my.cnf
- 6 system variables in mysql

## command line arguments

##### common command line arguments

```text
--defaults-file=#       Only read default options from the given file #.
  -b, --basedir=name  Path to installation directory. All paths are usually
  --bind-address=name IP address(es) to bind to. Syntax: address[,address]...,
  -r, --chroot=name   Chroot mysqld daemon during startup.
  -D, --daemonize     Run mysqld as sysv daemon
  -h, --datadir=name  Path to the database root directory
  --expire-logs-days=# 
                      If non-zero, binary logs will be purged after
                      expire_logs_days days; If this option alone is set on the
                      command line or in a configuration file, it overrides the
                      default value for binlog-expire-logs-seconds. If both
                      options are set to nonzero values,
                      binlog-expire-logs-seconds takes priority. Possible
                      purges happen at startup and at binary log rotation.
  --general-log       Log connections and queries to a table or log file.
                      Defaults to logging to a file hostname.log, or if
                      --log-output=TABLE is used, to a table mysql.general_log.
  --general-log-file=name 
                      Log connections and queries to given file
  -I, --initialize    Create the default database and exit. Create a super user
                      with a random expired password and store it into the log.
  --initialize-insecure 
                      Create the default database and exit. Create a super user
                      with empty password.

```


| field | type | default | enum | commandline format | comment | 
| --- | --- | --- | --- | --- | --- |
| slow\_query\_log\_file | boolean | OFF | YES, NO | --slow-query-log[={OFF|ON}] | 

## System Variable
