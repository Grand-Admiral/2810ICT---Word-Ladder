import V2word_ladderT
import unittest

class TestLadder(unittest.TestCase):
    # Try to open dictionary
    try:
        file = open('dict.txt')
        lines = file.readlines()
    except:
        print('Error. Test file requires dictionary (dict.txt).')
        exit()
        
    #generate data for testing use
    global words
    words = []
    for line in lines: #Regenerate word list
        word = line.rstrip()
        if len(word) == 4: #using only 4 letter words in test
            words.append(word)
    global seen
    seen = {'hide': True}
    global list
    list = ['aide', 'bide', 'eide', 'nide', 'ride', 'side', 'tide', 'vide', 'wide', 'hade', 'hike', 'hire', 'hive']

    def testFileIncorrect(self): #test when file does not exist
        result = V2word_ladderT.main('invalid-file-name', 'hide', 'seek', '', 'y', 'n')
        self.assertEqual(result,'File does not exist')
        
    def testTargetSame(self): #test when target word is same as start word
        result = V2word_ladderT.main('dict.txt', 'hide', 'hide', '', 'y', 'n')
        self.assertEqual(result,'Error. Start and target words cannot be the same. Try again.')
    
    def testInputCaseUpper(self): #test when y/n has varying cases (upper)
        result = V2word_ladderT.main('dict.txt', 'hide', 'seek', '', 'Y', 'N')
        self.assertIsNone(result)
    def testInputCaseLower(self): #test when y/n has varying cases (lower case)
        result = V2word_ladderT.main('dict.txt', 'hide', 'seek', '', 'y', 'n')
        self.assertIsNone(result)
        
    def testSame0(self): #test the same() function
        result = V2word_ladderT.same('hide','seek')
        self.assertEqual(result,0)
    def testSame1(self):
        result = V2word_ladderT.same('lead','gold')
        self.assertEqual(result,1)
    def testSame2(self):
        result = V2word_ladderT.same('seek','seal')
        self.assertEqual(result,2)
    def testSame3(self): #long test
        result = V2word_ladderT.same('presumptuous','unfamiliarly')
        self.assertEqual(result,0)

    def testBuild(self): #test the build() function
        result = V2word_ladderT.build('h.de', words, seen, list)
        self.assertEqual(result,[])




if __name__ == '__main__':
    unittest.main()
