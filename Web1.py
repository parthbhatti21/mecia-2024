from flask import Flask, request, render_template
import appwebAI as a
import threading
import time
import audio

app = Flask(__name__)

# Global flag for stopping the function
stop_flag = False

# Home route for your HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit1', methods=['GET', 'POST'])
def submit_form():
    global stop_flag
    if request.method == 'POST':
        # Process the form submission
        print("Form submitted successfully!")
        stop_flag = False  # Reset the flag
        i = 0
        while i < 5:
            if stop_flag:
                print("Stopping the process...")
                break
            
            if i < 1:
                print(i)
                a.recognize_speech(0)
            else:
                a.recognize_speech(1)

            i += 1
            time.sleep(1)  # Simulate some delay for the process

        if stop_flag:
            print("Function terminated by stop request.")
        return render_template('index.html')

@app.route('/stop', methods=['GET', 'POST'])
def submit_for1():
    global stop_flag
    if request.method == 'POST':
        # Set the flag to stop the function
        stop_flag = True
        print("Stop signal sent.")
        audio.stop()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
