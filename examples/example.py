import logging

from log_ext import setup_logger

logger = logging.getLogger('ExampleLogger')


def log_messages():
    try:
        raise TypeError
    except Exception:
        logger.exception('Exception Message')
    logger.critical('Critical Message')
    logger.error('Error Message')
    logger.warning('Warning Message')
    logger.info('Info Message')
    logger.debug('Debug Message')
    logger.trace('Trace Message')


if __name__ == '__main__':
    setup_logger(cfg_file=False)
    logger.setLevel(logging.TRACE)
    log_messages()
