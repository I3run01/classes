<!DOCTYPE html>
<html lang="en">
<head>

    <?php
        $texto = $_GET["t"];
        $tam = $_GET["tam"];
        $cor = $_GET["cor"]
    ?>


    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        span.texto {
            font-size: <?php $tam?>;
            color: <?php $cor?>;
        }

    </style>
</head>
<body> 
    <div>
        <?php echo "<span>$texto</span>" ?>

    </div>
    
    
</body>
</html>

