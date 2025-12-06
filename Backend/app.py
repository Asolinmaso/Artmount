

from flask import Flask, request, jsonify
from flask_cors import CORS
from validators import validate_email, sanitize_input, validate_required_fields
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

# Enable CORS for frontend
CORS(app)

# Check if email is configured
EMAIL_CONFIGURED = (
    Config.SMTP_USERNAME != 'your-email@gmail.com' and
    Config.SMTP_PASSWORD != 'your-app-password'
)

@app.route('/')
def home():
    return jsonify({
        "message": "Contact Form API is running",
        "email_configured": EMAIL_CONFIGURED,
        "endpoints": {
            "POST /contact/submit": "Submit contact form"
        }
    })

@app.route('/contact/submit', methods=['POST'])
def submit_contact():
    """Handle contact form submission"""
    try:
        data = request.get_json()
        
        print(f"📨 Received contact form submission:")
        print(f"   Data: {data}")
        
        # Validate required fields
        required = ['name', 'email', 'phone', 'message']
        is_valid, error_msg = validate_required_fields(data, required)
        if not is_valid:
            print(f"❌ Validation failed: {error_msg}")
            return jsonify({"message": error_msg}), 400
        
        # Extract and sanitize data
        name = sanitize_input(data.get('name'))
        email = sanitize_input(data.get('email')).lower()
        phone = sanitize_input(data.get('phone'))
        message = sanitize_input(data.get('message'))
        
        print(f"✓ Sanitized data:")
        print(f"   Name: {name}")
        print(f"   Email: {email}")
        print(f"   Phone: {phone}")
        print(f"   Message: {message}")
        
        # Validate email
        if not validate_email(email):
            print(f"❌ Invalid email format: {email}")
            return jsonify({"message": "Invalid email format"}), 400
        
        print(f"✓ Email validation passed")
        
        # If email is configured, send emails
        if EMAIL_CONFIGURED:
            print(f"📧 Email is configured, attempting to send...")
            try:
                from email_service import EmailService
                
                # Send confirmation email to user
                user_email_sent = EmailService.send_contact_confirmation(name, email, phone, message)
                
                # Send notification to admin
                admin_email_sent = EmailService.send_admin_notification(name, email, phone, message)
                
                if not user_email_sent:
                    print(f"❌ Failed to send confirmation email")
                    return jsonify({"message": "Failed to send confirmation email"}), 500
                
                print(f"✓ Emails sent successfully")
            except Exception as e:
                print(f"❌ Email error: {e}")
                return jsonify({"message": f"Email error: {str(e)}"}), 500
        else:
            print(f"⚠️  Email NOT configured - skipping email send")
            print(f"   To enable emails, update your .env file with valid SMTP credentials")
        
        response_data = {
            "message": "Thank you! We have received your inquiry and will get back to you shortly.",
            "success": True,
            "email_sent": EMAIL_CONFIGURED,
            "data_received": {
                "name": name,
                "email": email,
                "phone": phone
            }
        }
        
        print(f"✓ Sending success response")
        return jsonify(response_data), 200
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({"message": f"Server error: {str(e)}"}), 500
    
@app.route('/enquiry/submit', methods=['POST'])
def submit_enquiry():
    """Handle course enquiry form submission"""
    try:
        data = request.get_json()
        
        print(f"📩 Received enquiry form submission:")
        print(f"   Data: {data}")
        
        # Validate required fields
        required = ['name', 'email', 'phone', 'course']
        is_valid, error_msg = validate_required_fields(data, required)
        if not is_valid:
            print(f"❌ Validation failed: {error_msg}")
            return jsonify({"message": error_msg}), 400
        
        # Extract and sanitize data
        name = sanitize_input(data.get('name'))
        email = sanitize_input(data.get('email')).lower()
        phone = sanitize_input(data.get('phone'))
        course = sanitize_input(data.get('course'))
        
        print(f"✓ Sanitized data:")
        print(f"   Name: {name}")
        print(f"   Email: {email}")
        print(f"   Phone: {phone}")
        print(f"   Course: {course}")
        
        # Validate email
        if not validate_email(email):
            print(f"❌ Invalid email format: {email}")
            return jsonify({"message": "Invalid email format"}), 400
        
        print(f"✓ Email validation passed")
        
        # If email is configured, send emails
        if EMAIL_CONFIGURED:
            print(f"📧 Email is configured, attempting to send...")
            try:
                from email_service import EmailService
                
                # Send confirmation email to user
                user_email_sent = EmailService.send_enquiry_confirmation(name, email, phone, course)
                
                # Send notification to admin
                admin_email_sent = EmailService.send_enquiry_notification(name, email, phone, course)
                
                if not user_email_sent:
                    print(f"❌ Failed to send confirmation email")
                    return jsonify({"message": "Failed to send confirmation email"}), 500
                
                print(f"✓ Emails sent successfully")
            except Exception as e:
                print(f"❌ Email error: {e}")
                return jsonify({"message": f"Email error: {str(e)}"}), 500
        else:
            print(f"⚠️  Email NOT configured - skipping email send")
        
        response_data = {
            "message": "Thank you for your interest! We'll contact you soon with batch details.",
            "success": True,
            "email_sent": EMAIL_CONFIGURED,
            "data_received": {
                "name": name,
                "email": email,
                "phone": phone,
                "course": course
            }
        }
        
        print(f"✓ Sending success response")
        return jsonify(response_data), 200
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({"message": f"Server error: {str(e)}"}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "email_configured": EMAIL_CONFIGURED
    }), 200

if __name__ == '__main__':
    print("🚀 Starting Contact Form Backend...")
    if EMAIL_CONFIGURED:
        print("📧 Email service configured and ready")
    else:
        print("⚠️  Email NOT configured (will accept forms but won't send emails)")
        print("   Update .env file to enable email sending")
    print("🌐 Server running on http://localhost:5001")
    print("")
    app.run(debug=True, port=5001)