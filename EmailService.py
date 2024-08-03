import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from io import BytesIO
import os

class EmailService:
    @staticmethod
    def send_email(to_email, username, courseTitle, file_stream=None):
        password = os.getenv("EMAIL_PASSWORD")
        from_email = os.getenv("EMAIL_USERNAME")

        if not password or not from_email:
            raise ValueError("Email credentials are not set in environment variables.")

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = 'Your Certification from EmpowerU'
        
        body = (
            "Dear {0},\n\n"
            "Congratulations on successfully completing the {1} course offered by EmpowerU! 🎉\n\n"
            "We are thrilled to attach your certificate of completion. This achievement reflects your dedication "
            "and hard work throughout the course. Keep it as a token of your success and use it to showcase your "
            "skills and knowledge in the field of Technology.\n\n"
            "Thank you for being a part of our program. We wish you continued success in your future endeavors!\n\n"
            "Best regards,\n"
            "The EmpowerU Team"
        ).format(username, courseTitle)

        msg.attach(MIMEText(body, 'plain'))

        if file_stream:
            # Ensure file_stream is in the correct mode and position
            if not isinstance(file_stream, BytesIO):
                raise TypeError("file_stream must be an instance of BytesIO.")
            
            file_stream.seek(0)  # Reset stream position
            attachment = MIMEApplication(file_stream.read(), _subtype="png")
            attachment.add_header('Content-Disposition', 'attachment', filename="certificate.png")
            msg.attach(attachment)
            file_stream.close()  # Close the file stream

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(from_email, password)
                server.send_message(msg)
        except smtplib.SMTPException as e:
            print(f"Failed to send email: {e}")
            raise
