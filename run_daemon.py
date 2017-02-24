import sys
import time
from daemon import Daemon
import argparse


class MyDaemon(Daemon):

    def run(self):
        while True:
            logging.info("Creating local DB")
            init_db()
            logging.info("Starting processing")
            main()
            logging.info("Copying DB to UI folder")
            result = copy_db()
            if result:
                logging.info("Finished successfully")
            else:
                logging.info("Finished with errors")
            time.sleep(60)


if __name__ == "__main__":
    log_file = "{}/run_output.log".format(LOG_DIR)
    daemon = MyDaemon('{}/mysilename.pid'.format(TMP_DIR),
                      stdout=log_file, stderr=log_file)
    parser = argparse.ArgumentParser()
    parser.add_argument("action", help="Starts/stops/restarts agent", type=str)
    args = parser.parse_args()
    if args.action == "start":
        logging.info("Starting agent ....")
        daemon.start()
    elif args.action == "stop":
        logging.info("Stopping agent ....")
        daemon.stop()
    elif args.action == "restart":
        logging.info("Re-starting agent ....")
        daemon.stop()
        daemon.start()
