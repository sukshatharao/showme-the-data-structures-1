#!/usr/bin/env python
# coding: utf-8

# In[18]:


import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    files = []
    if len(path)==0 or len(suffix)==0:
        return None
    try:
        for i in os.listdir(path):
            temp1 = os.path.join(path,i)
            #print("temp1 is", temp1)
            if os.path.isfile(temp1) and temp1.endswith(".c"):
                files.append(temp1)
            elif os.path.isdir(temp1):
                files.extend(find_files(suffix, temp1))
        return files
    except:
        print("ooops! not a directory")

print("\n\t\t\t\tTest case 1")
files_1 = find_files('.c', 'testdir')
print(files_1)

print("\n\t\t\t\tTest case 2")
files_2 = find_files('.c', 'testdir/subdir3')
print(files_2)

print("\n\t\t\t\tTest case 3")
files_3 = find_files('.c', '')   #returns None, since there is no path defined
print(files_3)

print("\n\t\t\t\tTest case 4")
files_4 = find_files('', 'testdir')  #returns None, since there is no suffix defined
print(files_4)

print("\n\t\t\t\tTest case 5")
files_5 = find_files('.c', 'fakedir')  
print(files_5)


# In[ ]:





# In[ ]:




