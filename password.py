from flask import Flask, request

app = Flask(__name__)

correct_password = "admin123"


@app.route("/", methods=["GET", "POST"])
def login():

    message = ""
    attempts = 0

    if request.method == "POST":

        password = request.form.get("password", "")

        # Get previous attempt count
        attempts = int(request.form.get("attempts", 0))

        # Allow maximum 3 attempts
        if attempts < 3:

            attempts += 1

            if password == correct_password:

                message = "Login Successful ✓"

            else:

                if attempts == 3:
                    message = "Account Locked 🔒"
                else:
                    message = "Wrong Password ✗"

    return f"""
<!DOCTYPE html>
<html>

<head>

    <title>Login System</title>

    <style>

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: Arial, sans-serif;

            min-height: 100vh;

            display: flex;
            justify-content: center;
            align-items: center;

            background: linear-gradient(
                135deg,
                #667eea,
                #764ba2
            );
        }}

        .login-box {{
            width: 400px;
            max-width: 90%;

            background: white;

            padding: 40px;

            border-radius: 20px;

            box-shadow:
                0 15px 40px
                rgba(0, 0, 0, 0.25);

            text-align: center;
        }}

        .icon {{
            font-size: 50px;
            margin-bottom: 15px;
        }}

        h1 {{
            color: #333;
            margin-bottom: 10px;
        }}

        .subtitle {{
            color: #777;
            margin-bottom: 30px;
        }}

        label {{
            display: block;

            text-align: left;

            color: #444;

            font-weight: bold;

            margin-bottom: 8px;
        }}

        input {{
            width: 100%;

            padding: 14px;

            border: 1px solid #ccc;

            border-radius: 8px;

            font-size: 16px;

            margin-bottom: 20px;

            outline: none;
        }}

        input:focus {{
            border-color: #667eea;
        }}

        button {{
            width: 100%;

            padding: 14px;

            border: none;

            border-radius: 8px;

            background: #667eea;

            color: white;

            font-size: 17px;

            font-weight: bold;

            cursor: pointer;
        }}

        button:hover {{
            background: #5568d8;
        }}

        .message {{
            margin-top: 20px;

            padding: 12px;

            border-radius: 8px;

            background: #f1f1f1;

            font-weight: bold;
        }}

        .attempts {{
            margin-top: 15px;

            color: #777;

            font-size: 14px;
        }}

    </style>

</head>


<body>

    <div class="login-box">

        <div class="icon">🔐</div>

        <h1>Secure Login</h1>

        <p class="subtitle">
            Enter your password to continue
        </p>


        <form method="POST">

            <label>
                Password
            </label>

            <input
                type="password"
                name="password"
                placeholder="Enter your password"
                required
            >

            <input
                type="hidden"
                name="attempts"
                value="{attempts}"
            >

            <button type="submit">
                Login
            </button>

        </form>


        {f'''
        <div class="message">
            {message}
        </div>
        ''' if message else ""}


        <div class="attempts">
            Attempts: {attempts} / 3
        </div>

    </div>

</body>

</html>
"""


if __name__ == "__main__":
    app.run(debug=True, port=5001)