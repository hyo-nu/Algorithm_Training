# 저작권이 있는 멜로디의 개수 
# 앨범에 수록된 곡의 개수
song, avg = map(int,input().split())

melody = song * (avg-1)

print(melody+1)