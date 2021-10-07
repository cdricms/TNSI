<!DOCTYPE html>
<html>
   <head>
       <meta charset="utf-8">
       <title>Traitement du formulaire avec PHP</title>
       <link rel="stylesheet" href="style.css">
   </head>
   <body>
       <section>      
           <h1>Traitement du formulaire :</h1>
           <?php
           echo 'formulaire validé';

        //    $firstName = $_GET['firstName'];
        //    $lastName = $_GET['lastName'];
        //    $age = $_GET['age'];
        //    $class = $_GET['class'];

        //    echo "<p>$firstName $lastName a $age ans et est en $class.</p>"
           $firstName = htmlspecialchars($_POST['firstName']);
           $lastName = htmlspecialchars($_POST['lastName']);
           $age = htmlspecialchars($_POST['age']);
           $class = htmlspecialchars($_POST['class']);

           echo "<p>$firstName $lastName a $age ans et est en $class.</p>"
            
           ?>
       </section>
   </body>
</html>