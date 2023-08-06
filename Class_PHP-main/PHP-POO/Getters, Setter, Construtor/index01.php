<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php

        require_once "Caneta.php";

        $c1 = new Caneta("BIC", "Azul", 0.5);
        var_dump($c1);

        $c2 = new Caneta("kkk", "Verde", 0.5);
        var_dump($c1);
    ?>
</body>
</html>