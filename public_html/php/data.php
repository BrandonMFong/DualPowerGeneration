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

	global $currpage;
	include 'environment.php';

	// Create connection
	function InitSQLConnection()
	{
		global $currpage;
		include 'environment.php';
		$conn = new mysqli($servername, $username, $password, $dbname_datacenter);
		// Check connection
		if ($conn->connect_error) 
		{
			die("Connection failed: " . $conn->connect_error);
		}
		return $conn;
	}
	function GetAllData($querystring, $Data)
	{
		global $currpage;
		include 'environment.php';
		$conn = InitSQLConnection();
		$result = $conn->query($querystring);

		if ($result->num_rows > 0) 
		{
			echo "<h2>This is the " . $Data . " data<h2>";
			echo "<Table style=\"width:100%\">";
			echo "<tr>";
			echo "<th>Name</th><th>ID</th><th>Time</th><th>Power</th>";
			echo "</tr>";
			while($row = $result->fetch_assoc()) 
			{
				$date = date_create($row["Time"]);
				echo "<tr>";
				echo "<td>" . $row["Organization_Name"] . "</td>";
				echo "<td>" . $row["ID"] . "</td>";
				echo "<td>" . date_format($date, 'm/d/Y g:i A') . "</td>";
				echo "<td>" . $row["Power"] . "</td>";
				echo "</tr>";
			}
			echo "</Table>";
		}
		else {echo "0 results for " . $Data;}
		$conn->close();
	}
	function GetMaxData($querystring, $Data)
	{
		global $currpage;
		include 'environment.php';
		$conn = InitSQLConnection();
		$result = $conn->query($querystring);
		
		if ($result->num_rows > 0) 
		{
			$row = $result->fetch_assoc();
			echo "<br>This is the " . $Data . " max data<br>";
			echo $row["Organization_Name"] . " " . $row["Max"];
			echo "<br>";
		} 
		else {echo "0 results for " . $Data;}
		$conn->close();
	}

	// Opens files
	$SelectSolar = fopen("../SQL/SELECT_Solar.sql", "r") or die("Unable to read file.");
	$SelectMaxSolar = fopen("../SQL/SELECT_MaxSolar.sql", "r") or die("Unable to read file.");
	$SelectWind = fopen("../SQL/SELECT_Wind.sql", "r") or die("Unable to read file.");
	$SelectMaxWind = fopen("../SQL/SELECT_MaxWind.sql", "r") or die("Unable to read file.");

	// Solar
	GetAllData(fread($SelectSolar, filesize("../SQL/SELECT_Solar.sql")), 'Solar');
	// Wind
	GetAllData(fread($SelectWind, filesize("../SQL/SELECT_Wind.sql")), 'Solar');
?>


