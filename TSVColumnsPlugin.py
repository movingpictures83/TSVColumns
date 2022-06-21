import PyPluMA

class TSVColumnsPlugin:
    def input(self, inputfile):
       infile = open(inputfile, 'r')
       self.params = dict()
       for line in infile:
           contents = line.strip().split('\t')
           self.params[contents[0]] = contents[1]
       self.csvfile = open(PyPluMA.prefix()+"/"+self.params["tsvfile"], 'r')
       colfile = open(PyPluMA.prefix()+"/"+self.params["columns"], 'r')
       columns = []
       for line in colfile:
           line = line.strip()
           columns.append(line)
       self.colindices = []
       firstline = self.csvfile.readline()
       self.header = firstline.strip().split('\t')
       for column in columns:
           self.colindices.append(self.header.index(column))

    def run(self):
        pass

    def output(self, outputfile):
       outfile = open(outputfile, 'w')
       for i in range(len(self.colindices)):
           outfile.write(self.header[self.colindices[i]])
           if (i == len(self.colindices)-1):
               outfile.write('\n')
           else:
               outfile.write('\t')
       for line in self.csvfile:
          line = line.strip().split('\t')
          for i in range(len(self.colindices)):
              outfile.write(line[self.colindices[i]])
              if (i == len(self.colindices)-1):
               outfile.write('\n')
              else:
               outfile.write('\t')

