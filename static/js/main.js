// Main JavaScript file for LearnMate

document.addEventListener('DOMContentLoaded', function() {
    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            setTimeout(() => {
                alert.remove();
            }, 300);
        }, 5000);
    });

    // Form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;

            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.style.borderColor = 'red';
                } else {
                    field.style.borderColor = '#ddd';
                }
            });

            if (!isValid) {
                e.preventDefault();
                showNotification('Please fill in all required fields', 'danger');
            }
        });
    });

    // Password strength indicator
    const passwordInput = document.querySelector('input[name="password"]');
    if (passwordInput) {
        passwordInput.addEventListener('input', function() {
            const strength = calculatePasswordStrength(this.value);
            updatePasswordStrengthIndicator(strength);
        });
    }

    // Confirm password validation
    const confirmPasswordInput = document.querySelector('input[name="confirm_password"]');
    if (confirmPasswordInput && passwordInput) {
        confirmPasswordInput.addEventListener('input', function() {
            if (this.value !== passwordInput.value) {
                this.setCustomValidity('Passwords do not match');
                this.style.borderColor = 'red';
            } else {
                this.setCustomValidity('');
                this.style.borderColor = 'green';
            }
        });
    }

    // Search functionality
    const searchInput = document.querySelector('#searchSkills');
    if (searchInput) {
        searchInput.addEventListener('input', debounce(function() {
            filterSkills(this.value);
        }, 300));
    }

    // Category filter
    const categorySelect = document.querySelector('#categoryFilter');
    if (categorySelect) {
        categorySelect.addEventListener('change', function() {
            filterByCategory(this.value);
        });
    }

    // Confirm delete actions
    const deleteButtons = document.querySelectorAll('.btn-delete');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this item?')) {
                e.preventDefault();
            }
        });
    });

    // Initialize tooltips
    initTooltips();

    // Initialize smooth scrolling
    initSmoothScroll();
});

// Password strength calculator
function calculatePasswordStrength(password) {
    let strength = 0;
    
    if (password.length >= 8) strength += 25;
    if (password.length >= 12) strength += 25;
    if (/[a-z]/.test(password)) strength += 10;
    if (/[A-Z]/.test(password)) strength += 10;
    if (/[0-9]/.test(password)) strength += 15;
    if (/[^a-zA-Z0-9]/.test(password)) strength += 15;
    
    return strength;
}

// Update password strength indicator
function updatePasswordStrengthIndicator(strength) {
    const indicator = document.querySelector('#passwordStrength');
    if (!indicator) return;

    let color, text;
    
    if (strength < 30) {
        color = '#dc3545';
        text = 'Weak';
    } else if (strength < 60) {
        color = '#ffc107';
        text = 'Medium';
    } else if (strength < 80) {
        color = '#17a2b8';
        text = 'Strong';
    } else {
        color = '#28a745';
        text = 'Very Strong';
    }
    
    indicator.style.width = strength + '%';
    indicator.style.backgroundColor = color;
    indicator.textContent = text;
}

// Debounce function
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Filter skills by search term
function filterSkills(searchTerm) {
    const skillCards = document.querySelectorAll('.skill-card');
    searchTerm = searchTerm.toLowerCase();

    skillCards.forEach(card => {
        const skillName = card.querySelector('.skill-name').textContent.toLowerCase();
        const description = card.querySelector('.skill-description').textContent.toLowerCase();
        
        if (skillName.includes(searchTerm) || description.includes(searchTerm)) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}

// Filter by category
function filterByCategory(category) {
    const skillCards = document.querySelectorAll('.skill-card');

    skillCards.forEach(card => {
        const cardCategory = card.dataset.category;
        
        if (category === '' || cardCategory === category) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}

// Show notification
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type}`;
    notification.textContent = message;
    
    const container = document.querySelector('.container');
    if (container) {
        container.insertBefore(notification, container.firstChild);
        
        setTimeout(() => {
            notification.style.opacity = '0';
            setTimeout(() => {
                notification.remove();
            }, 300);
        }, 5000);
    }
}

// Initialize tooltips
function initTooltips() {
    const tooltips = document.querySelectorAll('[data-tooltip]');
    
    tooltips.forEach(element => {
        element.addEventListener('mouseenter', function() {
            const tooltipText = this.dataset.tooltip;
            const tooltip = document.createElement('div');
            tooltip.className = 'tooltip';
            tooltip.textContent = tooltipText;
            document.body.appendChild(tooltip);
            
            const rect = this.getBoundingClientRect();
            tooltip.style.top = (rect.top - tooltip.offsetHeight - 5) + 'px';
            tooltip.style.left = (rect.left + (rect.width / 2) - (tooltip.offsetWidth / 2)) + 'px';
        });
        
        element.addEventListener('mouseleave', function() {
            const tooltip = document.querySelector('.tooltip');
            if (tooltip) tooltip.remove();
        });
    });
}

// Smooth scrolling
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// AJAX form submission
function submitFormAjax(formId, successCallback) {
    const form = document.getElementById(formId);
    if (!form) return;

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const formData = new FormData(form);
        const data = Object.fromEntries(formData);
        
        fetch(form.action, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                showNotification(data.message, 'success');
                if (successCallback) successCallback(data);
            } else {
                showNotification(data.message, 'danger');
            }
        })
        .catch(error => {
            showNotification('An error occurred. Please try again.', 'danger');
            console.error('Error:', error);
        });
    });
}

// Real-time skill matching
function findMatches() {
    const userSkills = document.querySelectorAll('.user-skill');
    const availableSkills = document.querySelectorAll('.available-skill');
    const matches = [];

    userSkills.forEach(userSkill => {
        availableSkills.forEach(availableSkill => {
            const similarity = calculateSimilarity(
                userSkill.textContent,
                availableSkill.textContent
            );
            
            if (similarity > 0.7) {
                matches.push({
                    userSkill: userSkill.textContent,
                    matchedSkill: availableSkill.textContent,
                    similarity: similarity
                });
            }
        });
    });

    return matches;
}

// Calculate string similarity
function calculateSimilarity(str1, str2) {
    str1 = str1.toLowerCase();
    str2 = str2.toLowerCase();
    
    if (str1 === str2) return 1;
    if (str1.includes(str2) || str2.includes(str1)) return 0.8;
    
    const words1 = str1.split(' ');
    const words2 = str2.split(' ');
    const commonWords = words1.filter(word => words2.includes(word));
    
    return commonWords.length / Math.max(words1.length, words2.length);
}

// Exchange request animation
function animateExchangeRequest() {
    const exchangeCards = document.querySelectorAll('.exchange-card');
    
    exchangeCards.forEach((card, index) => {
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 100);
    });
}

// Chart initialization (if using charts)
function initCharts() {
    const chartCanvas = document.getElementById('statsChart');
    if (!chartCanvas) return;

    // This would integrate with a charting library like Chart.js
    console.log('Charts initialized');
}

// Export functions for use in other scripts
window.LearnMate = {
    showNotification,
    filterSkills,
    filterByCategory,
    submitFormAjax,
    findMatches
};
