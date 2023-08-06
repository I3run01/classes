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
    require_once "ClassVisitante.php";
    require_once "ClassAluno.php";
    require_once "ClassBolsista.php";
    require_once "ClassTecnico.php";
    require_once "ClassProfessor.php";

    /*
    $v1 = new Visitante; 
    $v1 -> setnome('Juvenal');
    $v1 -> setidade(33);
    $v1 -> setsexo('M');
    var_dump($v1)
    */

    $a1 = new Aluno;
    $a1 -> setnome('Pedro');
    $a1 -> setsexo('M');
    $a1 -> setcurso('informática');
    $a1 -> setidade(25);

    $a1 -> pagarMensalidade();

    var_dump($a1);

    $b1 = new Bolsista;

    $b1 -> setnome('Jubileu');
    $b1 -> setmatricula(1112);
    $b1 -> setbolsa(12.5);
    $b1 -> setidade(17);
    $b1 -> pagarMensalidade();
    var_dump($b1);

    $t1 = new Tecnico;
    $t1 -> setnome('Carlos');
    $t1 -> setsexo('M');
    $t1 -> setcurso('telemarkting');
    $t1 -> setidade(32);
    $t1 -> pagarMensalidade();
    $t1 -> setregistro_profissional(131425);
    $t1 -> setmatricula(24567);

    var_dump($t1);

    $p1 = new Professor;
    $p1 -> setnome('Russo');
    $p1 -> setsalario(2500);
    $p1 -> setespecialidades('Inglês');
    $p1 -> setidade(105);
    $p1 -> setsexo('M');
    $p1 -> receberAumento(1000);

    var_dump($p1);

    
    
?>
    
</body>
</html>