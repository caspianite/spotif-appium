import time
def set(driver, proxy_dict):
    ip = str(proxy_dict["ip"])
    port = str(proxy_dict["port"])
    username = str(proxy_dict["username"])
    password = str(proxy_dict["password"])
    commands = [
                'settings put global http_proxy ' + ip + ":" + port,
                # "put|global|global_http_proxy_host|" + proxy_dict["ip"],
                # "put|global|global_http_proxy_port|" + proxy_dict["port"]
                ]

    # if len(proxy_dict["username"]) > 0:
    #     commands.extend([
    #         'put global http_proxy_username ' + username,
    #         'put global http_proxy_password ' + port
    #     ])

    for command in commands:
        driver.execute_script('mobile: shell', {
            'command': command,
            'args': [],
            'includeStderr': True,
            'timeout': 5000
        })
        time.sleep(0.1)

def reset(driver):
    commands = [
                # "settings delete global http_proxy",
                # "settings delete global global_http_proxy_host",
                # "settings delete global global_http_proxy_port",
                # "settings delete global global_http_proxy_username",
                # "settings delete global global_http_proxy_password",
                # "settings delete global global_http_proxy_exclusion_list",
                # "settings delete global global_proxy_pac_url",
                "settings put global http_proxy :0"
                ]

    for command in commands:
        driver.execute_script('mobile: shell', {
            'command': command,
            'args': [],
            'includeStderr': True,
            'timeout': 5000
        })
        time.sleep(0.1)
    print("")


def parse(proxy_list):
    proxy_dict_list = []
    for proxy in proxy_list:
        p = proxy.split(":")
        proxy_dict = {}
        proxy_dict["ip"] = p[0]
        proxy_dict["port"] = p[1]

        if len(p) == 4:
            proxy_dict["username"] = p[2]
            proxy_dict["password"] = p[3]
        else:
            proxy_dict["username"] = "",
            proxy_dict["password"] = ""
        proxy_dict_list.append(proxy_dict)
    # print(proxy_dict_list)
    return proxy_dict_list




def check(proxy_dict):
    print("")





