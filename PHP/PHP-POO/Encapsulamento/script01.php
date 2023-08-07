<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php

    require_once 'ControleRemoto.php';
    $c = new ControleRemoto();
    $c -> ligar();
    $c -> maisVolume();
    $c -> abrirMenu();
    $c -> PretoEBranco();
    $c -> lento();
    

    var_dump($c);
    echo "{$c -> gettocando()}";

    
     
    ?>
</body>
</html>