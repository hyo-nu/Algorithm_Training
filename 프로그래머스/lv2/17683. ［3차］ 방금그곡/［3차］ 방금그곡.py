def solution(m, musicinfos):
    m = m.replace('C#','c').replace('D#','d').replace('G#','g')
    m = m.replace('F#','f').replace('A#','a')
    
    music_lst = []
    for info in musicinfos:
        ST, ET, title, melody = info.split(',')
        melody = melody.replace('C#','c').replace('D#','d').replace('G#','g')
        melody = melody.replace('F#','f').replace('A#','a')
        
        EH, EM = map(int,ET.split(':'))
        SH, SM = map(int,ST.split(':'))
        
        time = (EH - SH) * 60 + (EM - SM)
        melody = melody * (time//len(melody)) + melody[:time%len(melody)]
        
        if m in melody : music_lst.append((title,time))
    
    music_lst.sort(key = lambda x : -x[1])
    if music_lst : return music_lst[0][0]
    else: return "(None)"
