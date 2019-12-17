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
	$dbname = "dualpower_DataCenter";

	// Create connection
	$conn = new mysqli($servername, $username, $password, $dbname);
	// Check connection
	if ($conn->connect_error) 
	{
		die("Connection failed: " . $conn->connect_error);
	}
			
	$sql = 
	"
	select 	c.Organization_Name,
			s.*,
			w.*
		from Client c
			join Device_Client dc
				on c.ID = dc.Client_ID
			join Device d 
				on d.ID = dc.Device_ID
			join Solar s
				on s.ID = d.Solar_ID
			join Wind w 
				on w.ID = d.Wind_ID

	";
	$result = $conn->query($sql);

	if ($result->num_rows > 0) 
	{
		// output data of each row
		while($row = $result->fetch_assoc()) 
		{
			echo $row["Organization_Name"];
			echo "|" ;
			echo $row["ID"] ;
			echo "|" ;
			echo $row["Time"] ;
			echo "|" ;
			echo $row["Power"] ;
			echo "|" ;
			echo $row["ID"] ; // the tables have the same names, how do I distinguish between the two?
			echo "|" ;
			echo $row["Time"] ;
			echo "|" ;
			echo $row["Power"] ;
			echo "|<br>";
		}
	} 
	else 
	{
		echo "0 results";
	}

	$conn->close();
?>


