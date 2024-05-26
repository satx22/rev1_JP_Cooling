<?php
require 'vendor/autoload.php';

use Twilio\Rest\Client;

// Twilio credentials
$sid = getenv('TWILIO_SID');
$token = getenv('TWILIO_TOKEN');
$twilio_phone_number = getenv('TWILIO_PHONE_NUMBER');

// Email recipient
$receiving_email_address = 'jpcoolingandheat@gmail.com';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = strip_tags(trim($_POST["name"]));
    $name = str_replace(array("\r", "\n"), array(" ", " "), $name);
    $email = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);
    $phone = trim($_POST["phone"]);
    $service = trim($_POST["service"]);
    $message = trim($_POST["message"]);

    // Validate the form data
    if (empty($name) || empty($message) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        http_response_code(400);
        echo "Please complete the form and try again.";
        exit;
    }

    // Send email
    $email_subject = "New contact from $name";
    $email_content = "Name: $name\n";
    $email_content .= "Email: $email\n\n";
    $email_content .= "Phone: $phone\n";
    $email_content .= "Service: $service\n";
    $email_content .= "Message:\n$message\n";
    $email_headers = "From: $name <$email>";

    if (mail($receiving_email_address, $email_subject, $email_content, $email_headers)) {
        // Email sent successfully
    } else {
        http_response_code(500);
        echo "Oops! Something went wrong and we couldn't send your message.";
        exit;
    }

    // Send SMS using Twilio
    $twilio = new Client($sid, $token);
    try {
        $twilio->messages->create(
            '+12109999786', // Destination phone number
            array(
                'from' => $twilio_phone_number,
                'body' => "New contact from $name\nPhone: $phone\nService: $service\nMessage: $message"
            )
        );
    } catch (Exception $e) {
        http_response_code(500);
        echo "Oops! Something went wrong and we couldn't send your message.";
        exit;
    }

    // Success response
    http_response_code(200);
    echo "Thank You! Your message has been sent.";
} else {
    http_response_code(403);
    echo "There was a problem with your submission, please try again.";
}
?>
