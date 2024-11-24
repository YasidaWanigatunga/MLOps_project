import sys


def error_message_detail(error, error_detail: sys):
    try:
        _, _, exc_tb = error_detail.exc_info()
        if exc_tb is None:
            raise ValueError("No traceback found. Ensure this function is called within an exception handling block.")

        file_name = exc_tb.tb_frame.f_code.co_filename
        error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
            file_name, exc_tb.tb_lineno, str(error)
        )
        return error_message
    except Exception as inner_error:
        return f"Failed to extract error details: {inner_error}"


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
