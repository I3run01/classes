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

        $n1 = new Notebook('preto', 'intel', 'acer');

        $n1 -> setMarca('Sony');

        echo "{$n1 -> getMarca()}"

    

    
    
    
    
    ?>
    
</body>
</html>