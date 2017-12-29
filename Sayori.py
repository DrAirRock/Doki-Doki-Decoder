from matplotlib import pylab
from pylab import *
import wave
import os
import subprocess

filename = os.path.join('Char_files', 'sayori.chr')
command = ["ffmpeg", "-hide_banner", "-loglevel", "panic", "-i", filename, "-f", "wav", "-"]
converter = subprocess.Popen(command, stdout=subprocess.PIPE)
sig = wave.open(converter.stdout, 'r')
xsig = sig.readframes(214748000)
xsig = fromstring(xsig, 'Int16')
f = sig.getframerate()
spectrogram = specgram(xsig[0:214748000], Fs = f, scale_by_freq=True, sides='default')
#axis('tight')
plt.axis([0, 6.25, 5500, 22000])
title('DOKI DOKI QR');
show()
sig.close()