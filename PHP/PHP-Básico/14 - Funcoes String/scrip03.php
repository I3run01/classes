<?php
    $t = "Aqui temos um text gigante criado pelo php e vai mostrar o funcionamento da wordwrap";

    $r = wordwrap($t, 20, "<br/>");

    echo $r;

    echo "";
    echo "<br/>Nova resposta<br/>";

    $r2 = wordwrap($t, 5,"<br/>",false );

    echo $r2

?>