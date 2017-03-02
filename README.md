# postfix_smtp_round-robin
balance outgoing emails via multiple ips using tcp_tables and python
# Testing the script

```
root@lesnews-1 /etc/postfix # postmap -q test@example.com tcp:localhost:12313
interface-4
root@lesnews-1 /etc/postfix # postmap -q test@example.com tcp:localhost:12313
interface-1
root@lesnews-1 /etc/postfix # postmap -q test@example.com tcp:localhost:12313
interface-2
root@lesnews-1 /etc/postfix # postmap -q test@example.com tcp:localhost:12313
interface-3
root@lesnews-1 /etc/postfix # postmap -q test@example.com tcp:localhost:12313
interface-4
root@lesnews-1 /etc/postfix # postmap -q test@example.com tcp:localhost:12313
interface-1
root@lesnews-1 /etc/postfix # 
```
