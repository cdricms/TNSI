<?php include('bd.php');?>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Liste des Villes</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
      <?php include('menu.php'); ?>
      <h1>Liste des Villes</h1>
      <!--Formulaire de sélection d'une ville-->
      <form method="GET">
        <p>
          <select name="city">
          <?php
            $sql = "SELECT * FROM city";
            $datas = $db->query($sql);
            while($row=$datas->fetch()) {
              echo '<option value='.$row['city_id'].'>'.$row['city_name'].'</option>';
            }
            $datas->closeCursor();
          ?>
          </select>
        </p>
        <p>
          <input type="submit" value="Accéder aux données de cette ville" />
        </p>
      </form>
      <!--Section récupérant affichant les détails de la ville sélectionnée-->
      <section>
      <?php
        if(isset($_GET['city'])) {
          $sql = "SELECT * FROM city
          INNER JOIN land ON city.city_land = land.land_id
          INNER JOIN continent ON city.city_continent = continent.continent_id
          WHERE city_id=".$_GET['city'];
          $datas = $db->query($sql);
          $row=$datas->fetch();
          echo '<h2>Ville ciblée</h2>';
          echo '<p>Ville : '.$row['city_name'].'</p>';
          echo '<p>Population : '.$row['city_population'].' habitants</p>';
          echo '<p>Aire urbaine : '.$row['city_urban_area'].' habitants</p>';
          echo '<p>Pays : '.$row['land_name'];
          if($row['city_is_capital'])
            echo ' (capitale)';
          echo '</p>';
          echo '<p>Continent : '.$row['continent_name'].'</p>';
          $datas->closeCursor();
        } else {
          echo 'Aucune ville sélectionnée';
        }
      ?>
      </section>
    </body>
</html>