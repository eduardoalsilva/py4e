string = 'X-DSPAM-Confidence:0.8475'
l = string.split(":")
f = float(l[-1])
print(f)
