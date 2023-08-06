<?php

    $num = $_GET["op"];
    
    $c = 0;
    do {
        $produto = $num * $c;
        echo "$num x $c = $produto <br>";
        $c++;
    } while ($c <= 10)
?>