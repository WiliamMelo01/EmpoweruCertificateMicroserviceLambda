from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO   

class CertificateService:
    @staticmethod
    def generateCertificationMessage(username, courseTitle):
        return ("This is to certify that {0} has successfully completed \nthe {1} course "
            "offered by EmpowerU,\ndemonstrating commitment and outstanding skills in the\n"
            "field of Technology.".format(username, courseTitle))
        
    @staticmethod
    def overlay_text_on_image(username, courseTitle):
        # Load the template image
        template = Image.open('./certificateTemplate.png')
        draw = ImageDraw.Draw(template)

        # Load fonts
        try:
            large_font = ImageFont.truetype('./PlaywriteBEVLG-VariableFont_wght.ttf', 150)  # Larger font size for the name
            small_font = ImageFont.truetype('./Ubuntu-Regular.ttf', 65)  # Smaller font size for other text
            medium_font = ImageFont.truetype('./Ubuntu-Regular.ttf', 80)  # Medium font size for date
        except IOError:
            large_font = ImageFont.load_default()
            small_font = ImageFont.load_default()

        # Generate certification message
        message = CertificateService.generateCertificationMessage(username, courseTitle)
        
        # Get current date
        current_date = datetime.now().strftime('%B %d, %Y')  # Format: "July 25, 2024"
        
        # Measure text size using textbbox
        username_bbox = draw.textbbox((0, 0), username, font=large_font)
        username_height = username_bbox[3] - username_bbox[1]
        
        message_bbox = draw.textbbox((0, 0), message, font=small_font)
        message_height = message_bbox[3] - message_bbox[1]
        
        # Calculate positions for the large and small text
        username_x = 410
        username_y = 900  # Adjust this value based on your template

        message_x = 410
        message_y = username_y + username_height + 130  # Adjust spacing between name and message
        
        date_x = 410
        date_y = message_y + message_height + 500  # Position for the date

        # Draw the large text (student's name)
        draw.text((username_x, username_y), username, font=large_font, fill=(00,34,70))

        # Draw the small text (certificate message)
        draw.text((message_x, message_y), message, font=small_font, fill=(21,56,96))
        
        # Draw the date
        draw.text((date_x, date_y), f"{current_date}", font=medium_font, fill=(21,56,96))
        
        # Save the image to a BytesIO object
        output = BytesIO()
        template.save(output, format='PNG')
        output.seek(0)

        return output
    
