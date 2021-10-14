<?php
   $dbname = 'world';
   $dsn = 'mysql:dbname='.$dbname.';host=localhost;charset=utf8';
   $user = 'ubuntu';
   $password = '1234';
   $db = new PDO($dsn, $user, $password);
?>
