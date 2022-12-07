
import fitz
import fnmatch
import os
import math

### scoring global variables
score = 0
FScore = 0
Keywords = ['LipE', ' selectiv', ' pan-', 'isoform', 'hERG', 'Kp ', ' Kp', ' Kpuu', 'P-gp', 'efflux', 'Papp',
            ' KI ', '/KI' , 'Kinact',
            'CNS', 'BBB', 'MDR1', 'Vd ', 'GSH', 'metabolite',
            'BSEP', 'PPB', 't1/2', 'bioavailability', 'CLint', 'unbound', 'F (%)', 'F %', '% F ', ' KD', 'KD '
            'efflux', ' AUC ', '(AUC)', ' AUC0', ' AUC(', ' CL (', ' CL ', ' Clp ', ' CLhep ', ' Clint ', ' Clu ',
            ' LLE']

### READ IN PDF
for file in os.listdir('PDFS'):
    if fnmatch.fnmatch(file, '*.pdf'):
        document = os.path.join('PDFS', file)
        doc = fitz.open(document)

        #doc = fitz.open("acs.jmedchem.2c01102.pdf")


        for page in doc:

            for x in range(len(Keywords)):
                ### SEARCH
                text = Keywords[x]
                text_instances = page.search_for(text)

                ### HIGHLIGHT
                for inst in text_instances:
                    highlight = page.add_highlight_annot(inst)
                    highlight.update()
                    score = score + 1
            FScore = FScore + pow(1.05,score)

        ### OUTPUT
        FScore = math.ceil(FScore)
        doc.save("PDFS\{}.pdf".format(FScore), garbage=4, deflate=True, clean=True)
        print(FScore)
        score = 0
        FScore = 0
