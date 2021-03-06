# py_logging_extensions
a wrapper to provide advanced logging capability with a simple call

Provides:
* coloured logging (If colorama installed)
* Log to file
* configuration file is generated for log formats and colours
* different log format for levels of logging.DEBUG and below
* TRACE logging level added as a level below logging.DEBUG (set to 5)


## Basic Usage

```python
    import logging
    
    # Import and setup the logger
    from log_ext import setup_logger
    setup_logger()

    # Create a normal logging instance, and use as per normal docs
    logger = logging.getLogger('ExampleLogger')
    logger.setLevel(logging.DEBUG)
    logger.debug('MyDebugMessage')
```

# setup_logger
```python
setup_logger(
    name='log',
    base_logger=None,
    log_dir='logs',
    cfg_file='log.yaml',
    config={
        'date_fmt': '%Y-%m-%d_%H:%M:%S',
        'format_str': '%(asctime)17s-%(name)-12s-%(levelname)-8s-%(message)s',
        'detailed_format_str': '(%(module)s-%(funcName)s #%(lineno)d)',
        'colors': {
            'TRACE': 'Back.WHITE,Fore.BLACK',
            'DEBUG': 'Fore.CYAN',
            'INFO': 'Fore.GREEN', 
            'WARNING': 'Fore.YELLOW', 
            'ERROR': 'Fore.RED', 
            'CRITICAL': 'Back.RED,Fore.WHITE'
        }
    },
    trace_logging=True,
    clear_others=False,
    handles=None)
```
Setup a logger (call instead of logging.basicConfig)

    :param name: (String) log file name
    :param base_logger: (logging.Logger) logger to base off - uses root if not set
    :param log_dir: (string | False) directory to store log files in - doesn't log to file if set to False
    :param cfg_file: (string | False) configuration file to use, or false to skip creating a file
    :param config: (Dict) configuration dictionary see CONFIG variable for example
    :param trace_logging: (Bool) use trace logging
    :param clear_others: (Bool) clear existing handlers on the base logger
    :param handles: (List) also add these handlers to the base logger
    :returns None



