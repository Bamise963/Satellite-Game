import pgzrun, random

WIDTH=600
HEIGHT=800

station=[]
lines=[]

next_satellite=0
number_of_satellite=10

for i in range(number_of_satellite):
    satellite=Actor("satellite (1)")
    satellite.x=(random.randint(0,550))
    satellite.y=(random.randint(0,750))
    station.append(satellite)


def draw():
    screen.blit("space background",(0,0))
    number=1
    for i in station:
        screen.draw.text(str(number),(i.pos[0],i.pos[1]+10))
        i.draw()
        number=number+1
    for i in lines:
       screen.draw.line(i[0],i[1],color="white")

def on_mouse_down(pos):
  global next_satellite, lines
  if next_satellite < number_of_satellite:
    if station[next_satellite].collidepoint(pos):
      if next_satellite:
          lines.append((station[next_satellite-1].pos,station[next_satellite].pos))  
      next_satellite+=1
    else:
      lines=[]


pgzrun.go()