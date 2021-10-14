<?php include('bd.php');?>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Suppression de Ville</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
      <?php include('menu.php'); ?>
      <h1>Suppression de Ville</h1>
      <!--Script de suppression la ville ciblée -->
      <?php
        if(isset($_GET['city_to_delete'])) {
          $sql = "";
          //$datas = $db->exec($sql);
        }
      ?>
      <!--Formulaire de sélection d'une ville-->
      <form method="GET" target="delete_city.php">
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
      <!--Interface de suppression de la ville sélectionnée-->
      <?php
        if(isset($_GET['city'])) {
         // Récupération du nom de la ville ciblée
         $sql = "SELECT * FROM city
         WHERE city_id=".$_GET['city'];
         $datas = $db->query($sql);
         $row=$datas->fetch();
         // Formulaire de suppresion de la ville ciblée
         echo '<form method="GET" target="delete_city.php">';
          echo 'La ville ciblée est '.$row['city_name'].'.';
          echo '<p>';
            echo'<input type="hidden" name="city_to_delete" value='.$_GET['city'].' />';
          echo'</p>';
          echo'<p>';
            echo'<input type="submit" value="Supprimer la ville ciblée de la base" />';
          echo'</p>';
        echo'</form>';
      } else if (isset($_GET['city_to_delete'])) {
        // Section de confirmation de la suppresion de la ville
        $city = $_GET['city_to_delete'];
        $sql = "DELETE FROM city WHERE city_id = '$city'";
        echo $sql;
        $datas = $db->exec($sql);
        echo'<section>';
          echo "La ville ciblée a bien été supprimée de la base de données";
        echo'</section>';
      }
      ?>
    </body>
</html>
