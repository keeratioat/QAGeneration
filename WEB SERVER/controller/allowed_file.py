ALLOWED_EXTENSIONS_EXAM = set(['java'])
ALLOWED_EXTENSIONS_ADD_USER = set(['csv'])

def allowed_file_exam(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS_EXAM

def allowed_file_add_user(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS_ADD_USER