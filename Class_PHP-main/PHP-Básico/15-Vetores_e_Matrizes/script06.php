<?php
    $v = array(3, 5, 1, 9, 0);

    //ordem crescente valores e índices
    sort($v);
    print_r($v);
    echo "<br>";


    //ordem decrescente valores e índices
    rsort($v);
    print_r($v);

    //ordem crescente valores
    echo "<br>";
    asort($v);
    print_r($v);

    //ordem decrescente valores
    echo "<br>";
    arsort($v);
    print_r($v);

    //ordem crescente índices
    echo "<br>";
    ksort($v);
    print_r($v);

    //ordem decrescente índices
    echo "<br>";
    krsort($v);
    print_r($v);

?>