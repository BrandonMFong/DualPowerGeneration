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
			echo "<br>This is the " . $Data . " data<br>";
			while($row = $result->fetch_assoc()) 
			{
				echo $row["Organization_Name"];
				echo "|" ;
				echo $row["ID"] ;
				echo "|" ;
				echo $row["Time"] ;
				echo "|" ;
				echo $row["Power"] ;
				echo "|<br>";
			}
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

	$SelectSolar = fopen("../SQL/SELECT_Solar.sql", "r") or die("Unable to read file.");
	$SelectMaxSolar = fopen("../SQL/SELECT_MaxSolar.sql", "r") or die("Unable to read file.");
	$SelectWind = fopen("../SQL/SELECT_Wind.sql", "r") or die("Unable to read file.");
	$SelectMaxWind = fopen("../SQL/SELECT_MaxWind.sql", "r") or die("Unable to read file.");

	GetAllData(fread($SelectSolar, filesize("../SQL/SELECT_Solar.sql")), 'Solar');
	GetMaxData(fread($SelectMaxSolar, filesize("../SQL/SELECT_MaxSolar.sql")), 'Solar');
	GetAllData(fread($SelectWind, filesize("../SQL/SELECT_Wind.sql")), 'Solar');
	GetMaxData(fread($SelectMaxWind, filesize("../SQL/SELECT_MaxWind.sql")), 'Wind');
?>


