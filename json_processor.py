import requests

URL_PROGRAMS = 'https://cnc.kovalev.team/get/3'
URL_DETAILS = 'https://cnc.kovalev.team/get/5'


def format_time(time: str) -> str:
    '''
    Function to format time to HH:MM:SS
    '''
    hours, mins, secs = time.split(':')
    hours = hours.zfill(2)
    mins = mins.zfill(2)
    secs = secs.zfill(2)
    return ':'.join([hours, mins, secs])


class JSONProcessor:
    def request_programs(self) -> dict[str, str]:
        '''
        Function to request data from programs running machine
        '''
        try:
            json = requests.get(URL_PROGRAMS).json()
            channel_1 = json['data'][1][1]
            all_time, current_time, status, mode, program_time, percentage, program_name = [it[1] for it in channel_1]
            all_time = format_time(all_time)
            current_time = format_time(current_time)
            context = {
                'all_time': all_time,
                'current_time': current_time,
                'status': status,
                'mode': mode,
                'program_time': program_time,
                'percentage': percentage,
                'program_name': program_name,
            }
        except:
            context = {
                'all_time': '-',
                'current_time': '-',
                'status': 'Ошибка выполнения. Повторите еще раз / проверьте оборудование',
                'mode': '-',
                'program_time': '-',
                'percentage': '-',
                'program_name': '-',
            }
        return context

    def request_details(self) -> dict[str, str]:
        '''
        Function to request data from details making machine
        '''
        try:
            json = requests.get(URL_DETAILS).json()
            channel_1 = json['data'][1][1]
            all_time, current_time, status, mode, program_time, percentage, program_name = [it[1] for it in channel_1]
            all_time = format_time(all_time)
            current_time = format_time(current_time)
            context = {
                'all_time': all_time,
                'current_time': current_time,
                'status': status,
                'mode': mode,
                'program_time': program_time,
                'percentage': percentage,
                'program_name': program_name,
            }
        except:
            context = {
                'all_time': '-',
                'current_time': '-',
                'status': 'Ошибка выполнения. Повторите еще раз / проверьте оборудование',
                'mode': '-',
                'program_time': '-',
                'percentage': '-',
                'program_name': '-',
            }
        return context
