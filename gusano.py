import shutil
import sys
import os

if len(sys.argv) == 2:
    for num in range(0, int(sys.argv[1])):
        shutil.copy(sys.argv[0], sys.argv[0] + str(num) + ".py")
else:
    print("Usage: python gusano.py <number>")
    sys.exit(1)
