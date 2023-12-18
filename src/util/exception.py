import sys

from util.logger import logging

class CustomException(Exception):
    def __init__(self, message: str, details: sys) -> None:
        super().__init__(message)
        self._custom_message = self._err_msg(message, details)

    def _err_msg(self, message: str, details: sys) -> str:
        _,_,exc_traceback = details.exc_info()
        filename = exc_traceback.tb_frame.f_code.co_filename
        lineno = exc_traceback.tb_lineno
        message = str(message)
        return f'Error occured in python script name [{filename}] line number [{lineno}] error message [{message}]'
    
    def __str__(self) -> str:
        return self._custom_message
    
if __name__ == '__main__':
    try:
        a=1/0
    except Exception as e:
        logging.info('Divide by zero')
        raise CustomException(e, sys)
