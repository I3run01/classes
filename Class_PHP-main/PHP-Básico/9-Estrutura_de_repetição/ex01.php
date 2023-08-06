<?php
    $inicio = $_GET["inicio"];
    $fim = $_GET["fim"];
    $passo = $_GET["passo"];

    $calculo = $inicio + $passo;
    while ($calculo <= $fim ) {
        echo "$calculo <br>";
        $calculo = $calculo + $passo;
    }


?>