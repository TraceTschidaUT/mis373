def BuildSong():

    s_file = open('skeleton_SamuraiShowdown.txt', 'r')
    e_file = open('endings.txt', 'r')

    endings = {}
    rhythms = {}
    rap_verse = []

    # load the ending.txt file into memory
    for line in e_file:

        # Clean the line
        clean_line = line.strip()

        # Split the line into its componet parts
        # idx 0 = end words
        # idx 1 = rhythm word
        # idx 2 = beats in word
        words = clean_line.split('::')
        words[2] = int(words[2])

        # add the endings to the dictionary
        endings[words[0]] = (words[1], words[2])
        if words[1] in rhythms:

            # Get the List of words and beats
            words_and_beats = rhythms[words[1]]

            # idx 0 = rhythm words
            # idx 1 = beats in word
            words_and_beats.append((words[0], words[2]))
        
        else:

            # Add a list containing Tuples of words and beats
            rhythms[words[1]] = [(words[0], words[2])]

    previous_total_beats = None
    previous_rhythm = None

    for line in s_file:

        # Clean the line endings
        clean_line = line.strip()

        # Split the line into its componet parts
        # idx 0 = prefix words
        # idx 1 = beats in prefix
        # idx 2 = ending words or 'XXX'
        words = clean_line.split('::')
        words[1] = int(words[1])

        if words[2] == 'XXX':

            # Locate the word(s) that have the same rhythms
            same_rhythm_words = rhythms[previous_rhythm]

            # Determine the number of beats needed
            beats_needed = previous_total_beats - words[1]

            # Find the right word with correct rhythm and beats needed
            for ending_word in same_rhythm_words:
                
                # Match the correct beats needed
                if beats_needed == ending_word[1]:
                    
                    # change the last word
                    words[2] = ending_word[0]
        elif words[2] == '':
            # do nothing
            pass
        else:
            # Locate the ending words in the ending dictionary
            verse_stats = endings[words[2]]
            previous_total_beats = words[1] + verse_stats[1]
            previous_rhythm = verse_stats[0]


        rap_verse.append(words)
        print words[0] + ' ' + words[2]

BuildSong()
