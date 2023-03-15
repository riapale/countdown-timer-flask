from flask import Flask, render_template, request
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def timer():
    if request.method == 'POST':
        hours = int(request.form['hours'])
        minutes = int(request.form['minutes'])
        seconds = int(request.form['seconds'])
        total_time = hours * 3600 + minutes * 60 + seconds
        start_time = time.time()
        while True:
            if 'stop' in request.form:
                return "Timer stopped."
            elif 'reset' in request.form:
                return render_template('timer.html')
            else:
                time_elapsed = time.time() - start_time
                time_remaining = max(0, total_time - time_elapsed)
                if time_remaining == 0:
                    return "Timer finished!"
                hours, remainder = divmod(time_remaining, 3600)
                minutes, seconds = divmod(remainder, 60)
                time_str = f'{hours:02}:{minutes:02}:{seconds:02}'
                return render_template('timer.html', time=time_str)
    return render_template('timer.html')

if __name__ == '__main__':
    app.run(debug=True)


