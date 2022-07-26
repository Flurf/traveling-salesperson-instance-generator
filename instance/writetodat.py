#function that puts data necessary for the FSTSP into AMPL readable .dat format
def writetodat(filename,params):
    param = 'param '
    defas = ' :=\t'

    f = open(filename + '.dat', "a")

    for i in params:
        if i[0].ndim == 0:
            f.write(param + i[1]  + defas + str(i[0]) + ';\n\n')
            
        elif i[0].ndim == 1:
            f.write(param + i[1] + defas  + '\n')
            for j in range(i[0].size):
                f.write(str(j) + '\t' + str(i[0][j]) + '\n')

            f.write(';\n\n')

        else:
            f.write(param + i[1] + ': ')
            for k in range(i[0][1].size):
                f.write(str(k) + ' ')
            f.write(defas + '\n')

            for j in range(i[0].shape[0]):
                f.write(str(j) + '\t')
                for k in range(i[0].shape[1]):
                    f.write(str(i[0][j][k]) + '\t')
                f.write('\n')

            f.write(';\n\n')            

        
    f.close()

#function that puts variables in a readable format
def writetotxt(filename,params):
    f = open(filename + '.txt', "a")

    for i in params:
        if i[0].ndim == 0:
            f.write(i[1]  + '\n' + str(i[0]) + '\n\n')
            
        elif i[0].ndim == 1:
            f.write(i[1]  + '\n')
            for j in range(i[0].size):
                f.write(str(i[0][j]) + '\n')

            f.write('\n\n')

        else:
            f.write(i[1] + '\n')


            for j in range(i[0].shape[0]):
                for k in range(i[0].shape[1]):
                    f.write(str(i[0][j][k]) + '\t')
                f.write('\n')

            f.write('\n\n')            

        
    f.close()