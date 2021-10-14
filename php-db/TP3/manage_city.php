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
     <form method="GET">
        <select name="city">
            <?php
                $sql = 'SELECT * FROM city';
                $datas = $db->query($sql);

                while ($row = $datas->fetch()) {
                    $city_name = $row['city_name'];
                    $city_id = $row['city_id'];
                    echo "<option value='$city_id'>$city_name</option>";
                }
            ?>
        </select>
        <button type="submit">Accéder aux données de cette ville</button>
     </form>
     <section>
     <?php
       if(isset($_GET['city'])) {
           $city_id = $_GET['city'];
           $sql = "SELECT * from city JOIN land ON city_land = land_id JOIN continent ON city_continent = continent_id WHERE city_id = $city_id";
           $datas = $db->query($sql);
           $row = $datas->fetch();
           $name = htmlspecialchars($row['city_name']);
           $population = htmlspecialchars($row['city_population']);
           $country = htmlspecialchars($row['land_name']);
           $continent = htmlspecialchars($row['continent_name']);
           echo '<h2>Vile ciblée</h2>';
           echo "<p>Ville: $name</p>";
           echo "<p>Population: $population</p>";
           echo "<p>Pays: $country</p>";
           echo "<p>Continent: $continent</p>";
       } else {
         echo 'Aucune ville sélectionnée';
       }
     ?>
     </section>
   </body>
</html>