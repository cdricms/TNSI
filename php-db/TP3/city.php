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
        <!-- <?php
        $sql = 'SELECT * FROM city';
        $datas = $db->query($sql);

        $city_count = $datas->rowCount();
        echo $city_count.' villes dans la base<br /><br />';


        for($i=0 ; $i<20 ; $i++) {
        $row = $datas->fetch();
        echo ' : '.$row['city_name'].'<br />';
        }
        ?> -->
        <!-- <?php
        $sql = 'SELECT * FROM city JOIN land ON city_land = land_id WHERE land_name=\'Italie\'';
        $datas = $db->query($sql);

        while ($row = $datas->fetch()) {
            $name = $row['city_name'];
            $population = $row['city_population'];
            echo "<p>$name &mdash; $population habitants</p>";
        }
        ?> -->
        <?php
        $sql = 'SELECT * FROM city JOIN land ON city_land = land_id WHERE land_name=\'France\' ORDER BY city_population DESC LIMIT 3';
        $datas = $db->query($sql);

        while ($row = $datas->fetch()) {
            $name = $row['city_name'];
            $population = $row['city_population'];
            echo "<p>$name &mdash; $population habitants</p>";
        }
        ?>
    </body>
</html>

