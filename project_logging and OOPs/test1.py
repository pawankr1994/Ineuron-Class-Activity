import logging
logging.basicConfig(filename='test1.log', level= logging.INFO, format= '%(levelname)s %(asctime)s %(name)s %(message)s ')
logging.info('this is info msg')
l = [1,2,4,4,5,6,6]
for i in l:
    if i == 2:
        logging.info(l)
        logging.warning('this is warning for user')