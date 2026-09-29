from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def quiz():

    result1 = ""
    result2 = ""

    if request.method == "POST":

        # Question 1
        q = request.form.get("q1", "").lower()

        if q == "delhi":
            result1 = "Correct Answer ✅"
        else:
            result1 = "Wrong Answer ❌"

        # Question 2
        q = request.form.get("q2", "").lower()

        if q == "bang":
            result2 = "Correct Answer ✅"
        else:
            result2 = "Wrong Answer ❌"

    return f"""
<!DOCTYPE html>
<html>

<head>

    <title>Quiz App</title>

    <style>

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: Arial, sans-serif;

            background: linear-gradient(
                135deg,
                #667eea,
                #764ba2
            );

            min-height: 100vh;

            display: flex;
            justify-content: center;
            align-items: center;

            padding: 20px;
        }}

        .quiz-container {{
            width: 600px;
            max-width: 100%;

            background: white;

            padding: 35px;

            border-radius: 20px;

            box-shadow:
                0 15px 40px
                rgba(0, 0, 0, 0.25);
        }}

        h1 {{
            text-align: center;
            color: #333;

            margin-bottom: 8px;
        }}

        .subtitle {{
            text-align: center;
            color: #777;

            margin-bottom: 30px;
        }}

        .question {{
            background: #f5f6ff;

            padding: 20px;

            margin-bottom: 20px;

            border-radius: 12px;

            border-left: 5px solid #667eea;
        }}

        .question h2 {{
            color: #667eea;

            font-size: 18px;

            margin-bottom: 12px;
        }}

        .question p {{
            color: #333;

            font-size: 17px;

            margin-bottom: 15px;
        }}

        input {{
            width: 100%;

            padding: 13px;

            border: 1px solid #ccc;

            border-radius: 8px;

            font-size: 16px;

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

        .result {{
            margin-top: 12px;

            padding: 10px;

            border-radius: 8px;

            background: #e8f5e9;

            color: #2e7d32;

            font-weight: bold;

            text-align: center;
        }}

    </style>

</head>


<body>

    <div class="quiz-container">

        <h1>📝 Quiz App</h1>

        <p class="subtitle">
            Test Your General Knowledge
        </p>


        <form method="POST">


            <!-- Question 1 -->

            <div class="question">

                <h2>Question 1</h2>

                <p>
                    What is the capital of India?
                </p>

                <input
                    type="text"
                    name="q1"
                    placeholder="Enter your answer"
                    required
                >

                {"<div class='result'>" + result1 + "</div>"
                if result1 else ""}

            </div>


            <!-- Question 2 -->

            <div class="question">

                <h2>Question 2</h2>

                <p>
                    What is the capital of Karnataka?
                </p>

                <input
                    type="text"
                    name="q2"
                    placeholder="Enter your answer"
                    required
                >

                {"<div class='result'>" + result2 + "</div>"
                if result2 else ""}

            </div>


            <button type="submit">
                Submit Quiz
            </button>

        </form>

    </div>

</body>

</html>
"""


if __name__ == "__main__":
    app.run(debug=True)