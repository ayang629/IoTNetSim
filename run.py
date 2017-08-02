import logging
import os
import sys
import netsim_Vis
from netsim_YAML import run
from netsim_NS3 import experiment


if __name__ == "__main__":
    if len(sys.argv) >= 2 and os.path.isfile(sys.argv[1]): #check cmd arg
        topology = dict()
        try:
            topology = run(sys.argv[1]) #parse yaml
        except Exception as e:
            logging.exception("YAML Parsing stage failed.")
        try:
            info_to_feed_into_visualizations = experiment(topology) #NS3 exp
        except Exception as e:
            logging.exception("NS3 Experimentation failed.")
        try:
            netsim_Vis.visA(info_to_feed_into_visualizations) #some visualization
            #... and so on
        except Exception as e:
            logging.exception("Visualizations failed")

        sys.exit(0) #everything ended ok
    sys.exit("Invalid argument provided to script.") #something went wrong
