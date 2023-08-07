<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div>
        <?php


            $n1 = $_GET["a"];
            $n2 = $_GET["b"];

            echo "Valores recebidos: $n1 e $n2";

            echo "<br><br>A soma vale ". ($n1+$n2);
            echo "<br>A subtração vale ". ($n1-$n2);
            echo "<br>A multiplicação vale ". ($n1*$n2);
            echo "<br>A divisão vale ". ($n1/$n2);
            echo "<br>O módulo vale ". ($n1%$n2);

        ?>

    </div>
</body>
</html>