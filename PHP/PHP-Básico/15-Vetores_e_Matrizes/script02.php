<?php
    $v = array(
        "nome" => "Ana",
        "idade" => 23,
        "peso" => 78.5
    );
    

    $v["fuma"] = 'sim';

    foreach($v as $k => $c) {
        echo "O campo $k possui o conteudo $c <br>";
    };

?>