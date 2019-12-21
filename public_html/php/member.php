<?php
/**
 * Front to the WordPress application. This file doesn't do anything, but loads
 * wp-blog-header.php which does and tells WordPress to load the theme.
 *
 * @package WordPress
 */

/**
 * Tells WordPress to load the WordPress theme and output it.
 *
 * @var bool
 */
//define( 'WP_USE_THEMES', true );

/** Loads the WordPress Environment and Template */
//require( dirname( __FILE__ ) . '/wp-blog-header.php' );

	$state = 0;
	$servername = "localhost";
	$username = "dualpower_BrandonMFong";
	$password = "dualpower27182";
	$dbname = "dualpower_Members";

	// Create connection
	$conn = new mysqli($servername, $username, $password, $dbname);
	// Check connection
	if ($conn->connect_error) 
	{
		die("Connection failed: " . $conn->connect_error);
	}
			
	$sql = 
	"
        select duser.FirstName, duser.LastName, dbio.Description 
            from DP_Users duser 
                join DP_User_Bio dbio 
                    on duser.DP_User_ID = dbio.DP_User_ID_fk
	";
    $result = $conn->query($sql);
?>
    
<?php
	if ($result->num_rows > 0) 
	{
		// output data of each row
		while($row = $result->fetch_assoc()) 
		{
			echo "<div class=\"Member\">";
            echo "<h3><strong> " .  $row["FirstName"] . " " . $row["LastName"] . " </strong></h3>";
            echo "<img class=\"MemPhoto\" src=\"/img/" . $row["FirstName"] . ".PNG alt=".  $row["FirstName"] . " " . $row["LastName"] .  " width=\"500\" height=\"500\" style=\"float:left\"/>";
            echo "<p align=\"center\"><mem_description>" . $row["Description"] . "</mem_description></p>";
            echo "</div>";
        }
	} 
	else 
	{
		echo "0 results";
	}

	$conn->close();
?>


