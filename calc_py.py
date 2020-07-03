import os

fieldsPath = "YOUR CALCULATED FIELDS"
localPath = ""
propsLocalPath = ""
propsDefaultPath = ""
folder = ""
lineIndex = 0
visited = False

with open(fieldsPath, 'r') as file:

  			for line in file:
  				stripped_line = line.strip()

  				if stripped_line[:3] == 'app':
  					for i in range(lineIndex):
  						file.next()

  					for line in file:
  						if lineIndex == 0:
  							folder = stripped_line[4:]

  						stripped_line = line.strip()

  						if stripped_line[:3] == 'app' and lineIndex != 0:
  							folder = stripped_line[4:]
  							visited = False
  							continue

						localPath = "$SPLUNK_HOME/etc/"+folder+"/local/"
						propsLocalPath = "$SPLUNK_HOME/etc/"+folder+"/local/props.conf"
						propsDefaultPath = "$SPLUNK_HOME/etc/"+folder+"/default/props.conf"

  						if os.path.exists(localPath) == True and os.path.exists(propsLocalPath) == True:						
  							if visited == False:
  								os.system("cp -r "+propsLocalPath+" "+localPath+"props.conf.backup")
  								fileAdd = open(propsLocalPath, 'a')
  								fileAdd.write("\n"+stripped_line+"\n")
  								visited = True
  							else:
  								fileAdd = open(propsLocalPath, 'a')
  								fileAdd.write("\n"+stripped_line+"\n")

  						elif os.path.exists(localPath) == True and os.path.exists(propsLocalPath) == False:
  							os.system("cp -r "+propsDefaultPath+" "+localPath)

  							if visited == False:
  								os.system("cp -r "+propsLocalPath+" "+localPath+"props.conf.backup")
  								fileAdd = open(propsLocalPath, 'a')
  								fileAdd.write("\n"+stripped_line+"\n")
  								visited = True
  							else:
  								fileAdd = open(propsLocalPath, 'a')
  								fileAdd.write("\n"+stripped_line+"\n")

  						elif os.path.exists(localPath) == False and os.path.exists(propsLocalPath) == False:
  							os.system("mkdir "+localPath)
  							os.system("cp -r "+propsDefaultPath+" "+localPath)

  							if visited == False:
  								os.system("cp -r "+propsLocalPath+" "+localPath+"props.conf.backup")
  								fileAdd = open(propsLocalPath, 'a')
  								fileAdd.write("\n"+stripped_line+"\n")
  								visited = True
  							else:
  								fileAdd = open(propsLocalPath, 'a')
  								fileAdd.write("\n"+stripped_line+"\n")

  						lineIndex+=1

  				
  		