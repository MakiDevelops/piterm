import subprocess
import sys

result = subprocess.run([sys.executable, "-c", "print('This is a subprocess')"])
