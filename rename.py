#!/usr/bin/env python3
import os

# Function to replace the character in a filename
def replacechar(filename, inputchar, outputchar):
	os.rename(filename, filename.replace(inputchar, outputchar))
	filename = filename.replace(inputchar, outputchar)
	return filename

for filename in os.listdir("."):
	os.rename(filename, filename.lower())
	filename = filename.lower()

	# Remove unwanted characters
	chars_to_remove = ["?", "!", "'", ",", ")", "]", "*"]
	for ch in chars_to_remove:
		if ch in filename:
			filename = replacechar(filename, ch, "")

	# Replace brackets
	filename = replacechar(filename, " (", "_")
	filename = replacechar(filename, " [", "_")

	# Replace colons
	filename = replacechar(filename, ": ", "_")

	# Replace spaces
	filename = replacechar(filename, " ", "-")

	# Replace &
	filename = replacechar(filename, "&", "and")

        # Replace @
	filename = replacechar(filename, "@", "a")
	filename = replacechar(filename, "á", "a")
	filename = replacechar(filename, "à", "a")
	filename = replacechar(filename, "ä", "a")
	filename = replacechar(filename, "â", "a")
        
        # Replace special characters
	filename = replacechar(filename, "é", "e")
	filename = replacechar(filename, "è", "e")
	filename = replacechar(filename, "ë", "e")
	filename = replacechar(filename, "ê", "e")

	filename = replacechar(filename, "í", "i")
	filename = replacechar(filename, "ì", "i")
	filename = replacechar(filename, "ï", "i")
	filename = replacechar(filename, "î", "i")

	filename = replacechar(filename, "ç", "c")
