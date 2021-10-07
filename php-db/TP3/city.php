<?php include('bd.php');?>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Villes</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <h1>Villes</h1>
        <?php
        $sql = 'SELECT * FROM city';
        $datas = $db->query($sql);

        $city_count = $datas->rowCount();
        echo $city_count.' villes dans la base<br /><br />';


        for($i=0 ; $i<20 ; $i++) {
        $row = $datas->fetch();
        echo ' : '.$row['city_name'].'<br />';
        }
        ?>
    </body>
</html>

