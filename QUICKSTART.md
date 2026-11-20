# LearnMate - Quick Start Guide

## Getting Started in 5 Minutes

### Step 1: Install Python
Make sure you have Python 3.8 or higher installed on your system.
- Windows/Mac: Download from https://www.python.org/downloads/
- Linux: Usually pre-installed, or use `sudo apt install python3 python3-pip`

### Step 2: Open Terminal/Command Prompt
Navigate to the learnmate_app folder:
```bash
cd path/to/learnmate_app
```

### Step 3: Quick Start

**Option A - Using the run script (Recommended):**

On Windows:
```bash
run.bat
```

On Mac/Linux:
```bash
chmod +x run.sh
./run.sh
```

**Option B - Manual setup:**
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

### Step 4: Access the Application
Open your web browser and go to:
```
http://127.0.0.1:5000
```

### Step 5: Login

**For Admin Access:**
- Username: `admin`
- Password: `admin123`

**For Regular User:**
- Click "Register" and create a new account

## What Can You Do?

### As a Student User:
1. **Register**: Create your account with college details
2. **Add Skills**: List skills you can teach others
3. **Request Skills**: Add skills you want to learn
4. **Browse**: Search for students offering skills you need
5. **Exchange**: Send exchange requests and start learning!

### As an Admin:
1. **Monitor**: View platform statistics
2. **Manage Users**: View and manage all registered users
3. **Track Exchanges**: Monitor all skill exchanges

## Example Usage Scenario

**Meet Sarah (Computer Science Student):**
1. Sarah registers on LearnMate
2. She adds "Python Programming" as a skill she can teach (Advanced level)
3. She adds "Web Design" as a skill she wants to learn
4. She browses and finds John who teaches Web Design
5. She sends an exchange request offering to teach Python in exchange for learning Web Design
6. John accepts, and they coordinate their learning sessions
7. Both learn new skills without spending any money!

## Common Actions

### Adding a Skill You Can Teach:
1. Go to Dashboard
2. Click "Add Skill"
3. Fill in details:
   - Skill Name (e.g., "JavaScript Programming")
   - Category (e.g., "Programming")
   - Proficiency Level (Beginner/Intermediate/Advanced/Expert)
   - Description (What you can teach)
   - Availability (When you're free to teach)
4. Submit

### Requesting a Skill to Learn:
1. Go to Dashboard
2. Click "Add Request"
3. Fill in what you want to learn
4. System will show you matching users

### Initiating an Exchange:
1. Browse Skills
2. Find someone teaching what you need
3. Click "Request Exchange"
4. Select what skill you'll offer in return
5. Write a friendly message
6. Send request

### Managing Exchange Requests:
1. Go to Dashboard
2. See "Pending Exchanges"
3. Accept or Reject incoming requests
4. Track your ongoing exchanges

## Tips for Success

### For Finding Matches:
- Add multiple skills you can teach - more options = more matches!
- Be specific in descriptions (e.g., "Python for Data Science" vs just "Python")
- Keep your availability updated

### For Getting Accepted:
- Write personalized messages in exchange requests
- Explain why you want to learn the skill
- Be clear about your availability
- Show enthusiasm!

### For Admin Users:
- Regularly check the dashboard for platform health
- Monitor exchange completion rates
- Remove inactive or spam accounts

## Troubleshooting

**Problem: Can't access http://127.0.0.1:5000**
- Solution: Make sure the application is running in your terminal
- Check if another application is using port 5000

**Problem: "Module not found" error**
- Solution: Install dependencies using `pip install -r requirements.txt`

**Problem: Forgot admin password**
- Solution: Delete the `instance/learnmate.db` file and restart the app (this resets everything)

**Problem: Page not loading properly**
- Solution: Clear your browser cache and refresh
- Try a different browser

## Next Steps

### Explore Features:
- Update your profile with complete details
- Add at least 3 skills you can teach
- Browse and connect with other students
- Complete your first exchange!

### Spread the Word:
- Invite your classmates to join
- Create a study group on LearnMate
- Share success stories

## Need Help?

- Check the README.md for detailed documentation
- Review the code comments in app.py
- Contact your system administrator

---

Happy Learning! 🎓

**Created by**: Swetha R | BSc IT
**Guide**: Dr S Vijaya
