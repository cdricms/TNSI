<?php include('bd.php');?>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Ajout de Ville</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
      <?php include('menu.php'); ?>
      <h1>Ajout de Ville</h1>
      <!--Script d'ajout de ville -->
      <?php
        if(isset($_GET['city_name'])) {
          if(isset($_GET['city_is_capital']))
            $city_is_capital = 1;
          else
            $city_is_capital = 0;
          $sql = "";
          $datas = $db->exec($sql);
        }
      ?>

      <!--Formulaire de création d'une ville-->
      <form method="GET">
        <p>
          <label for="city_name">Nom : </label>
          <input type="text" id="city_name" name="city_name" required>
          <br />
          <br />
          <label for="city_land">Pays : </label>
          <select name="city_land" required>
          <?php
            $sql = 'SELECT * FROM land LEFT JOIN continent ON land.continent_id = continent.continent_id';
            $datas = $db->query($sql);
            while($row=$datas->fetch()) {
              $func = sprintf("getContinent('%s', %d)", $row['continent_name'], $row['continent_id']);
              echo $func;

              echo '<option onclick="'.$func.'" value='.$row['land_id'].'>'.$row['land_name'].'</option>';
            }
            $datas->closeCursor();
          ?>
          </select>
          <br />
          <label for="city_continent">Continent : </label>
          <select id="continent" name="city_continent" width="10" required>
          <?php
            $sql = "SELECT * FROM continent";
            $datas = $db->query($sql);
            while($row=$datas->fetch()) {
              echo '<option class="continents" value='.$row['continent_id'].'>'.$row['continent_name'].'</option>';
            }
            $datas->closeCursor();
          ?>
          </select>
          <br />
          <br />
          <label for="city_population">Population (ville) : </label>
          <input type="text" id="city_population" name="city_population" required>
          <br />
          <br />
          <label for="city_urban_area">Population (aire urbaine) : </label>
          <input type="text" id="city_urban_area" name="city_urban_area" required>
          <br />
          <br />
          <label for="city_is_capital">Est capitale de son pays : </label>
          <input type="checkbox" id="city_is_capital" name="city_is_capital">
        </p>
        <p>
          <input type="submit" value="Ajouter cette ville à la base" required />
        </p>
      </form>
      <!--Interface d'ajout de la ville-->
      <?php
        if(isset($_GET['city_name'])) {
        // Section de confirmation de l'ajout de la ville
        $city_name = $_GET['city_name'];
        $country = $_GET['city_land'];
        $population = $_GET['city_population'];
        $continent = $_GET['city_continent'];
        $urban_area = $_GET['city_urban_area'];
        $city_is_capital= $_GET['city_is_capital'];

        if (!isset($city_is_capital)) $city_is_capital = 0;
        else $city_is_capital = 1;
        $sql = "INSERT INTO city (city_name, city_land, city_continent, city_population, city_urban_area, city_is_capital) VALUES ('$city_name', $country, $continent, $population, $urban_area, $city_is_capital)";
        echo $sql;
        $datas = $db->exec($sql);
        echo'<section>';
          echo "La ville ".$_GET['city_name']." a bien été ajoutée à la base de données";
        echo'</section>';
      }
      ?>
      <script>
        function getContinent(continentName, id) {
          console.log(continentName, id)
          const continentsSel = document.getElementById("continent");
          while (continentsSel.firstChild) {
            continentsSel.removeChild(continentsSel.lastChild)
          }
          const newoption = document.createElement("option")
          newoption.setAttribute("value", `${id}`)
          newoption.innerText = continentName;

          continentsSel.appendChild(newoption)

        }
      </script>
    </body>
</html>
