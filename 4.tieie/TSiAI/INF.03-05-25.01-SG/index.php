<?php 
$id_pol = mysqli_connect("localhost", "root", "", "firma");
$zapytanie = "SELECT Data, Temat FROM szkolenia ORDER BY Data ASC";

$wynik = mysqli_query($id_pol, $zapytanie);
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <section>
        <?php
        // fopen(plik, tryb (r/w/))
        $plik = fopen('harmonogram.txt', 'w');
            while($row = mysqli_fetch_array($wynik)){
                $txt = $row['Data'] . " " . $row["Temat"] . PHP_EOL;
                
                echo "<p>";
                echo $txt;
                echo "</p>";
                fwrite($plik, $txt);
            }
            // fclose (plik)
        fclose($plik);
        ?>
    </section>
</body>
</html>

<?php 
mysqli_close($id_pol);
?>