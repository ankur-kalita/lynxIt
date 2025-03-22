# Secure Login & Fuzzy Search Dictionary

## Objective

Build a simple web application where users must log in to access a fuzzy search dictionary. If the user is not authenticated, they should be redirected to the login page. The dictionary search should return the closest matching word(s) and their meanings, even if the input contains typos.

## Features

### Login System

- Login page with username and password field
- Main page accessible only after login
- Logout button that clears authentication and redirects to login
- Session-based authentication system
- Authentication verification before allowing access

### Fuzzy Search Dictionary

- Search bar for entering words
- Submit button to trigger search
- Loading indicator during processing
- Result area displaying:
  - Exact match with meaning when found
  - Suggested words when no exact match is found
- Preloaded dictionary of words and meanings
- Fuzzy matching implementation for suggestions

## Bonus Features

- Real-time search suggestions while typing
- Past searches stored in localStorage for quick access
- Password hashing for better security

## Installation and Usage

1. Clone the repository
2. Install required dependencies:
   ```
   pip install flask # or install the dependencies from requirements.txt
   ```
3. Run the application:
   ```
   python app.py
   ```
4. Access the application at http://127.0.0.1:5000/
5. Login with the credentials:
   - Username: admin
   - Password: password123

## Project Structure

```
secure_login_dictionary/
├── app.py
├── static/
│   └── style.css
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── dictionary.html
│
└── dictionary.json
```

## Evaluation Criteria

- Authentication Handling: Login/logout functionality
- Session & Redirection: Protection against unauthorized access
- Fuzzy Search Accuracy: Useful suggestions for typos
- Code Cleanliness: Modular and understandable implementation

## Notes

This project was completed as part of the Lynxit Internship Program (March 2025).
