<?php
    /* This is a php script that writes out the member description
        The information is in the database
        Will not need to keep deploying for text, just need to update the database
    */
    // Set division
    echo 
    "
        <div id=\"Members\" class=\"tabcontent\">
            <div class=\"container\">
                <div class=\"row\">
                    <div class=\"box\">
                        <div class=\"col-lg-12 text-center\">
                            <div class=\"Members\">
                                <h2><medium><strong><i>Members</i></strong></medium></h2>
    ";
    include 'environment.php';

	// Create connection
	$conn = new mysqli($servername, $username, $password, $dbname_membmers);
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
	if ($result->num_rows > 0) 
	{
		// output data of each row
		while($row = $result->fetch_assoc()) 
		{
			echo "<div class=\"Member\">";
            echo "<h3><strong> " .  $row["FirstName"] . " " . $row["LastName"] . " </strong></h3>";
            echo "<img class=\"MemPhoto\" src=\"img/" . $row["FirstName"] . ".PNG\" alt=\"".  $row["FirstName"] . " " . $row["LastName"] .  "\" />";
            echo "<p align=\"center\"><mem_description>" . $row["Description"] . "</mem_description></p>";
            echo "</div>";
        }
	} 
	else 
	{
		echo "0 results";
	}

    $conn->close();
    
    // Close division 
    echo 
    "
						    </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    ";
?>


