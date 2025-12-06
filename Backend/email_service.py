import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import Config

class EmailService:
    @staticmethod
    def send_email(to_email, subject, body_html):
        """Send HTML email"""
        try:
            # Create message
            msg = MIMEMultipart('alternative')
            msg['From'] = Config.EMAIL_FROM
            msg['To'] = to_email
            msg['Subject'] = subject
            
            # Attach HTML body
            html_part = MIMEText(body_html, 'html')
            msg.attach(html_part)
            
            # Connect to SMTP server
            server = smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT)
            server.starttls()
            server.login(Config.SMTP_USERNAME, Config.SMTP_PASSWORD)
            
            # Send email
            server.send_message(msg)
            server.quit()
            
            print(f"✓ Email sent successfully to {to_email}")
            return True
            
        except Exception as e:
            print(f"✗ Failed to send email: {e}")
            return False
    
    @staticmethod
    def send_contact_confirmation(name, email, phone, message):
        """Send confirmation email to user"""
        from datetime import datetime
        
        subject = "Thank You for Contacting Us - Artmount Academy"
        body = f"""
        <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
            <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
                <h2 style="color: #2c3e50;">Hello {name},</h2>
                
                <p>Thank you for reaching out to <strong>Artmount Academy</strong>!</p>
                
                <p>We have received your inquiry and our team will get back to you shortly.</p>
                
                <div style="background-color: #f8f9fa; padding: 15px; border-left: 4px solid #007bff; margin: 20px 0;">
                    <h3 style="margin-top: 0; color: #007bff;">Your Message Details:</h3>
                    <p><strong>Name:</strong> {name}</p>
                    <p><strong>Email:</strong> {email}</p>
                    <p><strong>Phone:</strong> {phone}</p>
                    <p><strong>Message:</strong><br>{message}</p>
                </div>
                
                <p>If you need immediate assistance, please feel free to contact us at:</p>
                <ul>
                    <li><strong>Phone:</strong> +91 8778359643</li>
                    <li><strong>Email:</strong> info@artmountacademy.com</li>
                    <li><strong>Hours:</strong> Monday - Sunday, 7 AM to 9 PM IST</li>
                </ul>
                
                <p>We look forward to speaking with you soon!</p>
                
                <hr style="border: none; border-top: 1px solid #ddd; margin: 30px 0;">
                
                <p style="font-size: 12px; color: #666;">
                    <strong>Artmount Academy</strong><br>
                    No.4, Alamathi main road, New vellanur, Avadi, Chennai-600062<br>
                    © {datetime.now().year} Artmount Academy. All rights reserved.
                </p>
            </div>
        </body>
        </html>
        """
        
        return EmailService.send_email(email, subject, body)
    
    @staticmethod
    def send_admin_notification(name, email, phone, message):
        """Send notification to admin"""
        from datetime import datetime
        
        subject = f"New Contact Form Submission from {name}"
        body = f"""
        <html>
        <body style="font-family: Arial, sans-serif;">
            <h2>New Contact Form Submission</h2>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Phone:</strong> {phone}</p>
            <p><strong>Message:</strong><br>{message}</p>
            <p><strong>Submitted at:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')}</p>
        </body>
        </html>
        """
        
        return EmailService.send_email(Config.ADMIN_EMAIL, subject, body)
    @staticmethod
    def send_enquiry_confirmation(name, email, phone, course):
      """Send confirmation email for course enquiry"""
      from datetime import datetime
    
      course_names = {
        'uiux': 'UI/UX Design',
        'graphic': 'Graphic Design',
        'video-editing': 'Video Editing',
        'motion': 'Motion Graphics'
    }
    
      course_display = course_names.get(course, course)
      
      subject = f"Welcome to {course_display} - Artmount Academy"
      body = f"""
    <html>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
        <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
            <h2 style="color: #2c3e50;">Hello {name},</h2>
            
            <p>Thank you for your interest in <strong>{course_display}</strong> at <strong>Artmount Academy</strong>!</p>
            
            <p>We're excited to have you join our next batch. Our admission team will contact you within 24 hours to discuss:</p>
            
            <ul>
                <li>Upcoming batch schedules</li>
                <li>Course curriculum and structure</li>
                <li>Fee details and payment options</li>
                <li>Career support and placement assistance</li>
            </ul>
            
            <div style="background-color: #f8f9fa; padding: 15px; border-left: 4px solid #007bff; margin: 20px 0;">
                <h3 style="margin-top: 0; color: #007bff;">Your Enquiry Details:</h3>
                <p><strong>Name:</strong> {name}</p>
                <p><strong>Email:</strong> {email}</p>
                <p><strong>Phone:</strong> {phone}</p>
                <p><strong>Course:</strong> {course_display}</p>
            </div>
            
            <p>If you need immediate assistance, please feel free to contact us at:</p>
            <ul>
                <li><strong>Phone:</strong> +91 8778359643</li>
                <li><strong>Email:</strong> info@artmountacademy.com</li>
                <li><strong>Hours:</strong> Monday - Sunday, 7 AM to 9 PM IST</li>
            </ul>
            
            <p>We look forward to helping you start your creative journey!</p>
            
            <hr style="border: none; border-top: 1px solid #ddd; margin: 30px 0;">
            
            <p style="font-size: 12px; color: #666;">
                <strong>Artmount Academy</strong><br>
                No.4, Alamathi main road, New vellanur, Avadi, Chennai-600062<br>
                © {datetime.now().year} Artmount Academy. All rights reserved.
            </p>
        </div>
    </body>
    </html>
    """
    
      return EmailService.send_email(email, subject, body)

    @staticmethod
    def send_enquiry_notification(name, email, phone, course):
      """Send notification to admin about course enquiry"""
      from datetime import datetime
    
      course_names = {
        'uiux': 'UI/UX Design',
        'graphic': 'Graphic Design',
        'video-editing': 'Video Editing',
        'motion': 'Motion Graphics'
    }
    
      course_display = course_names.get(course, course)
    
      subject = f"New Course Enquiry: {course_display} - {name}"
      body = f"""
    <html>
    <body style="font-family: Arial, sans-serif;">
        <h2>New Course Enquiry Received</h2>
        <p><strong>Course Interested:</strong> {course_display}</p>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>Phone:</strong> {phone}</p>
        <p><strong>Submitted at:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')}</p>
        <hr>
        <p><em>Please follow up with this lead within 24 hours.</em></p>
    </body>
    </html>
    """
    
      return EmailService.send_email(Config.ADMIN_EMAIL, subject, body)