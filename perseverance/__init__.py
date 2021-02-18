# Taken from https://codegolf.stackexchange.com/questions/114960/when-will-brexit-happen
from datetime import*
# This is the main file.
def main():
    x = datetime
    while 1:d=x(2021,2,18,15,55)-x.now();s=d.seconds;a=s%3600;print(end=f"\r{d.days:03}:{s//3600:02}:{a//60:02}:{s%60:02}")
