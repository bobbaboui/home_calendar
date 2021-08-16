import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd7in5b_V2
import time
from PIL import Image,ImageDraw,ImageFont


from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

logging.basicConfig(level=logging.DEBUG)


#CONFIGURABLES
owm = OWM('')
mgr = owm.weather_manager()




try:
    logging.info("7.5 in waveshare demo")

    epd = epd7in5b_V2.EPD()
    logging.info("initializing screen")
    epd.init()
    logging.info("Clearing screen")
    epd.Clear()

    logging.info("looking for open weather API key")
    logging.info(os.getenv("WEATHER_API"))


    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'),18)

except IOError as e:
    logging.info(e)