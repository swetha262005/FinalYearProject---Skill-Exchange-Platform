# LearnMate - Skill Exchange Platform

#Run command
py -m venv venv
./venv/Scripts/activate
py app.py

## Project Information
- **Name**: Swetha R
- **Class**: BSc IT
- **Roll No**: 2326JB52
- **Guide**: Dr S Vijaya

## About
LearnMate is a web-based skill exchange platform designed specifically for students. It allows students to exchange skills with one another without any monetary transactions, promoting collaborative learning and knowledge sharing within academic communities.

## Features

### User Features
- **User Registration & Authentication**: Secure registration and login system
- **Profile Management**: Create and manage personal profiles with academic details
- **Skill Listing**: Add skills you can teach with proficiency levels
- **Skill Requests**: Post skills you want to learn
- **Smart Matching**: Find users who want to learn what you teach
- **Exchange System**: Send and receive skill exchange requests
- **Browse & Search**: Search and filter skills by category
- **Dashboard**: Personalized dashboard showing your activities

### Admin Features
- **Admin Dashboard**: Overview of platform statistics
- **User Management**: View and manage all registered users
- **Exchange Monitoring**: Track all skill exchanges on the platform
- **User Deletion**: Remove users if necessary

## Technology Stack

### Frontend
- HTML5
- CSS3 (Custom styling with responsive design)
- JavaScript (Vanilla JS for interactivity)
- Font Awesome Icons

### Backend
- Python 3.x
- Flask (Web Framework)
- Flask-SQLAlchemy (ORM)
- Werkzeug (Password hashing)

### Database
- SQLite (Development)
- Can be easily switched to MySQL/PostgreSQL for production

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone or Download the Project
```bash
# Navigate to the project directory
cd learnmate_app
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python app.py
```

The application will start on `http://127.0.0.1:5000/`

## Default Credentials

### Admin Account
- **Username**: admin
- **Password**: admin123

**Note**: Please change the admin password after first login in a production environment.

## Database Schema

### User Table
- id (Primary Key)
- username (Unique)
- email (Unique)
- password (Hashed)
- full_name
- college
- department
- year
- is_admin (Boolean)
- created_at

### Skill Table
- id (Primary Key)
- user_id (Foreign Key)
- skill_name
- category
- proficiency_level
- description
- availability
- created_at

### SkillRequest Table
- id (Primary Key)
- user_id (Foreign Key)
- skill_name
- category
- description
- urgency
- created_at

### Exchange Table
- id (Primary Key)
- initiator_id (Foreign Key)
- receiver_id (Foreign Key)
- initiator_skill
- receiver_skill
- status (pending/accepted/rejected/completed)
- message
- created_at
- updated_at

## Key Functionalities

### 1. User Registration
- Secure password hashing using Werkzeug
- Validation for username and email uniqueness
- Academic information collection (college, department, year)

### 2. Skill Management
- Add multiple skills with proficiency levels (Beginner, Intermediate, Advanced, Expert)
- Categorize skills (Programming, Design, Languages, etc.)
- Specify availability for teaching

### 3. Skill Exchange System
- Browse available skills from other users
- Filter by category and search by keyword
- Send exchange requests with personalized messages
- Accept/reject incoming requests
- Mark exchanges as completed

### 4. Smart Matching
- Automatic matching of users based on complementary skills
- Shows potential exchange partners on dashboard

### 5. Admin Panel
- Real-time statistics dashboard
- User management capabilities
- Exchange monitoring and analytics

## Project Structure
```
learnmate_app/
│
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
│
├── static/
│   ├── css/
│   │   └── style.css          # Custom CSS styles
│   ├── js/
│   │   └── main.js            # JavaScript functionality
│   └── images/                 # Static images
│
├── templates/
│   ├── base.html              # Base template
│   ├── index.html             # Home page
│   ├── login.html             # Login page
│   ├── register.html          # Registration page
│   ├── dashboard.html         # User dashboard
│   ├── profile.html           # User profile
│   ├── edit_profile.html      # Edit profile
│   ├── add_skill.html         # Add skill form
│   ├── add_request.html       # Add request form
│   ├── browse_skills.html     # Browse skills
│   ├── initiate_exchange.html # Exchange request form
│   └── admin/
│       ├── dashboard.html     # Admin dashboard
│       ├── users.html         # User management
│       └── exchanges.html     # Exchange management
│
└── instance/
    └── learnmate.db           # SQLite database (created automatically)
```

## Security Features
- Password hashing using PBKDF2-SHA256
- Session-based authentication
- CSRF protection
- Login required decorators
- Admin-only access control

## Deployment Considerations

### For Production:
1. Change the SECRET_KEY in app.py
2. Use PostgreSQL or MySQL instead of SQLite
3. Enable HTTPS
4. Set DEBUG=False
5. Use environment variables for sensitive data
6. Implement rate limiting
7. Add email verification
8. Set up proper logging

## Future Enhancements
- Real-time chat between users
- Rating and review system
- Skill verification/badges
- Email notifications
- Mobile app version
- Video call integration
- Advanced analytics
- Recommendation system using ML

## Troubleshooting

### Database Issues
If you encounter database errors, delete the `instance/learnmate.db` file and restart the application. It will create a fresh database.

### Port Already in Use
If port 5000 is already in use, you can change it in app.py:
```python
app.run(debug=True, port=5001)
```

### Module Not Found Errors
Make sure you've activated your virtual environment and installed all requirements:
```bash
pip install -r requirements.txt
```

## Support
For issues or questions, please contact the development team.

## License
This project is created for educational purposes as part of BSc IT curriculum.

---
Developed by Swetha R | Guide: Dr S Vijaya
