import xml.etree.cElementTree as et
import csv 
import os

#arquivos de entrada e saida 
for file in os.listdir('files/input/'):
    tree = et.parse('files/input/' + file)
    root = tree.getroot()

    #salvando dados das pessoas
    header = ['ID', 'project', 'BrainMaskNVox', 'BrainMaskVol', 'BrainSegNVox', 'BrainSegVol', 'ICV']
    subject = []

    subject.append(root.attrib.get('ID'))
    subject.append(root.attrib.get('project'))
    subject.append(root.find('{http://nrg.wustl.edu/fs}BrainMaskNVox').text)
    subject.append(root.find('{http://nrg.wustl.edu/fs}BrainMaskVol').text)
    subject.append(root.find('{http://nrg.wustl.edu/fs}BrainSegNVox').text)
    subject.append(root.find('{http://nrg.wustl.edu/fs}BrainSegVol').text)
    subject.append(root.find('{http://nrg.wustl.edu/fs}ICV').text)

    with open('files/output/subjects.csv', 'a', newline = '') as subjects:
        writer = csv.writer(subjects, delimiter = ',')
        #writer.writerow(header)
        writer.writerow(subject)
        print('Sujeito incluído com sucesso!!')

    header = ['SegId', 'name', 'hemisphere', 'NVoxels', 'Volume', 'normMean', 'normStdDev', 'normMin', 'normMax', 'normRange']
    with open('files/output/' + subject[0] + '.csv', 'w', newline = '') as subjects:
        writer = csv.writer(subjects, delimiter = ',')
        writer.writerow(header)
        data = []
        regions = root.findall('{http://nrg.wustl.edu/fs}regions')
        for region in regions:
            for child in region:
                data.append(child.attrib.get('SegId'))
                data.append(child.attrib.get('name'))
                data.append(child.attrib.get('hemisphere'))
                data.append(child.find('{http://nrg.wustl.edu/fs}NVoxels').text)
                data.append(child.find('{http://nrg.wustl.edu/fs}Volume').text)
                data.append(child.find('{http://nrg.wustl.edu/fs}normMean').text)
                data.append(child.find('{http://nrg.wustl.edu/fs}normStdDev').text)
                data.append(child.find('{http://nrg.wustl.edu/fs}normMin').text)
                data.append(child.find('{http://nrg.wustl.edu/fs}normMax').text)
                data.append(child.find('{http://nrg.wustl.edu/fs}normRange').text)
                writer.writerow(data)
                data.clear()
        print('Dados do sujeito salvos com sucesso!') 
            




