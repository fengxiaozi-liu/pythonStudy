def judge_ip(ip):
    if '.' in ip:
        if ip.count('.') == 3:
            every_ip_list = ip.split('.')
            for every in every_ip_list:
                ip_num = int(every)
                if 0 <= ip_num <= 255:
                    return f'您输入的ip-{ip}合法'
                return f'输入的ip-{ip}不合法'
        return f'输入的ip-{ip}不合法'
    return f'输入的ip-{ip}不合法'


if __name__ == '__main__':
    result = judge_ip('256.169.255.254')
    print(result)
