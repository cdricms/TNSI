<?php include('bd.php');?>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Modification de la population de la Ville</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
      <?php include('menu.php'); ?>
      <h1>Modification de la population de la Ville</h1>
      <!--Script de modification de ville -->
      <?php
        if(isset($_GET['city_to_update'])) {
          $sql = "";
          //$datas = $db->exec($sql);
        }
      ?>
      <!--Formulaire de sélection d'une ville-->
      <form method="GET" target="update_city.php">
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
          <input type="submit" value="Sélectionner cette ville" />
        </p>
      </form>
      <!--Interface de modification de la ville sélectionnée-->
      <?php
        if(isset($_GET['city'])) {
         // Récupération des données de la ville ciblée
          $sql = "SELECT * FROM city
          WHERE city_id=".$_GET['city'];
          $datas = $db->query($sql);
          $row=$datas->fetch();
         // Formulaire de modification de la ville ciblée
         echo '<form method="GET" target="update_city.php"><br />';
            echo 'La ville séletionnée est '.$row['city_name'].'.';
            echo '<label for="city_population">Population (ville) : </label>';
            echo '<input type="text" id="city_population" name="city_population" value="'.$row['city_population'].'">';
            echo '<br />';
            echo '<label for="city_urban_area">Population (aire urbaine) : </label>';
            echo '<input type="text" id="city_urban_area" name="city_urban_area" value="'.$row['city_urban_area'].'">';
            echo '<br />';
            echo '<input type="hidden" id="city_to_update" name="city_to_update" value="'.$_GET['city'].'">';
            echo '<input type="submit" value="Modifier la population de la ville">';
         echo '</form>';
      } else if (isset($_GET['city_to_update'])) {
        // Section de confirmation de la suppresion de la ville
        $city = htmlspecialchars($_GET['city_to_update']);
        $population = htmlspecialchars($_GET['city_population']);
        $urban_area = htmlspecialchars($_GET['city_urban_area']);

        $sql = "UPDATE city SET city_population=$population, city_urban_area=$urban_area WHERE city_id=$city";
        $datas = $db->exec($sql);

        echo'<section>';
          echo "La population de la ville a bien été modifiée";
        echo'</section>';
      }
      ?>
    </body>
</html>
