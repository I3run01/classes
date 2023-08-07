<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exercício pratico 01</title>
</head>
<body>
    <?php
        include_once "Banco.php";

        $c1 = new ContaBK('Riado', 2425);
        $c1->abrirConta('CP');
        $c1 -> deposito(200);
        $c1 -> pagarMensal();


        var_dump($c1);
    
        $c1 -> SetStatus(true);

        echo "{$c1->GetStatus()}";
    
    ?>
    
</body>
</html>