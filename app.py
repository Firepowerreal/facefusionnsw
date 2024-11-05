import subprocess
import os

# Set the device to CPU explicitly
device = "cpu"
print("Using CPU")

# Clone the repository
subprocess.run(["git", "clone", "https://github.com/facefusion/facefusion", "--single-branch"], check=True)

# Change directory to facefusion to run the UI
os.chdir("facefusion")

# Install dependencies for CPU mode
subprocess.run(["python", "install.py", "--onnxruntime", "default", "--skip-conda"], check=True)

# Run the UI in CPU mode
subprocess.run(["python", "facefusion.py", "run", "--execution-providers", "cpu"], check=True)
