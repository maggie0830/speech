from subprocess import Popen, PIPE, STDOUT

slave = Popen(['ruby', 'slave.rb'], stdin=PIPE, stdout=PIPE, stderr=STDOUT)

while True:
    # read user input, expression to be evaluated:
    line = "asd"
    # write that line to slave's stdin
    slave.stdin.write(bytes(line+'\n', "UTF-8"))
    # result will be a list of lines:
    result = []
    # read slave output line by line, until we reach "[end]"
    while True:
        print("lool")
        # check if slave has terminated:
        if slave.poll() is not None:
            print('slave has terminated.')
            exit()
        # read one line, remove newline chars and trailing spaces:
        
        line = slave.stdout.readline().rstrip()
        print('line:', line)
        if line == '[end]':
            print("fuck")
            break
#        result.append(line)
#    print('result:')
#    print('\n'.join(result))


# from subprocess import Popen, PIPE, STDOUT
#
# slave = Popen(['ruby', 'slave.rb'], stdin=PIPE, stdout=PIPE, stderr=STDOUT)
#
# while True:
#     # read user input, expression to be evaluated:
#     line = "asd"
#     # write that line to slave's stdin
#     slave.stdin.write(line+'\n')
#     # result will be a list of lines:
#     result = []
#     # read slave output line by line, until we reach "[end]"
#     while True:
#         # check if slave has terminated:
#         if slave.poll() is not None:
#             print('slave has terminated.')
#             exit()
#         # read one line, remove newline chars and trailing spaces:
#         line = slave.stdout.readline().rstrip()
#         #print 'line:', line
#         if line == '[end]':
#             break
#         result.append(line)
#     print('result:')
#     print('\n'.join(result))
