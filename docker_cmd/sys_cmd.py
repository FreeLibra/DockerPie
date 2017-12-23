import subprocess


def list_docker_images():
    result = subprocess.getstatusoutput('docker images')
    print(result[0])
    print(result[1])
    with open('./output/output.txt','w') as fp:
        fp.write(result[1])

if __name__ == '__main__':
    list_docker_images()
