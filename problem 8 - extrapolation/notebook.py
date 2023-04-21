#!/usr/bin/env python
# coding: utf-8

# In[70]:


import numpy as np
import matplotlib.pyplot as plt


# In[78]:


num_given = 40
num_chopped = 20
num_points = num_given+num_chopped

amplitude = np.random.uniform(3, 5)
wavelength = np.random.uniform(0.2, 2)
noise_level = amplitude/7

x = np.linspace(0, 2*np.pi, num_points)
y = amplitude * np.sin(x * wavelength / 2*np.pi)

plt.plot(x, y, color='green')

noise = np.random.normal(0, noise_level, num_given)
y_noisy = y[:num_given] + noise

plt.scatter(x[:num_given], y_noisy, color='blue')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine Wave with Noise')
plt.show()

for xv, yv in zip(x[:num_given], y_noisy):
    print("{},{}".format(xv, yv))


# In[79]:


gpt_continuation = """
4.259786648935312,-2.9704872883258727
4.366281315158695,-1.681620602619956
4.472775981382078,-2.7109912955877224
4.579270647605461,-2.606939754291697
4.685765313828844,-2.963674148747162
4.792259980052226,-3.056447928305092
4.898754646275609,-3.423057903716207
5.005249312498992,-3.8096720449189813
5.111743978722375,-3.8568274066903525
5.218238644945758,-4.168844291694532
5.3247333111691405,-4.145089271821258
5.431227977392523,-4.103259245087475
5.537722643615906,-4.615302616563718
5.644217309839289,-4.764482512819691
5.750711976062671,-4.857948044831842
5.857206642286054,-5.191116235302568
5.963701308509437,-5.094064729755822
6.07019597473282,-5.345728834983966
6.176690640956202,-5.678449845221634
6.283185307179585,-5.54652470786963
6.389679973402968,-5.664900965958538
6.496174639626351,-5.620425469932784
6.602669305849734,-5.683731178189461
6.709163972073117,-5.816679526888947
6.8156586382965,-5.940719417550261
6.922153304519882,-5.957454475963688
7.028647970743265,-5.7640179472907835
7.135142636966648,-5.902177341179938
7.241637303190031,-5.860009789272583
7.348131969413414,-5.909981601932845
7.454626635636796,-5.875844641133759
7.561121301860179,-5.94247847268422
7.667615968083562,-5.9543252557411245
7.774110634306945,-6.0541120500301345
7.880605300530327,-6.1135873758965085
7.98709996675371,-5.8999965758466375
8.093594632977093,-6.0106019333546825
8.200089299200476,-5.9988756665153875
8.306583965423859,-6.0425641611090135
8.413078631647242,-5.95847278969752
8.519573297870625,-5.9831123021199315
8.626067964094008,-6.053142580635604
8.73256263031739,-6.05603583855548
8.839057296540773,-6.073275473698143
8.945551962764156,-6.0407789035740415
9.052046628987539,-6.1014266855365555
9.158541295210921,-5.921558799529784
"""


# In[80]:


xgpt = []
ygpt = []

lines = gpt_continuation.split('\n')
for line in lines:
    if line == '':
        continue
    values = line.split(',')
    xgpt.append(float(values[0]))
    ygpt.append(float(values[1]))

#xgpt, ygpt


# In[81]:


plt.plot(x, y, color='green')
plt.scatter(x[:num_given], y_noisy, color='blue')
plt.scatter(xgpt, ygpt, color='red')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine Wave with Noise')
plt.show()


# ------------------
# 
# # Line
# 

# In[104]:


num_given = 40
num_chopped = 20
num_points = num_given+num_chopped

line_m = np.random.uniform(-10, 10)
line_c = np.random.uniform(1, 10)
noise_level = np.random.uniform(1, 3)

x = np.linspace(0, 2*np.pi, num_points)
y = line_m * x + line_c

plt.plot(x, y, color='green')

noise = np.random.normal(0, noise_level, num_given)
y_noisy = y[:num_given] + noise

plt.scatter(x[:num_given], y_noisy, color='blue')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Line with Noise')
plt.show()

for xv, yv in zip(x[:num_given], y_noisy):
    print("{},{}".format(xv, yv))


# In[106]:


gpt_continuation = """
4.259786648935312,-34.57429387191755
4.366281315158695,-35.94092435687065
4.472775981382078,-29.67512207666228
4.579270647605461,-31.28459833506567
4.685765313828844,-33.95579276535722
4.792259980052227,-30.55624100878303
4.898754646275609,-33.761559731914685
5.005249312498992,-30.517949233488534
5.111743978722375,-29.925722034111935
5.218238644945758,-35.29008454829199
5.324733311169141,-30.496590617097032
5.431227977392523,-35.62355043257917
5.537722643615906,-34.99496004483338
5.644217309839289,-34.039726081110746
5.750711976062672,-37.417005908506654
5.857206642286055,-37.51639946786166
5.963701308509437,-36.35724274769521
6.07019597473282,-36.40142503572218
6.176690640956203,-38.715744482307186
6.283185307179586,-39.30311814216469
6.389679973402969,-39.63812934842916
6.496174639626352,-39.60670687861136
6.602669305849734,-39.555751837461506
6.709163972073117,-39.8991092692716
6.8156586382965,-43.041456548102175
6.922153304519883,-43.51085532968987
7.028647970743266,-43.19975748408098
7.135142636966648,-43.94347418142214
7.241637303190031,-45.299334491306
7.348131969413414,-44.26774513880905
7.454626635636797,-43.95305033136394
7.56112130186018,-43.75243360502122
7.667615968083562,-44.31887645108162
7.774110634306945,-45.03781804723231
7.880605300530328,-42.95964780427206
"""


# In[107]:


xgpt = []
ygpt = []

lines = gpt_continuation.split('\n')
for line in lines:
    if line == '':
        continue
    values = line.split(',')
    xgpt.append(float(values[0]))
    ygpt.append(float(values[1]))

#xgpt, ygpt


# In[109]:


plt.plot(x, y, color='green')
plt.scatter(x[:num_given], y_noisy, color='blue')
plt.scatter(xgpt, ygpt, color='red')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Line with Noise')
plt.show()


# In[ ]:


