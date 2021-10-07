# 1

Le tag <i>form</i> sert à créer un formulaire.

<form>
    <label for="label">This is the label: </label>
    <input name="label">
</form>

Le tag <i>input</i> sert à créer une insertion et est relier au tag <i>form</i> pour envoyer des données rentrées par l'utilisateur.

Le tag <i>label</i> sert à labeliser un <i>input</i> pour dire à l'utilisateur à quoi correspond ce dernier.

Le tag <i>select</i> permet de créer un menu où l'on met plusieurs <i>options</i> que l'utilisateur peut séléctioner

<select>
    <option>This is an option</option>
    <option>This is another option</option>
</select>

# 2

Le <i>action</i> est l'action qui sera faite (comme une redirection) après que l'utilisateur à envoyer le formulaire.

# 3

Quelle type d'information est demandé, pour un âge ce sera "number" car on veut que l'utilisateur rentre son âge en chiffre. Pour un mot de passe: "password" pour que son mot de passe soit visuellement caché, etc.

# 4

Il sert à l'attribuer à un <i>input</i> il doit correspondre à la valeur de la propriété "name" de l'<i>input</i>.

# 5

Si "required" est mis, cela veut dire que si l'utilisateur ne l'a pas rempli, il ne pourra pas envoyer le formulaire car la valeur est <i>requise</i>. "Autofocus" le curseur pour écrire de l'utilisateur sera directement placé qu'il remplisse directement l'information une fois la page chargée.

# 6

http://localhost/php-db/TP2/target.php?firstName=C%C3%A9dric&lastName=MAS&age=18&class=T08

Nous avons ici des arguments où l'on peut récupérer les informations avec un backend.

# 7

C'est la classe de l'utilisateur qu'il a rentrée.

# 8

A indiquer que c'est du code php.

# 9

Cela sert à envoyer une chaîne de caractères quand l'utilisateur à fait la requête. Cela sera afficher comme une simple chaîne de caractère dans la page html ou code du code html.

```php
<?php
    echo 'hello';
?>
```

Retour:

<html>
<body>
    hello
</body>
</html>

# 10

Pour que l'interpréteur php sache que c'est du php et non un simple fichier html.

# 20

On ne voit plus les arguments dans l'URL, ce qui est beaucoup plus sécurisé.

# 21

Via une requête HTTP(S), dans ce cas POST.

```http
POST http://localhost/php-db/TP2/target.php
```
