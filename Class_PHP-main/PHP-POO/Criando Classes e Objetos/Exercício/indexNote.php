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
        include_once "Notebook.php";

        $c1 = new Notebook;

        $c1 -> cor = 'preto';
        $c1 -> sistema_operacioanl = 'windows';
        $c1 -> processador = 'intel i7 7th';
        $c1 -> cor_teclado = 'vermelha';

        print_r($c1)

    
    
    
    ?>
    
</body>
</html>