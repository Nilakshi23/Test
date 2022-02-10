from jenkinsapi.jenkins import Jenkins

def get_server_instance():
    jenkins_url = 'http://52.55.241.243:8080/'
    server = Jenkins(jenkins_url, username='nilaxshi', password='12345')
    return server
    
def get_job_details():
    # Refer Example #1 for definition of function 'get_server_instance'
    server = get_server_instance()
    for job_name, job_instance in server.get_jobs():
        print('Job Name:%s' %(job_instance.name))
        print('Job Description:%s' %(job_instance.get_description()))
        print('Is Job running:%s' %(job_instance.is_running()))
        print('Is Job enabled:%s' %(job_instance.is_enabled()))

get_job_details()

def chatbot() :
	from json import dumps

from httplib2 import Http


def main():
    """Hangouts Chat incoming webhook quickstart."""
    url = 'https://chat.googleapis.com/v1/spaces/AAAARM7dFAE/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=73W5Cltjjjv3IGdUv0MWoMP8eegMavqPu3HpAYTeL5I%3D'
    bot_message = {
        'text' : "Job_name %s" %(job_instance.name) }

    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )

    print(response)

if __name__ == '__main__':
    main()
	
chatbot()
