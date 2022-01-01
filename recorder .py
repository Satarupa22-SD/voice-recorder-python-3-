#!/usr/bin/env python
# coding: utf-8

# In[31]:


pip install sounddevice


# In[32]:


import sounddevice


# In[33]:


pip install scipy


# In[34]:


from scipy.io.wavfile import write


# In[35]:


fps= 44100


# In[36]:


duration= 10


# In[37]:


print("recording...")


# In[38]:


recording = sounddevice.rec((int)(duration*fps),samplerate=fps,channels=2)


# In[39]:


sounddevice.wait()
print("done!!")


# In[40]:


write("output.wav",fps,recording)


# In[ ]:




