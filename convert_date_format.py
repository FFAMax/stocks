from datetime import datetime, timezone

def convert_date_format(date_string):
    # список форматов дат, которые мы будем использовать для распознавания даты
    date_formats = [
        '%Y-%m-%d',
        '%Y/%m/%d',
        '%Y.%m.%d',
        '%d.%m.%Y',
        '%m/%d/%Y',
        '%m-%d-%Y',
#       '%d/%m/%Y',
        '%d-%m-%Y',
        '%d %B %Y',           # дата в формате '01 January 2022'
        '%d %b %Y',           # дата в формате '01 Jan 2022'
        '%Y-%m-%d %H:%M:%S',  # дата со временем в формате '2022-01-01 12:30:00'
        '%Y-%m-%d %H:%M',     # дата со временем в формате '2022-01-01 12:30'
        '%Y-%m-%d %I:%M:%S %p', # дата со временем в формате '2022-01-01 12:30:00 PM'
        '%Y-%m-%d %I:%M %p',    # дата со временем в формате '2022-01-01 12:30 PM'
        '%s',                  # дата в формате Unix Time (количество секунд с 1 января 1970 года)
        '%Y-%m-%d %H:%M:%S %Z', # дата со временем и часовым поясом в формате '2022-01-01 12:30:00 UTC'
        '%Y-%m-%d %H:%M %Z',    # дата со временем и часовым поясом в формате '2022-01-01 12:30 UTC'
    ]
    
    # перебираем форматы дат и пытаемся распознать дату
    for date_format in date_formats:
        try:
            if date_format == '%s':
                # если формат даты - Unix Time, то преобразуем его в datetime
                dt = datetime.fromtimestamp(int(date_string), tz=timezone.utc)
            else:
                # если формат даты не Unix Time, то пробуем распознать его через strptime
                dt = datetime.strptime(date_string, date_format)
            # если дата распознана, то преобразуем ее в формат '%Y-%m-%d' и возвращаем
            return dt.strftime('%Y-%m-%d')
        except ValueError:
            pass
    
    # если дата не распознана ни в одном из форматов, то выбрасываем ошибку
    raise ValueError(f'Cannot parse date: {date_string}')
