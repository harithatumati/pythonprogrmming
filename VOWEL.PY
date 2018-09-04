alphabet=input('raw_input()')
if (alphabet in ['a','e','i','o','u','A','E','I','O','U']):
 print('Vowel')
elif(alphabet in ['b','c','d','f','g','h','k','l','m','n','j','p','q','r','s','t','v','w','x','y','z','B','C','D','F','G','H','K','J','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']):
 print('Constant')
else:
 print('invalid')
