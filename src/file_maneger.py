import os


def mkdir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError as e:
        print('Error: ' + str(e))


def new_file(filename):
    f = open(filename, 'w', encoding='utf-8')
    f.close()


def new_project(path, project_name):
    # Make Project Directory
    mkdir("%s/%s" % (path, project_name))

    mkdir("%s/%s/Resources" % (path, project_name))
    new_file("%s/%s/format.json" % (path, project_name))


# For test
if __name__ == '__main__':
    test_name = input("Enter New Project: ")
    new_project("../test_skin", test_name)
