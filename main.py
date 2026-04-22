# 3-m
class MusicPlayer:
    def __init__(self, song):
        self.song = song

    def play(self):
        print(f"{self.song} chalinyapti")

    def stop(self):
        print("To‘xtatildi")


m = MusicPlayer("song.mp3")
m.play()
m.stop()

# 4-m
class Robot:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    def work(self):
        if self.energy > 0:
            print("Robot ishlayapti")
        else:
            print("Energiya yo‘q")


r = Robot("Robo", 10)
r.work()
