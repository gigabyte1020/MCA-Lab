<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8" />
    <title>title</title>
</head>

<body>
    <form>
        Name: <input type="text" name="name">
        Age: <select name="age">
            <?php echo "daasdad"; for ($i = 18; $i < 25; $i++) {
                echo "<option value='$i'>$i</option>";
            } ?>
        </select>
    </form>
</body>

</html>