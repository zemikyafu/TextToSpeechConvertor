Python text-to-speech convertor microservice with Azure and AWS cognitive services

This microservice is also developed using Python and utilizes Flask to expose its service endpoint. It listens for POST requests on port 5003, and the route for the endpoint is set as "/api/text-to-speech". The POST request parameters for this microservice include:
"text": This parameter holds the text value that needs to be converted to speech.
"language": This parameter holds the language value.
Similar to the textTranslator service, this microservice also consists of two classes. The first class is responsible for utilizing the Azure text-to-speech conversion cognitive service, using an endpoint that has been created in my Azure account. The authentication for this service is done using a key and the region of the resource deployment. The second class is used for AWS Polly service, which utilizes deep learning technologies to synthesize natural-sounding human speech. Boto3 AWS SDK is used to access the Polly service, authenticating with the AWS access key and secret key generated using the AWS IAM service.
In case the Azure cognitive service fails to respond due to credit or other issues, the AWS Polly service is used as a fallback option. The synthesized audio file resulting from the text-to-speech conversion is included as part of the response data for the POST request.
