import client
from template import Template

if __name__ == '__main__':
    payload = Template().parse()
    client.send(payload)
