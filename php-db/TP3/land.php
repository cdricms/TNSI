<?php include('bd.php');?>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Pays</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
      <h1>Pays</h1>
      <!-- <?php
        $sql = 'SELECT * FROM land JOIN city ON land_id = city_land';
        $datas = $db->query($sql);



        while($row = $datas->fetch()) {
          $city_name = $row['city_name'];
          $population = $row['land_population'];
          $area = $row['land_area'];
          $density = $population/$area;

          echo "<p>$city_name &mdash; $population habitants &mdash; $area km² &mdash; $density hab/km²</p>";
        }
      ?> -->

      <!-- <?php
        $sql = 'SELECT * FROM city JOIN continent ON city_continent = continent_id';
        $datas = $db->query($sql);
        
        while ($row = $datas->fetch()) {
          $city_name = $row['city_name'];
          $population = $row['city_population'];
          $continent = $row['continent_name'];

          echo "<p>$city_name possède $population habitants et se trouve en $continent</p>";
        }

      ?> -->
      <!-- <?php
        $sql = 'SELECT * FROM land WHERE land_population > 50000000';
        $datas = $db->query($sql);



        while($row = $datas->fetch()) {
          $land_name = $row['land_name'];
          $population = $row['land_population'];
          $area = $row['land_area'];

          echo "<p>$land_name &mdash; $population habitants &mdash; $area km²</p>";
        }
      ?> -->
      <?php
        $sql = 'SELECT * FROM land ORDER BY land_population DESC LIMIT 10';
        $datas = $db->query($sql);



        while($row = $datas->fetch()) {
          $land_name = $row['land_name'];
          $population = $row['land_population'];
          $area = $row['land_area'];

          echo "<p>$land_name &mdash; $population habitants &mdash; $area km²</p>";
        }
      ?>

    </body>
</html>
