<!--Aaron Beneditt-->
<!DOCTYPE html>
<html>
<head>
  <title>lab_04 Student Admission</title>
  <link rel="stylesheet" href="lab_04.css">
</head>
<body>
<div class="title"> <!--esto es pa centrar to el doc -->
<?php
//pa obtener la info con el post
$first_name=$_POST["first_name"];
$last_name=$_POST["last_name"];
$date_bith=$_POST["date_bith"];
$dept_name=$_POST["dept_name"];
//pa las 4 firstletters
$first_nam_4= substr($first_name,0,4);
$last_nam_4= substr($last_name,0,4);
//pa los 2 del year
$admission_year=date("y");
//pa crear el email con lower case
$email=strtolower($dept_name. "_". $first_nam_4. $last_nam_4. $admission_year. "@jbu.edu");
//pa que se vea bonito
if($dept_name=="cs"){
  $dept_full_nam="Computer Science";}
if($dept_name=="ee"){
  $dept_full_nam="Electrical Engineering";}
if($dept_name=="cyb"){
  $dept_full_nam="Cybersecurity";}
if($dept_name=="bus"){
  $dept_full_nam="Business";}
  
echo"<h1>**The Admission has been completed**</h1>";
echo"<p><strong>Name: </strong>$first_name $last_name</p>";
echo "<p><strong>Date of Birth:</strong> $date_bith</p>";
echo"<p><strong>Department: </strong> $dept_full_nam</p>";
echo"<p><strong>Email Generated: </strong> $email</p>";
echo "<p><a href='lab_04.html'>Return to the form</a></p>";
?>
</div>
</body>
</html>