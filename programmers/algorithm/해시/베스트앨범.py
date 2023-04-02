class Genre:
    totalPlays = 0
    childPlay = []  # index, play
    
    def __init__(self):
        self.totalPlays = 0
        self.childPlay = []

    def appendPlay(self, index, playCount):
        self.totalPlays += playCount
        self.childPlay.append([index, playCount])

    def sort(self):
        self.childPlay.sort(key=lambda x:(-x[1],x[0]))

def solution(genres, plays):
    answer = []
    genreMap = {}
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre not in genreMap:
            genreMap[genre] = Genre()
        genreMap[genre].appendPlay(i, play)
    tmp = sorted(genreMap.values(), key=lambda x:-x.totalPlays)
    for genreObject in tmp:
        genreObject.sort()
        for play in genreObject.childPlay[:2]:
            answer.append(play[0])
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))