from django.shortcuts import render, redirect

# Shared demo credentials
DEMO_USERS = {
    'student@auca.ac.rw': {'password': 'student123', 'role': 'Student'},
    'staff@auca.ac.rw':   {'password': 'staff123',   'role': 'Staff'},
}

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = DEMO_USERS.get(email)
        if user and user['password'] == password:
            request.session['user_email'] = email
            request.session['user_role'] = user['role']
            return redirect('dashboard')
        return render(request, 'accounts/login.html', {'error': 'Invalid email or password.'})
    return render(request, 'accounts/login.html')

def dashboard_view(request):
    email = request.session.get('user_email')
    if not email:
        return redirect('login')
    return render(request, 'accounts/dashboard.html', {
        'email': email,
        'role': request.session.get('user_role'),
    })

def logout_view(request):
    request.session.flush()
    return redirect('login')