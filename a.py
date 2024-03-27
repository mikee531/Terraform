import os, sys

slack_token = sys.argv[1]
os.makedirs('/Users/sairamdeepak/Downloads/'+slack_token)
print(slack_token)
#print(os.system('pwd'))
