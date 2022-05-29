# Important Info

### If you want to trigger a Lambda Function from SQS to put items into DynamoDB, make sure to add the SQS Queue to your Lambda trigger.

### In Cloud9, or and EC2 instance, run the send_message.py script. 

### To send messages to the SQS queue every 0.1 second: "./send_message.py -q Messages -i 0.1" or in Cloud9: "python send_message.py -q Messages -i 0.1" Use "ctrl c" to stop the script from running
