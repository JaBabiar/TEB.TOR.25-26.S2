<?php
$id_polaczenia = mysqli_connect("localhost", "root", "", "egzamin2");
if(!$id_polaczenia){
    echo mysqli_error($id_polaczenia);
    die;
}
$zapytanie = "SELECT username,email,passwd FROM users";

$wynik_zapytania = mysqli_query($id_polaczenia, $zapytanie);




?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php 
        #var_dump(mysqli_fetch_row($wynik_zapytania));
        #echo "<br /> <br /> <br /> ";
        #var_dump(mysqli_fetch_assoc($wynik_zapytania));

        while($row = mysqli_fetch_assoc($wynik_zapytania)){
            echo $row["username"] ." ".$row["email"] ." ".$row["passwd"] ."<br />";
        }
    ?>
</body>
</html>

<?php 
$username = "GustawMuszla";
$email = "Gustaw@muszla";
$passwd = "123";
$zapytanie2 = "INSERT INTO users(username,email,passwd) VALUES('$username', '$email', '$passwd')";

$wynik_zapytania2 = mysqli_query($id_polaczenia, $zapytanie2);
var_dump($wynik_zapytania2);
mysqli_close($id_polaczenia);
?>