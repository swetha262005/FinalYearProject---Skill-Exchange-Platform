"""
Sample Data Initializer for LearnMate
This script populates the database with sample users, skills, and exchanges for demonstration
"""

from app import app, db, User, Skill, SkillRequest, Exchange
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta
import random

def init_sample_data():
    """Initialize database with sample data"""
    
    with app.app_context():
        # Clear existing data (optional - uncomment if you want fresh data)
        # db.drop_all()
        # db.create_all()
        
        print("Adding sample users...")
        
        # Sample users
        users_data = [
            {
                'username': 'john_doe',
                'email': 'john@example.com',
                'password': 'password123',
                'full_name': 'John Doe',
                'college': 'ABC College',
                'department': 'Computer Science',
                'year': '3rd Year'
            },
            {
                'username': 'sarah_smith',
                'email': 'sarah@example.com',
                'password': 'password123',
                'full_name': 'Sarah Smith',
                'college': 'ABC College',
                'department': 'Information Technology',
                'year': '2nd Year'
            },
            {
                'username': 'mike_wilson',
                'email': 'mike@example.com',
                'password': 'password123',
                'full_name': 'Mike Wilson',
                'college': 'XYZ University',
                'department': 'Software Engineering',
                'year': '4th Year'
            },
            {
                'username': 'emma_brown',
                'email': 'emma@example.com',
                'password': 'password123',
                'full_name': 'Emma Brown',
                'college': 'ABC College',
                'department': 'Computer Applications',
                'year': '1st Year'
            },
            {
                'username': 'david_lee',
                'email': 'david@example.com',
                'password': 'password123',
                'full_name': 'David Lee',
                'college': 'Tech Institute',
                'department': 'Data Science',
                'year': '3rd Year'
            }
        ]
        
        users = []
        for user_data in users_data:
            # Check if user already exists
            existing_user = User.query.filter_by(username=user_data['username']).first()
            if not existing_user:
                user = User(
                    username=user_data['username'],
                    email=user_data['email'],
                    password=generate_password_hash(user_data['password'], method='pbkdf2:sha256'),
                    full_name=user_data['full_name'],
                    college=user_data['college'],
                    department=user_data['department'],
                    year=user_data['year']
                )
                db.session.add(user)
                users.append(user)
            else:
                users.append(existing_user)
        
        db.session.commit()
        print(f"Added {len(users)} users")
        
        print("Adding sample skills...")
        
        # Sample skills
        skills_data = [
            # John's skills
            {'user': users[0], 'skill_name': 'Python Programming', 'category': 'Programming', 
             'proficiency_level': 'Advanced', 'description': 'Can teach Python fundamentals, data structures, and web development with Flask/Django',
             'availability': 'Weekday evenings'},
            {'user': users[0], 'skill_name': 'Machine Learning Basics', 'category': 'Programming', 
             'proficiency_level': 'Intermediate', 'description': 'Familiar with scikit-learn, basic ML algorithms',
             'availability': 'Weekends'},
            
            # Sarah's skills
            {'user': users[1], 'skill_name': 'Web Design', 'category': 'Design', 
             'proficiency_level': 'Advanced', 'description': 'HTML, CSS, responsive design, UI/UX principles',
             'availability': 'Flexible - most days after 4 PM'},
            {'user': users[1], 'skill_name': 'Graphic Design', 'category': 'Design', 
             'proficiency_level': 'Intermediate', 'description': 'Adobe Photoshop, Illustrator, Canva',
             'availability': 'Weekends'},
            
            # Mike's skills
            {'user': users[2], 'skill_name': 'Java Programming', 'category': 'Programming', 
             'proficiency_level': 'Expert', 'description': 'Core Java, Spring Boot, Android development',
             'availability': 'Mon, Wed, Fri evenings'},
            {'user': users[2], 'skill_name': 'Database Design', 'category': 'Programming', 
             'proficiency_level': 'Advanced', 'description': 'MySQL, PostgreSQL, database normalization, SQL queries',
             'availability': 'Flexible'},
            
            # Emma's skills
            {'user': users[3], 'skill_name': 'Spanish Language', 'category': 'Languages', 
             'proficiency_level': 'Intermediate', 'description': 'Conversational Spanish, grammar basics',
             'availability': 'Tuesday and Thursday afternoons'},
            {'user': users[3], 'skill_name': 'Guitar Basics', 'category': 'Music', 
             'proficiency_level': 'Beginner', 'description': 'Basic chords, simple songs',
             'availability': 'Weekends'},
            
            # David's skills
            {'user': users[4], 'skill_name': 'Data Analysis', 'category': 'Programming', 
             'proficiency_level': 'Advanced', 'description': 'Python pandas, numpy, data visualization, Excel',
             'availability': 'Most evenings'},
            {'user': users[4], 'skill_name': 'Statistics', 'category': 'Mathematics', 
             'proficiency_level': 'Advanced', 'description': 'Probability, hypothesis testing, statistical analysis',
             'availability': 'Weekdays after 6 PM'}
        ]
        
        for skill_data in skills_data:
            skill = Skill(
                user_id=skill_data['user'].id,
                skill_name=skill_data['skill_name'],
                category=skill_data['category'],
                proficiency_level=skill_data['proficiency_level'],
                description=skill_data['description'],
                availability=skill_data['availability']
            )
            db.session.add(skill)
        
        db.session.commit()
        print(f"Added {len(skills_data)} skills")
        
        print("Adding skill requests...")
        
        # Sample skill requests
        requests_data = [
            {'user': users[0], 'skill_name': 'Web Design', 'category': 'Design',
             'description': 'Want to build better looking websites for my projects', 'urgency': 'Medium'},
            {'user': users[1], 'skill_name': 'JavaScript', 'category': 'Programming',
             'description': 'Need to learn JS for interactive web development', 'urgency': 'High'},
            {'user': users[2], 'skill_name': 'Python Programming', 'category': 'Programming',
             'description': 'Want to learn Python for data science', 'urgency': 'Medium'},
            {'user': users[3], 'skill_name': 'Photography', 'category': 'Arts',
             'description': 'Interested in learning basic photography skills', 'urgency': 'Low'},
            {'user': users[4], 'skill_name': 'Public Speaking', 'category': 'Other',
             'description': 'Need to improve presentation skills for conferences', 'urgency': 'Urgent'}
        ]
        
        for request_data in requests_data:
            skill_request = SkillRequest(
                user_id=request_data['user'].id,
                skill_name=request_data['skill_name'],
                category=request_data['category'],
                description=request_data['description'],
                urgency=request_data['urgency']
            )
            db.session.add(skill_request)
        
        db.session.commit()
        print(f"Added {len(requests_data)} skill requests")
        
        print("Adding sample exchanges...")
        
        # Sample exchanges
        exchanges_data = [
            {
                'initiator': users[0], 'receiver': users[1],
                'initiator_skill': 'Python Programming', 'receiver_skill': 'Web Design',
                'status': 'accepted',
                'message': 'Hi Sarah! I saw you teach web design. I can help you with Python in exchange!'
            },
            {
                'initiator': users[1], 'receiver': users[2],
                'initiator_skill': 'Graphic Design', 'receiver_skill': 'Java Programming',
                'status': 'pending',
                'message': 'Would love to learn Java from you. I can teach graphic design!'
            },
            {
                'initiator': users[3], 'receiver': users[0],
                'initiator_skill': 'Spanish', 'receiver_skill': 'Python Programming',
                'status': 'rejected',
                'message': 'Interested in learning Python!'
            },
            {
                'initiator': users[4], 'receiver': users[1],
                'initiator_skill': 'Data Analysis', 'receiver_skill': 'Web Design',
                'status': 'completed',
                'message': 'Your web design portfolio looks great! Want to exchange skills?'
            }
        ]
        
        for exchange_data in exchanges_data:
            exchange = Exchange(
                initiator_id=exchange_data['initiator'].id,
                receiver_id=exchange_data['receiver'].id,
                initiator_skill=exchange_data['initiator_skill'],
                receiver_skill=exchange_data['receiver_skill'],
                status=exchange_data['status'],
                message=exchange_data['message']
            )
            db.session.add(exchange)
        
        db.session.commit()
        print(f"Added {len(exchanges_data)} exchanges")
        
        print("\n" + "="*50)
        print("Sample data initialization complete!")
        print("="*50)
        print("\nSample User Credentials (all have password: 'password123'):")
        for user in users:
            print(f"  - {user.username}")
        print("\nAdmin Credentials:")
        print("  - admin / admin123")
        print("="*50)

if __name__ == '__main__':
    init_sample_data()
