# LearnMate - Complete Installation & Deployment Guide

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation Methods](#installation-methods)
3. [Running the Application](#running-the-application)
4. [Adding Sample Data](#adding-sample-data)
5. [Testing the Application](#testing-the-application)
6. [Deployment Options](#deployment-options)
7. [MySQL Setup (Optional)](#mysql-setup)
8. [Troubleshooting](#troubleshooting)

---

## Prerequisites

### Required Software
- **Python**: Version 3.8 or higher
- **pip**: Python package manager (usually comes with Python)
- **Web Browser**: Chrome, Firefox, Safari, or Edge

### Optional (for production)
- **MySQL** or **PostgreSQL**: For production database
- **Git**: For version control
- **Virtual Environment**: Recommended for isolation

---

## Installation Methods

### Method 1: Quick Start (Recommended for Beginners)

#### On Windows:
1. Extract the `learnmate_app` folder
2. Double-click `run.bat`
3. Wait for installation to complete
4. Open browser and go to http://127.0.0.1:5000

#### On Mac/Linux:
1. Extract the `learnmate_app` folder
2. Open Terminal and navigate to the folder:
   ```bash
   cd path/to/learnmate_app
   ```
3. Run:
   ```bash
   chmod +x run.sh
   ./run.sh
   ```
4. Open browser and go to http://127.0.0.1:5000

### Method 2: Manual Installation

#### Step 1: Open Terminal/Command Prompt
Navigate to the project folder:
```bash
cd path/to/learnmate_app
```

#### Step 2: Create Virtual Environment (Recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

#### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

#### Step 4: Run the Application
```bash
python app.py
```

---

## Running the Application

### Starting the Server
After installation, the application will be available at:
```
http://127.0.0.1:5000
```

### Default Admin Credentials
- **Username**: admin
- **Password**: admin123

⚠️ **Important**: Change admin password after first login!

### Stopping the Server
- Press `Ctrl+C` in the terminal/command prompt

---

## Adding Sample Data

For demonstration and testing purposes, you can add sample users and data:

```bash
python init_sample_data.py
```

This will create:
- 5 sample users (john_doe, sarah_smith, mike_wilson, emma_brown, david_lee)
- 10 sample skills
- 5 skill requests
- 4 sample exchanges

All sample users have password: `password123`

---

## Testing the Application

### User Flow Test

#### 1. Register a New User
- Go to http://127.0.0.1:5000
- Click "Register"
- Fill in the form with your details
- Submit

#### 2. Add Your Skills
- Login with your new account
- Click "Add Skill" on dashboard
- Add 2-3 skills you can teach
- Include proficiency level and availability

#### 3. Add Skill Requests
- Click "Add Request"
- Add skills you want to learn
- Set urgency level

#### 4. Browse and Exchange
- Click "Browse Skills"
- Find a skill you want to learn
- Click "Request Exchange"
- Select your skill to offer
- Write a message
- Send request

#### 5. Manage Exchanges
- Go to Dashboard
- Check "Pending Exchanges"
- Accept/Reject requests
- Mark completed exchanges

### Admin Flow Test

#### 1. Login as Admin
- Username: admin
- Password: admin123

#### 2. View Dashboard
- See total statistics
- Recent users
- Recent exchanges

#### 3. Manage Users
- Click "Admin" → "Manage Users"
- View all registered users
- Delete test users if needed

#### 4. Monitor Exchanges
- Click "Admin" → "View Exchanges"
- See all platform exchanges
- Check exchange status distribution

---

## Deployment Options

### Option 1: Local Network Deployment

To make the app accessible on your local network:

1. Find your local IP address:
   ```bash
   # Windows
   ipconfig
   
   # Mac/Linux
   ifconfig
   ```

2. Modify `app.py` (last line):
   ```python
   app.run(host='0.0.0.0', debug=True)
   ```

3. Access from other devices:
   ```
   http://YOUR_LOCAL_IP:5000
   ```

### Option 2: Cloud Deployment (Heroku)

#### Prerequisites:
- Heroku account
- Heroku CLI installed

#### Steps:

1. Create `Procfile`:
   ```
   web: python app.py
   ```

2. Create `runtime.txt`:
   ```
   python-3.11.0
   ```

3. Modify `app.py` for Heroku:
   ```python
   import os
   port = int(os.environ.get('PORT', 5000))
   app.run(host='0.0.0.0', port=port)
   ```

4. Deploy:
   ```bash
   heroku login
   heroku create your-app-name
   git init
   git add .
   git commit -m "Initial commit"
   git push heroku master
   ```

### Option 3: PythonAnywhere Deployment

1. Sign up at pythonanywhere.com
2. Upload project files
3. Configure WSGI file
4. Install dependencies
5. Reload web app

---

## MySQL Setup (Optional)

For production, use MySQL instead of SQLite:

### Step 1: Install MySQL
```bash
# Windows: Download from mysql.com
# Mac: brew install mysql
# Linux: sudo apt install mysql-server
```

### Step 2: Install Python MySQL Driver
```bash
pip install pymysql
```

### Step 3: Create Database
```sql
CREATE DATABASE learnmate;
CREATE USER 'learnmate_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON learnmate.* TO 'learnmate_user'@'localhost';
FLUSH PRIVILEGES;
```

### Step 4: Update app.py
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://learnmate_user:your_password@localhost/learnmate'
```

---

## Troubleshooting

### Common Issues and Solutions

#### 1. Port 5000 Already in Use
**Error**: `Address already in use`

**Solution**: Change port in `app.py`:
```python
app.run(debug=True, port=5001)
```

#### 2. Module Not Found Error
**Error**: `ModuleNotFoundError: No module named 'flask'`

**Solution**: 
```bash
pip install -r requirements.txt
```

#### 3. Database Locked Error
**Error**: `database is locked`

**Solution**: 
- Close any other instances of the app
- Delete `instance/learnmate.db`
- Restart the application

#### 4. Template Not Found
**Error**: `TemplateNotFound`

**Solution**: 
- Check folder structure
- Ensure templates are in `templates/` folder

#### 5. Static Files Not Loading
**Solution**:
- Clear browser cache (Ctrl+Shift+Delete)
- Refresh page (Ctrl+F5)
- Check static files are in `static/` folder

#### 6. Cannot Connect to Database
**Solution**:
- Check database connection string
- Verify MySQL/PostgreSQL is running
- Check credentials

#### 7. Permission Denied (Linux/Mac)
**Solution**:
```bash
chmod +x run.sh
sudo chown -R $USER:$USER learnmate_app
```

---

## Security Checklist for Production

Before deploying to production:

- [ ] Change SECRET_KEY in app.py
- [ ] Set DEBUG=False
- [ ] Change admin password
- [ ] Use strong passwords
- [ ] Enable HTTPS
- [ ] Use environment variables for sensitive data
- [ ] Set up proper logging
- [ ] Configure firewall
- [ ] Regular backups
- [ ] Update dependencies regularly

---

## Performance Optimization

### For Better Performance:

1. **Use PostgreSQL/MySQL** instead of SQLite
2. **Enable caching** with Flask-Caching
3. **Use CDN** for static files
4. **Optimize database queries**
5. **Add indexes** to database tables
6. **Use Gunicorn** or **uWSGI** as WSGI server
7. **Set up Nginx** as reverse proxy

---

## Maintenance

### Regular Tasks:

1. **Weekly**: Check logs for errors
2. **Monthly**: Update dependencies
3. **Quarterly**: Database backup
4. **Yearly**: Security audit

### Backup Database:
```bash
# SQLite
cp instance/learnmate.db instance/learnmate_backup.db

# MySQL
mysqldump -u learnmate_user -p learnmate > backup.sql
```

---

## Getting Help

### Resources:
- Check README.md for detailed documentation
- Review QUICKSTART.md for basic usage
- Examine code comments in app.py
- Flask documentation: https://flask.palletsprojects.com/

### Contact:
For issues or questions related to this project, contact:
- **Developer**: Swetha R
- **Class**: BSc IT
- **Guide**: Dr S Vijaya

---

## License and Credits

This project is created for educational purposes as part of BSc IT curriculum.

**Technologies Used**:
- Flask (Web Framework)
- SQLAlchemy (ORM)
- SQLite/MySQL (Database)
- HTML/CSS/JavaScript (Frontend)
- Font Awesome (Icons)

---

## Conclusion

You now have a complete skill exchange platform! Follow the steps above to get started, and don't hesitate to customize it for your needs.

Happy Learning! 🎓
