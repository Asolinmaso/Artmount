import re

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    """Validate phone number (10 digits)"""
    pattern = r'^[0-9]{10}$'
    return re.match(pattern, phone.replace(' ', '').replace('-', '')) is not None

def sanitize_input(text):
    """Remove dangerous characters"""
    if not text:
        return ""
    return text.strip()

def validate_required_fields(data, required_fields):
    """Check if all required fields are present"""
    missing = []
    for field in required_fields:
        if field not in data or not data[field] or not str(data[field]).strip():
            missing.append(field)
    
    if missing:
        return False, f"Missing required fields: {', '.join(missing)}"
    return True, None