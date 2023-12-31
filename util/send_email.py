import smtplib
from email.mime.text import MIMEText

class SendEmail:
    global send_user
    global email_host
    global password
    send_user = '18721268250@163.com'
    email_host = 'smtp.163.com'
    password = ''

    def send_email(self, user_list, sub, content):
        user = "18721268250"+"<"+send_user+">"
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user, password)
        server.sendmail(user, user_list, message.as_string())
        server.close()

    def send_main(self, pass_list, fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        total_num = pass_num + fail_num

        pass_result = '%.2f%%' %(pass_num/total_num*100)
        fail_result = '%.2f%%' %(fail_num/total_num*100)
        user_list = ['1243727831@qq.com']
        sub = "接口自动化测试报告"
        content = "此次一共运行接口%s个，通过个数为%s个，失败个数为%s个，通过率为%s，失败率为%s" %(total_num, pass_num, fail_num, pass_result, fail_result)

        self.send_email(user_list, sub, content)

if __name__ == '__main__':
    sen = SendEmail()
    # user_list = ['1243727831@qq.com']
    # sub = "接口自动化测试报告"
    # content = ""
    # sen.send_email(user_list, sub, content)

    sen.send_main([1,2,3,5,6], [4,7,8])

