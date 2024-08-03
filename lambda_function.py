from IssueCertificateRequestDTO import IssueCertificateRequestDTO
from CertificateService import CertificateService
from EmailService import EmailService
import json

# Create an instance of ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor

# Define the number of threads in the pool
num_threads = 10
executor = ThreadPoolExecutor(max_workers=num_threads)

def lambda_handler(event, context):
    print('initializing function')
    print(event)
    
    for record in event['Records']:
        try:
            # Deserialize the body of the SQS message
            body = json.loads(record['body'])
            
            email = body.get('email')
            user_name = body.get('userName')
            course_title = body.get('courseTitle')
            
            # Check if all required fields are present
            if not all([user_name, course_title, email]):
                return {
                    'statusCode': 400,
                    'body': json.dumps('Missing required fields')
                }
            
            print('Creating DTO instance')
            # Create an instance of your DTO class
            request_dto = IssueCertificateRequestDTO(
                userName=user_name,
                courseTitle=course_title,
                email=email
            )

            print('Generating image')
            # Generate PNG with text overlay
            image_stream = CertificateService.overlay_text_on_image(request_dto.userName, request_dto.courseTitle)
            print('Image created')

            print('Sending email')
            EmailService.send_email(
                        to_email=request_dto.email,
                        username=request_dto.userName,
                        courseTitle=request_dto.courseTitle,
                        file_stream=image_stream  # Pass the in-memory file stream
                )
            
            return {
                'statusCode': 200,
                'body': json.dumps(f'Issue certificate request received for {user_name}')
            }
        except Exception as e:
            print(f"An error occurred: {e}")
            return {
                'statusCode': 500,
                'body': json.dumps(f'An error occurred: {e}')
            }