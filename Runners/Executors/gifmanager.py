import random
from console import Swdconsole_logs

con_logs = Swdconsole_logs()


class kiss:
    first = "https://media.tenor.com/kQnRjkRiCDEAAAAM/kiss-dragon.gif"
    second = "https://media.tenor.com/KWis0FtrliwAAAAM/kiss.gif"
    third = "https://media.tenor.com/IOhsdpwBTKEAAAAM/proto-protogen.gif"

class hug:
    first = "https://media.tenor.com/EvBFUgZxmREAAAAM/dragon-sleepy.gif"
    second = "https://media.tenor.com/9oKHJBp5Ih4AAAAM/hug.gif"
    third = "https://media.tenor.com/dbr_rrtqRAkAAAAM/sleep-goodnight.gif"

class nom:
    first = "https://media.tenor.com/Um4G1x3HDjsAAAAM/cat-nom.gif"
    second = "https://media.tenor.com/syQg9pspRZcAAAAj/cat-bug.gif"
    third = "https://media.tenor.com/rsZL2pAOrIMAAAAM/nom-kitty.gif"

class nuzzle:
    first = "https://media.tenor.com/O563172BEbwAAAAM/dragon-love.gif"
    second = "https://media.tenor.com/7OoXtJA5jgkAAAAM/nuzzle-hug.gif"
    third = "https://media.tenor.com/wZPgHXme7k8AAAAM/fwenchfwy-fwench.gif"

class boop:
    first = "https://media.tenor.com/1G5K4yLKliUAAAAj/furry-synth.gif"
    second = "https://media.tenor.com/26O5j4-MLMoAAAAM/boop-furry.gif"
    third = "https://media.tenor.com/eOoQ_YB2IF8AAAAM/protogen-boop.gif"

class bite:
    first = "https://media.tenor.com/05Ria84wJBwAAAAM/kellygoblin-furry.gif"
    second = "https://media.tenor.com/nT8TOVv6oK8AAAAj/bite.gif"
    third = "https://media.tenor.com/i8_lPl9OQ1sAAAAM/love-cute.gif"

class lick:
    first = "https://media.tenor.com/fElVKhapK9wAAAAM/dragon-derg.gif"
    second = "https://media.tenor.com/gaWXoZBAoIAAAAAM/dragon-muzzle.gif"
    third = "https://media.tenor.com/GOHNpS3_9y8AAAAj/dragon-lick.gif"

class blush:
    first = "https://media.tenor.com/DkRz324vhxUAAAAM/dragon-blushing.gif"
    second = "https://media.tenor.com/4vWMW-CcLWQAAAAM/shamewing-jrod19.gif"
    third = "https://media.tenor.com/FXdTK3eUXPIAAAAM/owo-furry.gif"

class wiggle:
    first = "https://media.tenor.com/LRiRld7fp68AAAAM/dragon-wiggle.gif"
    second = "https://media.tenor.com/AovA_j2Yec4AAAAM/wiggle-dragon.gif"
    third = "https://media.tenor.com/zJCAajYqz1gAAAAM/dancing-dragon-wiggle.gif"

class happy:
    first = "https://media.tenor.com/ONC8XSJU_7cAAAAM/dragon-splash.gif"
    second = "https://media.tenor.com/LJOBARM0FVsAAAAM/happy-dragon-fly.gif"
    third = "https://media.tenor.com/t2pr42i4RHMAAAAM/zym-dragon-prince.gif"

class Swdgif_selector:
    def __init__(self):
        con_logs.call("Gifmanager")

    def get_gif(self, type: str):
        if type == "kiss":
            rgif = random.choice([kiss.first, kiss.second, kiss.third])
        elif type == "hug":
            rgif = random.choice([hug.first, hug.second, hug.third])
        elif type == "nom":
            rgif = random.choice([nom.first, nom.second, nom.third])
        elif type == "nuzzle":
            rgif = random.choice([nuzzle.first, nuzzle.second, nuzzle.third])
        elif type == "boop":
            rgif = random.choice([boop.first, boop.second, boop.third])
        elif type == "bite":
            rgif = random.choice([bite.first, bite.second, bite.third])
        elif type == "lick":
            rgif = random.choice([lick.first, lick.second, lick.third])
        elif type == "blush":
            rgif = random.choice([blush.first, blush.second, blush.third])
        elif type == "wiggle":
            rgif = random.choice([wiggle.first, wiggle.second, wiggle.third])
        elif type == "happy":
            rgif = random.choice([happy.first, happy.second, happy.third])

        return rgif