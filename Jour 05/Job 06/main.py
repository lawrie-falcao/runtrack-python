def arrondir_notes(notes):
    notes_arrondies = []
    for note in notes:
        if note < 40:
            notes_arrondies.append(note)
        else:
            multiple_de_5_sup = (note // 5) * 5 + 5
            if multiple_de_5_sup - note < 3:
                notes_arrondies.append(multiple_de_5_sup)
            else:
                notes_arrondies.append(note)
    return notes_arrondies
notes = [75, 62, 47, 83, 39, 91]
notes_arrondies = arrondir_notes(notes)
print(notes_arrondies)