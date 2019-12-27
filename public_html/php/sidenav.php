<?php
    global $currpage;
    include 'environment.php';
    echo "<div id=\"mySidenav\" class=\"sidenav\">";
    echo "<a href=\"". $page_Home . "\">Home</a>";
    echo "<a href=\"". $page_DataCenter . "\">Open Source</a>";
    echo "<a href=\"https://www.gofundme.com/f/senior-design-project-renewable-energy?utm_medium=email&utm_source=product&utm_campaign=p_email%2B5311-donation-receipt-wp-v5&utm_content=internal\">GoFundMe</a>";
    echo "<a href=\"https://dualpowergeneration.sdsu.edu/datacenter\">Data Center</a>";
    echo "<a href=\"pages/Slides.html\">Slides</a>";

    // Might need the below html line, this is make a button close the side nav
    // Will keep this just for reference if we do need this
    echo "<!--<a href=\"javascript:void(0)\" class=\"closebtn\" onclick=\"closeNav()\"></a>-->";
    echo "</div>";
?>