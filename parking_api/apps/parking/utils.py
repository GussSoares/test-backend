import re

import humanize


class PlateValidatior:
    """Validate vehicle plate"""

    @staticmethod
    def validate(plate: str, mercosul: bool = False):
        """validate method

        Parameters:
            plate (str): vehicle plate

        Returns:
            bool: True if plate is valid else False
        """
        if mercosul:
            return re.fullmatch(
                r"^[a-zA-Z]{3}[0-9][A-Za-z0-9][0-9]{2}$", plate
            )
        else:
            return re.fullmatch(r"^[a-zA-Z]{3}-[0-9]{4}$", plate)


def humanize_timedelta(value):
    """
    return timedelta humanized
    """
    return humanize.naturaldelta(value)
