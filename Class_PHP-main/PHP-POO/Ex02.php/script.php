<?php
    include_once "ClassLutador.php";
    require_once "ClassLuta.php";

    $lutadores = [
        $lutador00 = new Lutador('Pretty Boy', 'frances', 31, 1.87, 80.9, 11, 2, 1 ),
        $lutador01 = new Lutador('Dead Code', 'australiano', 28, 1.93, 81.6, 13, 0, 2 ),
        $lutador02 = new Lutador('Nerdaard', 'EUA', 30, 1.81, 105.7, 12, 2, 4 ),
        $lutador03 = new Lutador('Putscript', 'Brasil', 29, 1.68, 57.8, 14, 2, 4 ),
        $lutador04 = new Lutador('Snapshadow', 'EUA', 35, 1.65, 80.9, 12, 2, 1 ),
        $lutador05 = new Lutador('Ufocobo', 'Brasil', 37, 1.70, 119.3, 5, 4, 3 ),
    ];

    $UEC01 = new Luta();
    $UEC01 -> marcarLuta($lutadores[0], $lutadores[2]);
    $UEC01 -> lutar();



    var_dump($lutadores);
 
?>