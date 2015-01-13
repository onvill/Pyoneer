from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("language.xml")
dictionary = DOMTree.documentElement
wordBank = ["File","Choose Language","Help","Choose Language","Help","","","","4","5","6","","12","13","14","15","16","17","18","","","21","","","","","","","28","","","","","","34","","","","","39","","","","","","","","","","49"]

class Readerr():     
    def reader1(self,choice):
        lang = dictionary.getElementsByTagName('language')[choice]
        
        one = lang.getElementsByTagName('one')[0]
        wordBank[0] = one.childNodes[0].data
        
        two = lang.getElementsByTagName('two')[0]
        wordBank[1] = two.childNodes[0].data
        
        three = lang.getElementsByTagName('three')[0]
        wordBank[2] = three.childNodes[0].data
        
        four = lang.getElementsByTagName('four')[0]
        wordBank[3] = four.childNodes[0].data
        
        five = lang.getElementsByTagName('five')[0]
        wordBank[4] = five.childNodes[0].data
        
        hello = lang.getElementsByTagName('hello')[0]
        wordBank[5] = hello.childNodes[0].data
        
        ChapterOne = lang.getElementsByTagName('ChapterOne')[0]
        wordBank[6] = ChapterOne.childNodes[0].data
        
        ChapterTwo = lang.getElementsByTagName('ChapterTwo')[0]
        wordBank[7] = ChapterTwo.childNodes[0].data
        
        ChapterThree = lang.getElementsByTagName('ChapterThree')[0]
        wordBank[8] = ChapterThree.childNodes[0].data

        ChapterFour = lang.getElementsByTagName('ChapterFour')[0]
        wordBank[9] = ChapterFour.childNodes[0].data
        
        ChapterFive = lang.getElementsByTagName('ChapterFive')[0]
        wordBank[10] = ChapterFive.childNodes[0].data

        ChapterSix = lang.getElementsByTagName('ChapterSix')[0]
        wordBank[11] = ChapterSix.childNodes[0].data

        ChapterSeven = lang.getElementsByTagName('ChapterSeven')[0]
        wordBank[12] = ChapterSeven.childNodes[0].data

        starte = lang.getElementsByTagName('starte')[0]
        wordBank[13] = starte.childNodes[0].data
        
        exit = lang.getElementsByTagName('exit')[0]
        wordBank[14] = exit.childNodes[0].data
        
        about = lang.getElementsByTagName('about')[0]
        wordBank[15] = about.childNodes[0].data
        
        helpe = lang.getElementsByTagName('helpe')[0]
        wordBank[16] = helpe.childNodes[0].data
        
        change = lang.getElementsByTagName('change')[0]
        wordBank[17] = change.childNodes[0].data

        N18 = lang.getElementsByTagName('N18')[0]
        wordBank[18] = N18.childNodes[0].data
        
        N19 = lang.getElementsByTagName('N19')[0]
        wordBank[19] = N19.childNodes[0].data
        
        N20 = lang.getElementsByTagName('N20')[0]
        wordBank[20] = N20.childNodes[0].data

        welldone = lang.getElementsByTagName('welldone')[0]
        wordBank[21] = welldone.childNodes[0].data

        opps = lang.getElementsByTagName('opps')[0]
        wordBank[22] = opps.childNodes[0].data

        section1Q1 = lang.getElementsByTagName('section1Q1')[0]
        wordBank[23] = section1Q1.childNodes[0].data
        ###### Section 2 Question 1-5
        section2Q1 = lang.getElementsByTagName('section2Q1')[0]
        wordBank[24] = section2Q1.childNodes[0].data
        section2Q2 = lang.getElementsByTagName('section2Q2')[0]
        wordBank[25] = section2Q2.childNodes[0].data
        section2Q3 = lang.getElementsByTagName('section2Q3')[0]
        wordBank[26] = section2Q3.childNodes[0].data
        section2Q4 = lang.getElementsByTagName('section2Q4')[0]
        wordBank[27] = section2Q4.childNodes[0].data
        section2Q5 = lang.getElementsByTagName('section2Q5')[0]
        wordBank[28] = section2Q5.childNodes[0].data

        section3Q = lang.getElementsByTagName('section3Q')[0]
        wordBank[29] = section3Q.childNodes[0].data

        section4Q1 = lang.getElementsByTagName('section4Q1')[0]
        wordBank[30] = section4Q1.childNodes[0].data
        section4Q2 = lang.getElementsByTagName('section4Q2')[0]
        wordBank[31] = section4Q2.childNodes[0].data
        section4Q3 = lang.getElementsByTagName('section4Q3')[0]
        wordBank[32] = section4Q3.childNodes[0].data
        section4Q4 = lang.getElementsByTagName('section4Q4')[0]
        wordBank[33] = section4Q4.childNodes[0].data
        section4Q5 = lang.getElementsByTagName('section4Q5')[0]
        wordBank[34] = section4Q5.childNodes[0].data

        ###### Section 5 Question 1-5
        section5Q1 = lang.getElementsByTagName('section5Q1')[0]
        wordBank[35] = section5Q1.childNodes[0].data
        section5Q2 = lang.getElementsByTagName('section5Q2')[0]
        wordBank[36] = section5Q2.childNodes[0].data
        section5Q3 = lang.getElementsByTagName('section5Q3')[0]
        wordBank[37] = section5Q3.childNodes[0].data
        section5Q4 = lang.getElementsByTagName('section5Q4')[0]
        wordBank[38] = section5Q4.childNodes[0].data
        section5Q5 = lang.getElementsByTagName('section5Q5')[0]
        wordBank[39] = section5Q5.childNodes[0].data

        ###### Section 6 Question 1-5
        section6Q1 = lang.getElementsByTagName('section6Q1')[0]
        wordBank[40] = section6Q1.childNodes[0].data
        section6Q2 = lang.getElementsByTagName('section6Q2')[0]
        wordBank[41] = section6Q2.childNodes[0].data
        section6Q3 = lang.getElementsByTagName('section6Q3')[0]
        wordBank[42] = section6Q3.childNodes[0].data
        section6Q4 = lang.getElementsByTagName('section6Q4')[0]
        wordBank[43] = section6Q4.childNodes[0].data
        section6Q5 = lang.getElementsByTagName('section6Q5')[0]
        wordBank[44] = section5Q5.childNodes[0].data

        ###### finalTest
        finalExam1 = lang.getElementsByTagName('finalExam1')[0]
        wordBank[45] = finalExam1.childNodes[0].data
        finalExam2 = lang.getElementsByTagName('finalExam2')[0]
        wordBank[46] = finalExam2.childNodes[0].data
        finalExam3 = lang.getElementsByTagName('finalExam3')[0]
        wordBank[47] = finalExam3.childNodes[0].data
        finalExam4 = lang.getElementsByTagName('finalExam4')[0]
        wordBank[48] = finalExam4.childNodes[0].data
        finalExam5 = lang.getElementsByTagName('finalExam5')[0]
        wordBank[49] = finalExam5.childNodes[0].data
