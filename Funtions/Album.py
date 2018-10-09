def make_album(artistname, albumtitle, track = ''):
    full = {'Name': artistname, 'Title': albumtitle}
    if track:
        full['track'] = track
    return full


mus = make_album('atif', 'kyun', track=88)
print(mus)
print(make_album('fateh', 'ali'))
print(make_album('rafid', 'ali'))