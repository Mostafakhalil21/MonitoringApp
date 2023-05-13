import os
import psutil
from flask import Flask, render_template, jsonify

app = Flask(__name__)



@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent()
    mem_info = psutil.virtual_memory()
    mem_percent = mem_info.percent
    message = None
    if cpu_percent > 80 or mem_percent > 80:
        message = "High CPU or Memory Utilization detected, please Scale Up"
    return render_template("index.html", cpu_metric=cpu_percent, mem_metric=mem_percent, message=message)

@app.route("/api/cpu")
def get_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
    return jsonify(cpu_percent)

@app.route("/api/memory")
def get_memory_usage():
    mem_info = psutil.virtual_memory()
    mem_percent = mem_info.percent
    return jsonify(mem_percent)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
