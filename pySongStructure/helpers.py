import numpy as np
import librosa

def get_label_groups(y, sections, labels):
    '''
    Parses labels and sections to generate a mapping of labels to actual sections and a measure of how percussive each section is
    
    Parameters
    ----------
    y: Audio signal
    sections: Array of tuples that describe the end and start times of each section
    labels: Array describing sections relations to one another. Signals that share similarities have the same label.
        
    Returns
    -------
    label_groups:
        A Dictionary from labels to their corresponding sections. 
        E.g. 
        If sections 0, 1 and 3 share similarities and sections 2, 4 share similarities
        {
            1: [(0, p), (1, p), (3, p)],
            2: [(2, p), (4, p)],
        }
        where each `p` is the percussive score of its corresponding section.
    '''

    label_groups = {}
    for i in range(len(labels)):
        if labels[i] not in label_groups:
            label_groups[labels[i]] = []
        percussiveness = librosa.effects.percussive(y[sections[i][0]:sections[i][1]])
        score = sum(abs(percussiveness))
        label_groups[labels[i]].append((i, score))

    return label_groups
    
def clean_labels(_labels):
    '''
    Makes label ids start at 0 and end at num_unique_sections 

    Parameters
    ----------
    _labels: old labels that need to be cleaned
        
    Returns
    -------
    labels:
        Cleaned labels
    '''

    labels = np.copy(_labels)
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    label_map = {}

    current_index = 0
    for i in range(len(labels)):
        if 'tro' in labels[i]:
            continue
        if labels[i] in label_map:
            labels[i] = alphabet[label_map[labels[i]]]
        else:
            label_map[labels[i]] = current_index
            labels[i] = alphabet[current_index]
            current_index += 1
    
    return labels

def clean_tempos(y, sr, sections):
    '''
    Generates and cleans the estimated tempos of each section by 
    checking for either accidental halving/doubling of tempos
    
    Parameters
    ----------
    y: audio signal
    sections: Array of tuples that describe the end and start times of each section
        
    Returns
    -------
    cleaned_tempos:
        An array of cleaned_tempos
    '''
    tempos = []
    for start, end in sections:
        tempos.append(librosa.beat.tempo(y[start:end], sr)[0])

    cleaned_tempos = [tempos[0]]
    for i in range(len(tempos)-1):
        ratio = tempos[i + 1] / tempos[i]
        if round(ratio) >= 2:
            cleaned_tempos.append(tempos[i+1] / round(ratio))
        elif round(1/ratio) >= 2:
            tempos[i] *= round(ratio)
            cleaned_tempos.append(tempos[i+1])
        else:
            cleaned_tempos.append(tempos[i+1])
        
    return cleaned_tempos

def get_beats_from_boundaries(beats, sections, sr):
    '''
    Converts the boundary values in seconds to beats by snapping the section boundaries to beat values
    
    Parameters
    ----------
    beats: estimated beat values in frames
    sections: Array of tuples that describe the end and start times of each section
    sr: sample rate
        
    Returns
    -------
    section_beats:
        An array of tuples that represent the start/end of each section in terms of beats
    '''

    section_beats = []
    beats = librosa.frames_to_time(beats, sr)
    def find_nearest(array, value):
        array = np.asarray(array)
        idx = (np.abs(array - value)).argmin()
        return idx
    
    for start, end in sections:
        start_s = start/sr
        end_s = end/sr

        start_b = find_nearest(beats, start_s)
        end_b = find_nearest(beats, end_s)

        section_beats.append((int(start_b), int(end_b)))

    return section_beats





