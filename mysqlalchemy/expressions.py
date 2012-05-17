import sqlalchemy as sa
import sqlalchemy.ext.compiler

class IntervalUnit(object):
    def __init__(self, unit_name, unit_format):
        self.unit_name = unit_name
        self.unit_format = unit_format

    def format(self, values):
        return self.unit_format.format(values) + " " + self.unit_name

class Interval(sa.sql.expression.Function):
    """
    `Date and Time Functions <http://dev.mysql.com/doc/refman/5.1/en/date-and-time-functions.html>`_

    ::
        unit Value	Expected expr Format
        MICROSECOND	MICROSECONDS
        SECOND	SECONDS
        MINUTE	MINUTES
        HOUR	HOURS
        DAY	DAYS
        WEEK	WEEKS
        MONTH	MONTHS
        QUARTER	QUARTERS
        YEAR	YEARS
        SECOND_MICROSECOND	'SECONDS.MICROSECONDS'
        MINUTE_MICROSECOND	'MINUTES:SECONDS.MICROSECONDS'
        MINUTE_SECOND	'MINUTES:SECONDS'
        HOUR_MICROSECOND	'HOURS:MINUTES:SECONDS.MICROSECONDS'
        HOUR_SECOND	'HOURS:MINUTES:SECONDS'
        HOUR_MINUTE	'HOURS:MINUTES'
        DAY_MICROSECOND	'DAYS HOURS:MINUTES:SECONDS.MICROSECONDS'
        DAY_SECOND	'DAYS HOURS:MINUTES:SECONDS'
        DAY_MINUTE	'DAYS HOURS:MINUTES'
        DAY_HOUR	'DAYS HOURS'
        YEAR_MONTH	'YEARS-MONTHS'

    """

    # Units
    MICROSECOND = IntervalUnit('MICROSECOND', "{microseconds}")
    SECOND = IntervalUnit('SECOND', "{seconds}")
    MINUTE = IntervalUnit('MINUTE', "{minutes}")
    HOUR = IntervalUnit('HOUR', "{hours}")
    DAY = IntervalUnit('DAY', "{days}")
    WEEK = IntervalUnit('WEEK', "{weeks}")
    MONTH = IntervalUnit('MONTH', "{months}")
    QUARTER = IntervalUnit('QUARTER', "{quarters}")
    YEAR = IntervalUnit('YEAR', "{years}")
    SECOND_MICROSECOND = IntervalUnit('SECOND_MICROSECOND', "'{seconds}.{microseconds}'")
    MINUTE_MICROSECOND = IntervalUnit('MINUTE_MICROSECOND', "'{minutes}:{seconds}.{microseconds}'")
    MINUTE_SECOND = IntervalUnit('MINUTE_SECOND', "'{minutes}:{seconds}'")
    HOUR_MICROSECOND = IntervalUnit('HOUR_MICROSECOND', "'{hours}:{minutes}:{seconds}.{microseconds}'")
    HOUR_SECOND = IntervalUnit('HOUR_SECOND', "'{hours}:{minutes}:{seconds}'")
    HOUR_MINUTE = IntervalUnit('HOUR_MINUTE', "'{hours}:{minutes}'")
    DAY_MICROSECOND = IntervalUnit('DAY_MICROSECOND', "'{days} {hours}:{minutes}:{seconds}.{microseconds}'")
    DAY_SECOND = IntervalUnit('DAY_SECOND', "'{days} {hours}:{minutes}:{seconds}'")
    DAY_MINUTE = IntervalUnit('DAY_MINUTE', "'{days} {hours}:{minutes}'")
    DAY_HOUR = IntervalUnit('DAY_HOUR', "'{days} {hours}'")
    YEAR_MONTH = IntervalUnit('YEAR_MONTH', "'{years}-{months}'")

    units = [
        MICROSECOND,
        SECOND,
        MINUTE,
        HOUR,
        DAY,
        WEEK,
        MONTH,
        QUARTER,
        YEAR,
        SECOND_MICROSECOND,
        MINUTE_MICROSECOND,
        HOUR_MICROSECOND,
        HOUR_SECOND,
        HOUR_MINUTE,
        DAY_MICROSECOND,
        DAY_SECOND,
        DAY_MINUTE,
        DAY_HOUR,
        YEAR_MONTH,
    ]

    def __init__(self, unit, microseconds=None, seconds=None, minutes=None, hours=None,
                 days=None, weeks=None, months=None, quarters=None, years=None):
        super(Interval, self).__init__('Interval')
        assert unit in self.units

        self.unit = unit
        self.values = dict(
            microseconds = microseconds,
            seconds = seconds,
            minutes = minutes,
            hours = hours,
            days = days,
            weeks = weeks,
            months = months,
            quarters = quarters,
            years = years,
        )

@sa.ext.compiler.compiles(Interval, 'mysql')
def mysql_interval(element, compiler, **kw):
    return "INTERVAL " + element.unit.format(element.values)