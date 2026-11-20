from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from functools import wraps
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///learnmate.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    college = db.Column(db.String(100))
    department = db.Column(db.String(100))
    year = db.Column(db.String(20))
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    skills_offered = db.relationship('Skill', backref='user', lazy=True, foreign_keys='Skill.user_id')
    skills_wanted = db.relationship('SkillRequest', backref='user', lazy=True)
    exchanges_initiated = db.relationship('Exchange', foreign_keys='Exchange.initiator_id', backref='initiator', lazy=True)
    exchanges_received = db.relationship('Exchange', foreign_keys='Exchange.receiver_id', backref='receiver', lazy=True)

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    skill_name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    proficiency_level = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    availability = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class SkillRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    skill_name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    urgency = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Exchange(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    initiator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    initiator_skill = db.Column(db.String(100), nullable=False)
    receiver_skill = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default='pending')  # pending, accepted, rejected, completed
    message = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Decorators
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please login to access this page.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please login to access this page.', 'warning')
            return redirect(url_for('login'))
        user = User.query.get(session['user_id'])
        if not user or not user.is_admin:
            flash('Access denied. Admin privileges required.', 'danger')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        full_name = request.form.get('full_name')
        college = request.form.get('college')
        department = request.form.get('department')
        year = request.form.get('year')
        
        # Validation
        if not all([username, email, password, confirm_password, full_name]):
            flash('Please fill in all required fields.', 'danger')
            return redirect(url_for('register'))
        
        if password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return redirect(url_for('register'))
        
        if len(password) < 6:
            flash('Password must be at least 6 characters long.', 'danger')
            return redirect(url_for('register'))
        
        # Check if user exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists.', 'danger')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered.', 'danger')
            return redirect(url_for('register'))
        
        # Create new user
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(
            username=username,
            email=email,
            password=hashed_password,
            full_name=full_name,
            college=college,
            department=department,
            year=year
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            session['is_admin'] = user.is_admin
            
            flash(f'Welcome back, {user.full_name}!', 'success')
            
            if user.is_admin:
                return redirect(url_for('admin_dashboard'))
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    user = User.query.get(session['user_id'])
    my_skills = Skill.query.filter_by(user_id=user.id).all()
    my_requests = SkillRequest.query.filter_by(user_id=user.id).all()
    
    # Get pending exchanges
    pending_exchanges = Exchange.query.filter(
        ((Exchange.initiator_id == user.id) | (Exchange.receiver_id == user.id)) &
        (Exchange.status == 'pending')
    ).all()
    
    # Get matches
    matches = []
    for request in my_requests:
        matching_skills = Skill.query.filter(
            Skill.skill_name.ilike(f'%{request.skill_name}%'),
            Skill.user_id != user.id
        ).all()
        for skill in matching_skills:
            matches.append({
                'skill': skill,
                'request': request,
                'user': User.query.get(skill.user_id)
            })
    
    return render_template('dashboard.html', user=user, my_skills=my_skills, 
                         my_requests=my_requests, pending_exchanges=pending_exchanges,
                         matches=matches)

@app.route('/add_skill', methods=['GET', 'POST'])
@login_required
def add_skill():
    if request.method == 'POST':
        skill_name = request.form.get('skill_name')
        category = request.form.get('category')
        proficiency_level = request.form.get('proficiency_level')
        description = request.form.get('description')
        availability = request.form.get('availability')
        
        new_skill = Skill(
            user_id=session['user_id'],
            skill_name=skill_name,
            category=category,
            proficiency_level=proficiency_level,
            description=description,
            availability=availability
        )
        
        db.session.add(new_skill)
        db.session.commit()
        
        flash('Skill added successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('add_skill.html')

@app.route('/add_request', methods=['GET', 'POST'])
@login_required
def add_request():
    if request.method == 'POST':
        skill_name = request.form.get('skill_name')
        category = request.form.get('category')
        description = request.form.get('description')
        urgency = request.form.get('urgency')
        
        new_request = SkillRequest(
            user_id=session['user_id'],
            skill_name=skill_name,
            category=category,
            description=description,
            urgency=urgency
        )
        
        db.session.add(new_request)
        db.session.commit()
        
        flash('Skill request added successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('add_request.html')

@app.route('/browse_skills')
@login_required
def browse_skills():
    category = request.args.get('category', '')
    search = request.args.get('search', '')
    
    query = Skill.query.filter(Skill.user_id != session['user_id'])
    
    if category:
        query = query.filter_by(category=category)
    
    if search:
        query = query.filter(Skill.skill_name.ilike(f'%{search}%'))
    
    skills = query.all()
    categories = db.session.query(Skill.category).distinct().all()
    
    return render_template('browse_skills.html', skills=skills, categories=categories)

@app.route('/initiate_exchange/<int:skill_id>', methods=['GET', 'POST'])
@login_required
def initiate_exchange(skill_id):
    skill = Skill.query.get_or_404(skill_id)
    
    if skill.user_id == session['user_id']:
        flash('You cannot exchange with yourself.', 'warning')
        return redirect(url_for('browse_skills'))
    
    if request.method == 'POST':
        my_skill = request.form.get('my_skill')
        message = request.form.get('message')
        
        exchange = Exchange(
            initiator_id=session['user_id'],
            receiver_id=skill.user_id,
            initiator_skill=my_skill,
            receiver_skill=skill.skill_name,
            message=message
        )
        
        db.session.add(exchange)
        db.session.commit()
        
        flash('Exchange request sent!', 'success')
        return redirect(url_for('dashboard'))
    
    my_skills = Skill.query.filter_by(user_id=session['user_id']).all()
    return render_template('initiate_exchange.html', skill=skill, my_skills=my_skills)

@app.route('/manage_exchange/<int:exchange_id>/<action>')
@login_required
def manage_exchange(exchange_id, action):
    exchange = Exchange.query.get_or_404(exchange_id)
    
    if exchange.receiver_id != session['user_id']:
        flash('Unauthorized action.', 'danger')
        return redirect(url_for('dashboard'))
    
    if action == 'accept':
        exchange.status = 'accepted'
        flash('Exchange request accepted!', 'success')
    elif action == 'reject':
        exchange.status = 'rejected'
        flash('Exchange request rejected.', 'info')
    elif action == 'complete':
        exchange.status = 'completed'
        flash('Exchange marked as completed!', 'success')
    
    db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/profile')
@login_required
def profile():
    user = User.query.get(session['user_id'])
    return render_template('profile.html', user=user)

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    user = User.query.get(session['user_id'])
    
    if request.method == 'POST':
        user.full_name = request.form.get('full_name')
        user.email = request.form.get('email')
        user.college = request.form.get('college')
        user.department = request.form.get('department')
        user.year = request.form.get('year')
        
        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('profile'))
    
    return render_template('edit_profile.html', user=user)

# Admin Routes
@app.route('/admin/dashboard')
@admin_required
def admin_dashboard():
    total_users = User.query.count()
    total_skills = Skill.query.count()
    total_requests = SkillRequest.query.count()
    total_exchanges = Exchange.query.count()
    
    recent_users = User.query.order_by(User.created_at.desc()).limit(5).all()
    recent_exchanges = Exchange.query.order_by(Exchange.created_at.desc()).limit(5).all()
    
    return render_template('admin/dashboard.html', 
                         total_users=total_users,
                         total_skills=total_skills,
                         total_requests=total_requests,
                         total_exchanges=total_exchanges,
                         recent_users=recent_users,
                         recent_exchanges=recent_exchanges)

@app.route('/admin/users')
@admin_required
def admin_users():
    users = User.query.all()
    return render_template('admin/users.html', users=users)

@app.route('/admin/delete_user/<int:user_id>')
@admin_required
def admin_delete_user(user_id):
    user = User.query.get_or_404(user_id)
    
    if user.is_admin:
        flash('Cannot delete admin users.', 'danger')
        return redirect(url_for('admin_users'))
    
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully.', 'success')
    return redirect(url_for('admin_users'))

@app.route('/admin/exchanges')
@admin_required
def admin_exchanges():
    exchanges = Exchange.query.all()
    return render_template('admin/exchanges.html', exchanges=exchanges)

# Initialize database
def init_db():
    with app.app_context():
        db.create_all()
        
        # Create default admin if doesn't exist
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            admin = User(
                username='admin',
                email='admin@learnmate.com',
                password=generate_password_hash('admin123', method='pbkdf2:sha256'),
                full_name='Administrator',
                is_admin=True
            )
            db.session.add(admin)
            db.session.commit()
            print("Default admin created (username: admin, password: admin123)")

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
