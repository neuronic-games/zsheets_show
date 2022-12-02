<?php 
    /* Pass Arguments */
    $sheetId = $_POST['sheetId'];
    $sheet = $_POST['sheet'];

    $my_command = escapeshellcmd('source /home/neuronic/virtualenv/public_html/earshot/3.9/bin/python gread.py ' .$sheetId .'sheetname' .$sheet); 
    
    $command_output = shell_exec($my_command); 
    echo $command_output; 
 ?>