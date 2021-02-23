import time
from ProgressBar import ProgressBar

max_value = 50
progress_bar = ProgressBar(max_value)
for i in progress_bar():
    progress_bar.progress(i, "already download {}%".format(int((i + 1) / max_value * 100)))
    time.sleep(0.2)

progress_bar.end()
