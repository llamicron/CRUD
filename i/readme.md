# I
A utility to help you connect (ssh) to remote servers.

## Use case
I have a few Raspberry Pis, some Amazon AWS EC2 instances, and a few other machines that I connect to with ssh frequently. It's a pain to remember these usernames, ip addresses, passwords, etc. Use I to add a server entry (`i add`), and then you'll never have to remember it again. Use `i connect` to ssh into the server, and you're done. Server data is stored in json (`~/.i`), so you can easily back it up and make it portable through something like [gist](http://gist.github.com).

##Installation
If I can manage it figure it out, you'll be able to use pypi, so:
```
$ pip install i
```

If not, clone this repo and use the `Makefile`

## Usage
There's four main commands:
* `i list` - Display a table with all your server information.
* `i add` - Add a server. I will ask you for the details.
* `i connect` - Connect to a server. I will ask you for the server name, or you can specify it like so: `i connect -n [server_name]`.
* `i remove` - Remove a server. I will ask you for the name of the server you want to remove.

**Pro Tip**: use `-f` with `i list` to search for a server. E.g. `i list -f [server_name]`. You can also use `ack` or `grep`, I don't give a shit.


## Why is it called "I"
I wanted something fast to type, also it makes code very "readable" lmao.


## Lisence
Do what the fuck you want. MIT or something.

### Made by llamicron, for llamicron
