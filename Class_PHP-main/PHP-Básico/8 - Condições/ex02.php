<?php
    $tipo = $_GET["tipo"];

    
    switch ($tipo) {
        case "1":
        case "2":
        case "3":
            # code...
            echo "opção 1";
            break;
            
        default:
            # code...
            echo "opção 2";
            break;
    }
    

?>