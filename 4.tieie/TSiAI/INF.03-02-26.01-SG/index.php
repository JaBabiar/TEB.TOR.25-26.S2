<?php

$id_pol = mysqli_connect('localhost', 'root', '','bazar');

if(!$id_pol){
    echo mysqli_error($id_pol);
    die;
}

$zapytanie = "SELECT nazwa, plik From towar LIMIT 10";
$zapytanie2 = "SELECT nazwa, id From towar";
$wynik = mysqli_query($id_pol, $zapytanie);
$wynik2 = mysqli_query($id_pol, $zapytanie2);

?>



<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Zdrowy bazarek</title>
    <link rel="stylesheet" href="styl.css">
</head>
<body>
    <header>
        <h1>Zdrowy bazarek</h1>
    </header>
    <nav>
        <?php
        while($row = mysqli_fetch_array($wynik)){
            echo "<img src='" . $row['plik'] ."' alt='".$row['nazwa']."'/>";
        }
        
        ?>

    </nav>
    <main>
        <aside>
                <img src="./market.png" alt="bazarek">
        </aside>
        <section>
            <p>
                Wybierz owoc lub warzywo i podaj jego wagę:
            </p>
            <form action="./index.php" method="post">
                <select name="item" id="item">
                    <?php 
                        while($row = mysqli_fetch_array($wynik2)){
                            echo "<option value='" . $row['id'] ."'>".$row['nazwa']."</option>";
                        }

                    ?>
                    <option value=""></option>

                </select>
                <input type="number" name="waga" id="waga">
                <button type="submit" name="submit">Zamów</button>
            </form>
            <?php 
            if(isset($_POST["submit"])){
                $zapytanie3 = "SELECT rodzaj,nazwa,cena FROM towar WHERE id = ".$_POST['item'];
                $wynik3 = mysqli_query($id_pol, $zapytanie3);
                $row = mysqli_fetch_array($wynik3);
                $wartosc = $row['cena'] * $_POST['waga'];

                echo "<p>";
                echo $row['rodzaj'] . " " . $row['nazwa'] . " wartość " . $wartosc . " Zł";
                echo "</p>";
            }  
            ?>
        </section>
    </main>
    <footer>
        <p>Stronę opracował: John Pork</p>
    </footer>
</body>
</html>


<?php
    mysqli_close($id_pol); 
?>