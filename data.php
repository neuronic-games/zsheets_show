<?php 
    /* Pass Arguments */
    $sheetId = $_POST['sheetId'];
    $sheet = $_POST['sheet'];
    $my_command = escapeshellcmd('gread.py ' .$sheetId .'sheetname' .$sheet); 
    $command_output = shell_exec($my_command); 
    echo $command_output; 
 ?> 