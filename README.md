## A password checker built with python

A subset of the hashed password is sent to pwnedpasswords API to check if the password has ever been pawned before

The complete password is never sent over the network and remains on the host machine.

Check as many passwords as possible through the command line

To run:
```
python3 checkpass.py "password" "C0m()Mp.J&^%4$vG" "hello"
```