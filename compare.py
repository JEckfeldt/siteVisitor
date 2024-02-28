import os #module for file listing

path = 'jakeLaptop/' # path for directory
txtFiles = os.listdir(path) # list of all text files names

results = {}

keys = ['userAgent', 'visitorID', 'confidenceScore', 'fonts', 'cookies', 'resolution', 
        'platform', 'canvasGeometry', 'canvasText', 'canvas1', 'canvas2', 'canvas3', 'canvas4', 'canvas5']

# Start with first name and compare all entries to that one
firstFile = open(path + txtFiles[0], "r").readlines()
first = {} # Put first file into object with key/value
for i in range(14):
    first[keys[i]] = firstFile[i].split(": ", 1)[1].strip()

# Compare this one to the rest of the files
for file in txtFiles:
    currLines = open(path + file, "r").readlines()
    curr = {}
    for i in range(14): # Populate the curr file into an object
        curr[keys[i]] = currLines[i].split(": ", 1)[1].strip()

        # Compare current line in object to same field in firstFile
        if (curr[keys[i]] != first[keys[i]]):
            if keys[i] not in results:
                results[keys[i]] = 1
            else:
                results[keys[i]] = results[keys[i]] + 1

            
print(results)