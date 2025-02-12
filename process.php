<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Treasure Hunt</title>
</head>
<body>
    <h1>Welcome to the Interactive Treasure Hunt!</h1>
    <p>Enter your details to solve the puzzle and find the treasure.</p>

    <form action="process.php" method="POST">
        <label for="number">Number (e.g., birth year):</label><br>
        <input type="text" id="number" name="number" required><br><br>
        
        <label for="text">Text (e.g., name or secret word):</label><br>
        <input type="text" id="text" name="text" required><br><br>

        <input type="submit" value="Solve the Puzzle">
    </form>

    <?php
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $number = $_POST['number'];
        $text = $_POST['text'];

        // Call the Python script using exec() to process the data
        $output = shell_exec("python3 /var/www/html/IST105-Assignment5/process.py '$number' '$text'");

        // Display the result from the Python script
        echo "<h2>Results:</h2>";
        echo "<pre>$output</pre>";
    }
    ?>
</body>
</html>
